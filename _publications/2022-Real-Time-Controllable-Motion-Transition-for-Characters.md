---
collection: "publications"
citation: "/files/publications/2022TOG/citation.txt"
paperurl: "/files/publications/2022TOG/main.pdf"
video: "http://www.cad.zju.edu.cn/home/jin/SigMotion2022/demo.mp4"
teaser: "/files/publications/2022TOG/teaser.png"
title: "Real-time controllable motion transition for characters"
date: "2022-01-01"
year: "2022"
permalink: "/publication/2022-Real-time-controllable-motion-transition-for-characters"
first_author: "yes"
author: "Xiangjun Tang, [He Wang](https://drhewang.com/), Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "ACM Transactions on Graphics (TOG)"
---
## Abstract:

Real-time in-between motion generation is universally required in games and highly desirable in existing animation pipelines. Its core challenge lies in the need to satisfy three critical conditions simultaneously: *quality*, *controllability* and *speed*, which renders any methods that need offline computation (or post-processing) or cannot incorporate (often unpredictable) user control undesirable. To this end, we propose a new real-time transition method to address the aforementioned challenges. Our approach consists of two key components: motion manifold and conditional transitioning. The former learns the important low-level motion features and their dynamics; while the latter synthesizes transitions conditioned on a target frame and the desired transition duration. We first learn a motion manifold that explicitly models the intrinsic transition stochasticity in human motions via a multi-modal mapping mechanism. Then, during generation, we design a transition model which is essentially a sampling strategy to sample from the learned manifold, based on the target frame and the aimed transition duration. We validate our method on different datasets in tasks where no post-processing or offline computation is allowed. Through exhaustive evaluation and comparison, we show that our method is able to generate *high-quality* motions measured under multiple metrics. Our method is also *robust* under various target frames (with extreme cases). 

**bibtex:**
```
@article{tang2022real,
  title={Real-time controllable motion transition for characters},
  author={Tang, Xiangjun and Wang, He and Hu, Bo and Gong, Xu and Yi, Ruifan and Kou, Qilong and Jin, Xiaogang},
  journal={ACM Transactions on Graphics (TOG)},
  volume={41},
  number={4},
  pages={1--10},
  year={2022},
  publisher={ACM New York, NY, USA}
}
```
