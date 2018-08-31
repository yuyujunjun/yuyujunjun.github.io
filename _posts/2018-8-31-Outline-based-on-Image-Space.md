---
layout: post
current: post
cover:  assets/images/Outline/1.gif
navigation: True
title: Outline based on Image Space
date: 2018-8-31 00:00:00 +800
tags: [unity,Visual Effect]
class: post-template
author: yuyujunjun
---

# Outline(Based on Image Space)



![Visual effect](/assets/images/Outline/1.gif)

## 引言

图中的碎面特效在浅色背景下效果不明显。而如果在unity编辑器中选中该物体，unity会给它进行描边，而这个效果比较符合要求。

<img src="/assets/images/Outline/editorline.png" width="40%"/><img src="/assets/images/Outline/editornoline.png" width="40%"/>

描边方法多样，原理大多都通俗易懂，这篇文章重点是介绍一些unity与之相关的API。

## 优势及应用

1. 可以描绘出对象身上一切镂空的部位，不论是内边界还是外边界。

2. 可以根据需要判断遮挡（无非就是多添加一个纹理缓存）



**不足**

无法判断法向量突变的“边界”，所以如果只使用这个方法，和卡通渲染给人的感觉可能会不同。

## 基本原理

倒过来想，对于图像中的某个对象（比如说，那个球），如果我们要对它进行描边，我们需要它的边界位置，边界大小和边界颜色。

而从正面想，我们想要给一幅图像上的一片像素点组成的形状进行描边。首先我们需要获取该形状在图像上的位置，随后我们对它边界处的像素点进行标定，这个步骤很自由，因为理论上你可以用各式各样的标定方法，标定各式各样的形状，只要保证在GPU上并行实现即可，最后我们再将这些标定位置的像素点覆盖到原图像上，即可进行描边。

## 步骤

第一步：

<img src="/assets/images/Outline/pos.png"/>

这一步就是记载其位置，图示只是为了便于说明，所以用了一张常规的渲染结果。实际上我们最终使用的是其深度图，深度图的好处是，深度图变相标明了有对象的区域和没有对象的区域。没有对象的区域深度值当然全部都为1。

第二步:

<img src="/assets/images/Outline/outline.png"/>

第二步我们将第一步获取到的图片的边界进行拓展，对边界区域写入一个值。可以看出这张图片相较于上一张“粗犷”了许多。

关于如何判断是否是该物体的边界，因为我们上一张图片已经标明了对象区域和非对象区域，那么我们只需要对每个像素点周围采样，如果周围有像素点在对象区域内，则该像素点应该为边界。

这里有一个小trick，只要周围采样的点的值加起来不为0，则可以判断其为边界。代码如下：

```c#
fixed4 col1 = tex2D(_MainTex,i.screenPos.xy);
fixed4 col2 = tex2D(_MainTex,float2(i.screenPos.x + 4/_ScreenParams.x,i.screenPos.y));
fixed4 col3 = tex2D(_MainTex,float2(i.screenPos.x - 4/_ScreenParams.x,i.screenPos.y));
fixed4 col4 = tex2D(_MainTex,i.screenPos.xy);
fixed4 col5 = tex2D(_MainTex,float2(i.screenPos.x ,i.screenPos.y+ 4/_ScreenParams.y));
fixed4 col6 = tex2D(_MainTex,float2(i.screenPos.x ,i.screenPos.y- 4/_ScreenParams.y));
if((col1.x + col1.y + col1.z  + col2.x + col2.y + col2.z + col3.x + col3.y + col3.z + col4.x + col4.y + col4.z + col5.x + col5.y + col5.z+ col6.x + col6.y + col6.z)>0.01) 
return fixed4(_OutlineColor.rgb,i.vertex.z);
```

有趣的是，这一步可以非常复杂，而这里只是进行了简单的扩张。

第三步：

<img src="/assets/images/Outline/final.png"/>

第三步我们便将边界处的像素叠加上去，这时候，第一步的结果起了不同的作用。在第二步中，第一步的结果的目的是标识物体位置以便于第二步勾画边界，而在第三步中，是为了和第二步的结果作减法来告诉我们哪些地方不是边界，而是对象本身。

**注意事项**

虽然以上两张图（一张标定位置，一张标定边界）就可以完成基于图形空间的描边，但事实上如果需要判断遮挡性或者为边界添加特殊的辅助效果，大可以再增加一些缓存，这个自己权衡就好。

## 部分代码（API介绍）

**使用替换的着色器对场景进行渲染**

功能：相机会照常渲染场景，但是场景中的物体会使用你所规定的shader渲染。

这个功能的用处是：比如说，需要渲染一张场景法线信息的贴图，或者我们上面提到的我们要渲染的场景深度信息的贴图。

这个功能对应了两个API，分别是：

```C#
Camera.RenderWithShader(Shader shader,string replacementTag)
```

```C#
Camerea.SetReplacementShader(Shader shader,string replacementTag)
```

解释一下replacementTag的用处，如果该tag为空，那么该相机能渲染的所有对象都会使用我们所定制的shader。如果有值，那么该相机只会渲染拥有特定Tag的材质。比如：

```C#
Camerea.SetReplacementShader(depthshader,"RenderType")
```

相机只会渲染Render Type和depthshader的Render Type值相同的物体。

unity Shader中，如下方法指定shader的tag：

```cg
Tags { "TagName1" = "Value1" "TagName2" = "Value2" }
```

在Replacement Shader中，可以有多个subshader。对于一般的shader来说，subshader从上到下执行，如果第一个subshader由于硬件原因无法被执行，则会执行下一个，直到可以执行为止。

而这里的subshader发挥着类似的作用，如果subshader中有ReplacementTag，那么该subshader就会用于渲染真实场景的物体中，tag值和此subshader 的tag值相同的物体。

**使用特定着色器将原始图像拷贝到新图像上**

```C#
Graphics.Blit(RenderTexture src,RenderTexture dst,Material mat)
```



工程链接：

> https://github.com/yuyujunjun/OutLine_Geometry





