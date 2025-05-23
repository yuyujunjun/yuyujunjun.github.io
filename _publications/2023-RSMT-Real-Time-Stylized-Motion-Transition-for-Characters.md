---
collection: "publications"
citation: "/files/publications/2023Sig_RSMT/citation.txt"
paperurl: "/files/publications/2023Sig_RSMT/main.pdf"
video: "http://www.cad.zju.edu.cn/home/jin/sig20232/demo.mp4"
code: "https://github.com/yuyujunjun/RSMT-Realtime-Stylized-Motion-Transition"
supplementary_materials: "/files/publications/2023Sig_RSMT/appendix.pdf"
teaser: "/files/publications/2023Sig_RSMT/teaser.png"
title: "RSMT: Real-Time Stylized Motion Transition for Characters"
date: "2023-01-01"
year: "2023"
permalink: "/publication/2023-RSMT-Real-Time-Stylized-Motion-Transition-for-Characters"
first_author: "yes"
author: "Xiangjun Tang, [Linjun Wu](https://fivezerojun.github.io), [He Wang](https://drhewang.com/), Bo Hu, Xu Gong, Yuchen Liao, Songnan Li, Qilong Kou, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "ACM SIGGRAPH 2023 Conference Proceedings"
---
## Abstract:
Styled online in-between motion generation has important application scenarios in computer animation and games. Its core challenge lies in the need to satisfy four critical requirements simultaneously: generation speed,  motion quality, style diversity, and synthesis controllability. While the first two challenges demand a delicate balance between simple fast models and learning capacity for generation quality, the latter two are rarely investigated together in existing methods, which largely focus on either control without style or uncontrolled stylized motions. To this end, we propose a Real-time Stylized Motion Transition method (RSMT) to achieve all aforementioned goals. Our method consists of two critical, independent components: a general motion manifold model and a style motion sampler. The former acts as a high-quality motion source and the latter synthesizes styled motions on the fly under control signals. Since both components can be trained separately on different datasets, our method provides great flexibility, requires less data, and generalizes well when no/few samples are available for unseen styles. Through exhaustive evaluation, our method proves to be fast, high-quality, versatile, and controllable. The code and data are available at <a href="https://github.com/yuyujunjun/RSMT-Realtime-Stylized-Motion-Transition"> Code </a>.

**bibtex:**
```
@inproceedings{10.1145/3588432.3591514,
author = {Tang, Xiangjun and Wu, Linjun and Wang, He and Hu, Bo and Gong, Xu and Liao, Yuchen and Li, Songnan and Kou, Qilong and Jin, Xiaogang},
title = {RSMT: Real-Time Stylized Motion Transition for Characters},
year = {2023},
publisher = {Association for Computing Machinery},
url = {https://doi.org/10.1145/3588432.3591514},
doi = {10.1145/3588432.3591514},
booktitle = {ACM SIGGRAPH 2023 Conference Proceedings},
articleno = {38},
numpages = {10},
location = {Los Angeles, CA, USA},
series = {SIGGRAPH '23}
}
```
