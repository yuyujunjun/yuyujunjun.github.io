---
layout: post
current: post
navigation: True
title: Unity Shadow
date: 2018-9-9 00:00:00 +800
tags: [unity,Graphics,Rendering]
class: post-template
author: yuyujunjun
---

# Unity Shadow 

## Screen-based shadow map

只想知道API请直接翻到最后。

主流游戏引擎，包括unity所使用的阴影技术都为ShadowMap。而对于unity来说，在硬件支持的情况下，其使用的并非是原始的ShadowMap，而是ScreenBaseShadowMap。

思想与deferred shading类似，判断屏幕空间的阴影关系。渲染的时候首先得到相机空间的深度图和光源的shadowmap，然后在屏幕空间对所有shadowmap做一次阴影收集计算（考虑到每个光源可能都有一张自己的shadowmap）。阴影收集计算其实就是一个判断点是否在阴影中的过程，首先将屏幕坐标根据深度图变成三维坐标坐标，然后换算到shadowmap的坐标系下，再进行深度值的比较即可。如果小于shadowmap的深度值，则代表其处于阴影之中。

在实际shading过程中，我们会在顶点着色器中计算出每个点的屏幕坐标，而在片段着色器中，对阴影收集图根据屏幕坐标进行采样。这样计算所造成的问题是，相机看不见的位置，它们的阴影，与相同xy坐标且相机能看见那个点阴影相同。这当然是错误的，但是那又怎样，反正你也看不见它。

这个结论很容易验证，后面会提到unity如何渲染深度图，我会在那里对这个“错误”进行验证。

所以，如果需要一个物体投射阴影，它只需要写入光源的shadowmap即可。如果需要一个物体接受阴影，它必须写入相机的深度图。

这个结论非常有用，它可以帮助我们理解unity中透明物体的阴影。那么，透明物体有什么特殊的地方呢，比起不透明的物体来说？

透明物体会进行深度检测，但它们并不写入深度图，否则就会挡住后面的不透明物体。这也是为什么透明物体的渲染顺序非常重要的原因了，它们必须在不透明物体之后渲染，渲染它们的时候还得根据它们距离相机的远近关系大致排列一下顺序。不过这并不是这篇文章的重点。

重点是：

>  unity中的透明物体是不能接受阴影的，但是它可以投射阴影。

这句话的意思翻译一下，就是说，unity的透明物体是不会写入深度图的（和前面说的一样），但是它会写入shadowmap。

见下面这张图，紫色的平面为半透明材质，光在紫色平面的正上方，一块板子在紫色平面的下方。在第一幅图中，右侧为光源的深度图（光源渲染的结果是正交视图），而第二副图则是相机空间的深度图。在写入shadowmap中，透明物体会根据透明度进行写入。

<img src="assets/images/ShadowMap/transparentshadowmap.png" style="float:left;" /><img src="assets/images/ShadowMap/transparentdepth.png" style="float:right;" />

## 渲染深度图

理解了基于屏幕空间的深度图原理，我们再来看看unity中我们可以参与哪些步骤。

为了得到相机空间的深度图和光源的阴影纹理，首先需要渲染一遍场景中的物体（如果是前向渲染），由于只需要获取深度信息，并不需要走一遍复杂的光照模型，此刻最好可以单独使用一个简单的Pass。这里使用是 "LightMode"的值为"ShadowCaster"的Pass，也就是说当你写了一个pass，它的LightMode等于字符串"ShadowCaster"，就会被用于深度图的渲染中。通常情况下，unity会自动帮你生成这个Pass，自然，自动生成的pass渲染出来的结果会和最开始的Mesh长得一模一样，如果你的shader里有任何对顶点位置的操作，为了保证正确的阴影关系，你最好自己实现那个步骤。

例如，在这张图中，在渲染的时候我将顶点位置平移到紫色平面以上，但并没有改动ShaowCaster Pass，在右侧深度图中，它的深度信息还是保存在原来的位置。这显然不能得到正确的阴影关系，因为如果它的屏幕位置所对应的深度信息是某个其他像素点的深度信息，它的阴影关系也会变得和那个像素点一样。

<img src="assets/images/ShadowMap/shadowcasterwrong.png" style="float:left" />

如果你不想让它对环境产生阴影，最简单的方法就是你自己写一个shadowcaster，但是强制关闭深度写入。

以下两幅图分别为```ZWrite Off```和```ZWrite On```

<img src="assets/images/ShadowMap/ZwriteOff.png" style="float:left; width:45%" /><img src="assets/images/ShadowMap/ZwriteOn.png" style="float:right;width:45%" />

## 实现步骤

喜闻乐见的贴代码环节。

其实没啥好贴的，unity为我们跨平台使用定义了非常多的宏，经常用到的只有这三个，我猜测它们在我的电脑上（dx11 windows10）是这些：

```cg
#include "autolight.cginc"
#include "autolight.cginc"
struct v2f(){
	float4 pos:SV_POSITION;
	...
	SHADOW_COORDS(id)//float4/half4/fixed4 _ShadowCoord:TEXCOORD(id)
	...
}
v2f vert(){    
	...
	TRANSFER_SHADOW(o)//o._ShadowCoord=ComputeScreenPos(o.pos)
	return o;
}
fixed4 frag(v2f i){
	fixed shadow=SHADOW_ATTENUATION(i);//tex2Dproj(_ShadowMapTexture,i._ShadowCoord).r
}
```



本质就是计算得到屏幕坐标然后对```_ShadowMapTexture```进行采样。注意```SV_Position```所对应的变量的命名必须为```pos```，这里还是建议考虑到跨平台特性尽量用宏。