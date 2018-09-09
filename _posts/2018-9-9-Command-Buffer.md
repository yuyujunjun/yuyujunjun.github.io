---
layout: post
current: post
navigation: True
title: Command Buffer
date: 2018-9-9 00:00:01 +800
tags: [unity,Graphics,Rendering]
class: post-template
author: yuyujunjun
---

# Command Buffer

我学习Command Buffer是和屏幕后处理类比来学习的，我感觉（并不知道是不是这样），```OnRenderImage```的内部原理就是Command Buffer。

```c#
Graphics.Blit(RenderTexture src,RenderTexture dest,Material mat=null);//OnRenderImage
CommandBuffer CB=new CommandBuffer();
CB.Blit(RenderTargetIdentifier source,RenderTargetIdentifier dest,Material mat=null);//Command Buffer

```

看起来极为类似，不过```OnRenderImage```是在渲染结束后执行，而Command Buffer可以插进渲染的任何一步：

```c#
Camera.AddCommandBuffer(CameraEvent,CB);
Light.AddCommandBuffer(LightEvent,CB);
```

如何将```RenderTexture```转换成```RenderTargetIddentifier```:

```c#
//Temporary RenderTexture
int id=Shader.PropertyToId("_TextureName");
CB.GetTemporaryRT(id,width,height,depthbuffer,FilterMode);//生成名字为_TextureName的RenderTexture并给编号id赋值
CB.ReleaseTemporaryRT(id);//释放编号id的rendertexture
//已有RenderTexture
RenderTargetIdentifier id=new RenderTargetIdentifier(rt);
```

如何获取当前状态的RenderTexture（对应于```OnRenderImage```的source）：

```c#
BuiltinRenderTextureType.CurrentActive
```

给这个buffer中所有shader的变量赋值:

```c#
CB.SetGlobalVector();
CB.SetGlobalTexture();
...
```

举例：把一张光源的shadowmap掏出来贴到屏幕上：

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;
[ExecuteInEditMode]
public class grabdepth : MonoBehaviour {
    public Light ml;
    public RenderTexture rt;
	// Use this for initialization
	void Start () {
       
        CommandBuffer buf = null;
        buf = new CommandBuffer();
        buf.SetShadowSamplingMode(BuiltinRenderTextureType.CurrentActive, ShadowSamplingMode.RawDepth);
        RenderTargetIdentifier id = new RenderTargetIdentifier(rt);
        buf.Blit(BuiltinRenderTextureType.CurrentActive,id );
        ml.AddCommandBuffer(LightEvent.AfterShadowMap, buf);
    }
	

    private void OnRenderImage(RenderTexture source, RenderTexture destination)
    {
        Graphics.Blit(rt,destination);
    }
}
```

