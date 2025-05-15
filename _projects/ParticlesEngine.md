---
title: "Cross-platform Particles Effects Engine"
collection: projects
date: 2020-9-1
video: /images/particle.mp4
teaser: /images/particle.png
desc: "Designed and implemented a high-performance particle engine with full support for real-time editing and rendering on resource-constrained platforms" 
first_author: "yes"
---

We have built a mobile particle system engine based on Vulkan. 
We have a sample [video](/images/particle.mp4) available that demonstrates the use of the flock motion and surface attraction functions of our engine.

### Abstract

While visually stunning particle special effects and specific functions often require computationally-intensive algorithms, these can significantly impact the computing performance of mobile devices. This can affect the user's real-time experience and quickly consume battery life. Balancing computing performance, power consumption, and particle system effects of mobile devices remains a challenge.

To meet this challenge, we developed a cross-platform particle special effects system that satisfies the daily interaction needs of mobile devices. We chose Vulkan as our graphics API, as it supports cross-platform and multi-threaded rendering pipelines, offering better performance.

Common particle special effects often require calculating the animation of thousands of particles within a frame and supporting complex algorithms such as collision detection, which poses a significant challenge to device performance and power consumption. To achieve efficient interaction between particles and models, we innovatively introduced the Signed Distance Field (SDF) to improve performance.

Designers can efficiently achieve particle attraction, repulsion, and surface movement with constant complexity by importing the SDF of the model. To meet design needs, the system supports various common effects such as collision avoidance, surface attraction, flock motion, vortex force, and wind force. It also supports simplified group motion based on the Boids model, noise movement, and particle movement to the specified location.

Moreover, the system provides animation editing and playback based on keyframes. Designers can modify particle attributes arbitrarily, and the system automatically performs interpolation. This system has been commercially applied on Oppo smartphones under the umbrella of OnePlus Technology Co., Ltd.

The basic graphics engine framework developed can provide a reference for the development of other mobile graphics applications.


### Chinese Version

我们基于Vulkan搭建了一套移动端粒子系统引擎。

Vulkan的封装见：https://zhuanlan.zhihu.com/p/201311862

相关论文为：
吴优;基于Vulkan的跨平台粒子系统特效研发[D];浙江大学;2021年

摘要：

如果粒子特效系统的计算过于复杂,则会给移动设备的计算性能带来较大压力,从而影响用户的实时体验,并迅速消耗电量。另一方面,为了实现美观的粒子特效和特定的功能,一些计算量巨大的算法又很难被避免。要兼顾移动设备的计算性能、能耗和粒子系统的效果,是一个仍未解决的难题。本文研发了一个能够满足移动端日常特效交互需要的跨平台粒子特效系统。由于Vulkan支持跨平台,支持多线程渲染管线,性能更高,本文选择其为我们研发的图形API。常见的粒子特效往往需要在一帧之内计算上千粒子的运动状态,并支持诸如碰撞检测等较高复杂度的算法,这对设备的性能和功耗都是个不小的挑战。为了实现粒子与模型之间的高效交互,我们创新性地引入有向距离场(SDF,Signed Distance Field)来提升性能。设计人员可通过导入模型的SDF,可在常数复杂度下高效地实现模型表面对粒子的吸引、排斥和粒子沿表面运动。为了满足设计需要,系统支持碰撞避免、表面吸引、鸟群运动、涡旋力、风力等多种常见特效,还支持基于Boids模型的简化群组运动、噪声运动、粒子向指定位置移动等特效。而且,系统提供了基于关键帧的动画编辑播放功能。设计人员可在任意帧对粒子属性进行修改,然后由系统自动完成插值。本文研发的系统已经在万普拉斯科技有限公司旗下的Oppo手机上得到商业应用。而且,研发的基础图形引擎框架,可为更多的其它移动端图形应用开发提供借鉴。
