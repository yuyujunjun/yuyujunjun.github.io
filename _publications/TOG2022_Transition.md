---
title: Real-time Controllable Motion Transition for Characters
collection: publications
date: 2022-08-08
oriurl: https://dl.acm.org/doi/abs/10.1145/3528223.3530090
venue: "ACM Transactions on Graphics (Proc. Siggraph 2022)" 
pdf: 'https://yuyujunjun.github.io/files/2022_TOG_Motion_Transition.pdf'
video: http://www.cad.zju.edu.cn/home/jin/SigMotion2022/demo.mp4
author: '**Xiangjun Tang**, [He Wang](http://drhewang.com/), Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/).'
citation: 'https://yuyujunjun.github.io/files/citations/2022_TOG_transition.txt'
---



**Xiangjun Tang**, He Wang, Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, and Xiaogang Jin.

![teaser](https://yuyujunjun.github.io/images/2022TOG/teaser.png)

## Abstract:

Real-time in-between motion generation is universally required in games and highly desirable in existing animation pipelines. Its core challenge lies in the need to satisfy three critical conditions simultaneously: \textit{quality}, \textit{controllability} and \textit{speed}, which renders any methods that need offline computation (or post-processing) or cannot incorporate (often unpredictable) user control undesirable. To this end, we propose a new real-time transition method to address the aforementioned challenges. Our approach consists of two key components: motion manifold and conditional transitioning. The former learns the important low-level motion features and their dynamics; while the latter synthesizes transitions conditioned on a target frame and the desired transition duration. We first learn a motion manifold that explicitly models the intrinsic transition stochasticity in human motions via a multi-modal mapping mechanism. Then, during generation, we design a transition model which is essentially a sampling strategy to sample from the learned manifold, based on the target frame and the aimed transition duration. We validate our method on different datasets in tasks where no post-processing or offline computation is allowed. Through exhaustive evaluation and comparison, we show that our method is able to generate \textit{high-quality} motions measured under multiple metrics. Our method is also \textit{robust} under various target frames (with extreme cases). 

**bibtex:**

```
@article{10.1145/3528223.3530090,
author = {Tang, Xiangjun and Wang, He and Hu, Bo and Gong, Xu and Yi, Ruifan and Kou, Qilong and Jin, Xiaogang},
title = {Real-Time Controllable Motion Transition for Characters},
year = {2022},
issue_date = {July 2022},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {41},
number = {4},
issn = {0730-0301},
journal = {ACM Trans. Graph.},
month = {jul},
articleno = {137},
numpages = {10},
}

```