---
layout: post
current: post
cover:  assets/images/welcome.jpg
navigation: True
title: Get mesh from gpu and export obj
date: 2018-8-25 00:00:00 +800
tags: [bugs,unity,mesh]
class: post-template
author: yuyujunjun
---

## Tasks

获取GPU生成的顶点数据填入Unity支持的Mesh ，并将其导出为Obj

顶点数据在GPU中的处理方式：

我利用compute shader 生成一系列顶点数据（Marching Cubes算法），让它们每三个为一组，用一个结构体保存，并统一存储在一个compute buffer 中。紧接着我将Compute Buffer丢给GPU，shader根据自己的id从buffer中取出顶点数据并渲染出来。

对于每个GPU线程，都会根据线程id，在buffer上获取对应的顶点信息，并渲染出来。

**此时没有传入顶点索引数组哦，为什么它可以正常渲染呢？**

我猜测可能线程id充当了一部分顶点数组的作用，在unity的官方文档中，并没有对此做太多说明: 

> A vertex shader can receive a variable that has the “vertex number” as an unsigned integer. This is mostly useful when you want to fetch additional per-vertex data from textures or [ComputeBuffers](https://docs.unity3d.com/Manual/ComputeShaders.html).



## Working

我用C#写了一个和Shader里存储方式完全一样的结构体（类C风格），并利用 ```GetData()```  函数从GPU中读取到CPU中来。随后将其顶点数据，法向量数据，UV数据分别拿出来各自存入数组中，并按顺序给顶点索引赋值，因为相邻三个点必定属于一个三角面片，所以我只需要按顺序赋值即可正常绘制。

之后赋给Unity的标准Mesh，然后将其打包成Obj。

## Problem Description

在顶点数量不多的情况下正常显示，但当顶点数量更大的时候导出的模型出现破面，甚至不能通过第三方软件打开OBJ。

## Solution Guess

1. 会不会是预先分配的数组大小的问题？
   1. + 我的数组分配大小就为Compute Buffer中的三角形数量乘3，没有问题。
2. 会不会是```GetData()```函数读取数据的问题？
   1. + 不知道这个怎么检查，就很佛系地把```GetData()```得到的数据又丢了回去，发现正常可以显示，那就先把这个问题搁置。
3. 会不会是OBj导出的问题？
   1. + 于是把手写的导出换成了插件，问题依旧存在，直到后来我把导出前的数据显示了出来，发现依旧有破面，才排除这个问题。

## Problem Analyze

经过多次实验发现其中总是有一小块位置模型是好的，推测可能是排在前面的数据正常显示了，而后面的数据丢失或者乱了。

这依旧有可能是数组越界的问题，我依旧检查了所有涉及到的数组。

最后我打开了OBJ文件，发现f，也即是指定OBJ的面的关键词，后面跟着的是顶点索引信息，也就是我顺序赋值的东西，在超过65000多个后又重新从0开始变化了（没仔细看，但应该是65535附近的某个数）。

原来是顶点索引的值超过了unity的类型取值范围，unity支持的单个模型的顶点数量不超过65000个，我的解决方法就是借助一个字典，在读取顶点数据的同时将相同的顶点索引合并，让位置相同的顶点只作为一个顶点出现。

因为是在协程中使用的缘故并没有拖慢帧率，反而同时优化了存储和读取。