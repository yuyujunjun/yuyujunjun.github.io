---
title: Real-time Controllable Motion Transition for Characters
collection: publications
date: 2022-08-08
oriurl: https://dl.acm.org/doi/abs/10.1145/3528223.3530090
venue: "ACM Transactions on Graphics (Proc. Siggraph 2022), 2022, 41(4): Article No.: 137." 
citation: Xiangjun Tang, He Wang, Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, and Xiaogang Jin*. 2022. Real-time Controllable Motion Transition for Characters. ACM Trans. Graph. 41, 4, Article 137 (July 2022), 10 pages. https://doi.org/10.1145/3528223.3530090
---



**Xiangjun Tang**, He Wang, Bo Hu, Xu Gong, Ruifan Yi, Qilong Kou, and Xiaogang Jin.



## Abstract:

Real-time in-between motion generation is universally required in games and highly desirable in existing animation pipelines. Its core challenge lies in the need to satisfy three critical conditions simultaneously: \textit{quality}, \textit{controllability} and \textit{speed}, which renders any methods that need offline computation (or post-processing) or cannot incorporate (often unpredictable) user control undesirable. To this end, we propose a new real-time transition method to address the aforementioned challenges. Our approach consists of two key components: motion manifold and conditional transitioning. The former learns the important low-level motion features and their dynamics; while the latter synthesizes transitions conditioned on a target frame and the desired transition duration. We first learn a motion manifold that explicitly models the intrinsic transition stochasticity in human motions via a multi-modal mapping mechanism. Then, during generation, we design a transition model which is essentially a sampling strategy to sample from the learned manifold, based on the target frame and the aimed transition duration. We validate our method on different datasets in tasks where no post-processing or offline computation is allowed. Through exhaustive evaluation and comparison, we show that our method is able to generate \textit{high-quality} motions measured under multiple metrics. Our method is also \textit{robust} under various target frames (with extreme cases). 