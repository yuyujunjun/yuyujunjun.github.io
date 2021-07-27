---
layout: post
current: post
cover:  assets/images/tags.jpg
navigation: True
title: Unity Tips
date: 2018-8-25 00:00:00 +800
tags: [unity,unity tips]
class: post-template
author: yuyujunjun
---



## 文件和资源的读取和存储

>  引子： 开发者们对Assets文件夹并不陌生，我们进行游戏开发的几乎所有资源都会保存在这儿，很多时候我们可以直接根据路径进行文件读取。但随着unity的打包，资源该合并合并该压缩压缩，文件目录就发生了变化。



### Resources

unity在打包过程中，会将Assets目录及其所有子目录下的名字为Resources的文件夹合并，并加密压缩。压缩意味着在玩家进行游戏中，我们不能再往里面写入东西了。
调用API：

```C#
    Resource.Load("test");//返回获取到的第一个名字是test的文件
    Resource.LoadAll("test")//返回所有名字是test的文件
```

注意事项：

1. 只能读取不能写入
2. 在程序启动时会对Resources下的所有对象初始化，构建实例ID。这个过程耗时非线性增加，可能导致程序启动时间过长。

### StreamingAssets

 命名为StreamingAssets的文件夹为流文件夹，此文件夹资源不会压缩加密，它会一模一样出现在游戏数据文件夹下。在windows平台下，这个目录是可以写入的，所以我们可以进行更新。


+ 其路径为：Application.streamingAssets

###   PersistentDataPath

与Assets文件夹无关，在系统的某个地方，在windows上应该是C:/user/Appdata/.../，自然也不会经过unity的压缩和加密。

### 文件读取

unity对于文件的读取，不包括AssetBundle存在两种方式，IO和WWW。

+ IO: 新建一个文件流，正常读写即可。

+ WWW：WWW是unity封装的网络下载模块，支持Http，也同时支持文件读取。WWW是异步加载方式，并会将加载的资源转换成Unity能使用的AssetsComponents。例如：

  ```C#
  using(WWW www=new WWW(filePath)){
      yield return www;
      var xxx=www.text;//
      var xxx=www.texture;//可直接处理成unity可以用的Components
  }
  ```

