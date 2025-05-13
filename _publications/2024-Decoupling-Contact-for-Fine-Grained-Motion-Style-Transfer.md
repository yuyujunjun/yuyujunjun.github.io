---
collection: "publications"
citation: "/files/publications/2024Sigasia_decouple/citation.txt"
paperurl: "/files/publications/2024Sigasia_decouple/main.pdf"
teaser: "/files/publications/2024Sigasia_decouple/teaser.jpeg"
video: "http://www.cad.zju.edu.cn/home/jin/SigA20241/demo.mp4"
supplementary_materials: "/files/publications/2024Sigasia_decouple/appendix.pdf"
title: "Decoupling Contact for Fine-Grained Motion Style Transfer"
date: "2024-01-01"
year: "2024"
permalink: "/publication/2024-Decoupling-Contact-for-Fine-Grained-Motion-Style-Transfer"
first_author: "yes"
author: "Xiangjun Tang, [Linjun Wu](https://fivezerojun.github.io), [He Wang](https://drhewang.com/), [Yiqian Wu](https://onethousandwu.com), Bo Hu, Songnan Li, Xu Gong, Yuchen Liao, Qilong Kou, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "SIGGRAPH Asia 2024 Conference Papers"
---
## Abstract:

Motion style transfer changes the style of a motion while retaining its content and is useful in computer animations and games. Contact is an essential component of motion style transfer that should be controlled explicitly in order to express the style vividly while enhancing motion naturalness and quality. However, it is unknown how to decouple and control contact to achieve fine-grained control in motion style transfer.

In this paper, we present a novel style transfer method for fine-grained control over contacts while achieving both motion naturalness and spatial-temporal variations of style. Based on our empirical evidence, we propose controlling contact indirectly through the hip velocity, which can be further decomposed into the trajectory and contact timing, respectively. To this end, we propose a new model that explicitly models the correlations between motions and trajectory/contact timing/style, allowing us to decouple and control each separately. Our approach is built around a motion manifold, where hip controls can be easily integrated into a Transformer-based decoder. It is versatile in that it can generate motions directly as well as be used as post-processing for existing methods to improve quality and contact controllability. In addition, we propose a new metric that measures a correlation pattern of motions based on our empirical evidence, aligning well with human perception in terms of motion naturalness. Based on extensive evaluation, our method outperforms existing methods in terms of style expressivity and motion quality.

**bibtex:**
```
@inproceedings{10.1145/3680528.3687609,
author = {Tang, Xiangjun and Wu, Linjun and Wang, He and Wu, Yiqian and Hu, Bo and Li, Songnan and Gong, Xu and Liao, Yuchen and Kou, Qilong and Jin, Xiaogang},
title = {Decoupling Contact for Fine-Grained Motion Style Transfer},
year = {2024},
doi = {10.1145/3680528.3687609},
booktitle = {SIGGRAPH Asia 2024 Conference Papers},
articleno = {54},
numpages = {11},
keywords = {Style transfer, Motion quality, Editing.},
location = {Tokyo, Japan},
series = {SA '24}
}
```
