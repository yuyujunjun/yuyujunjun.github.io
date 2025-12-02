---
collection: "publications"
citation: "/assets/files/publications/2020DeepShape_ACMMM/citation.txt"
cover: "/assets/files/publications/2020DeepShape_ACMMM/teaser.jpg"
layout: "publication"
links:
  Paper: /assets/files/publications/2020DeepShape_ACMMM/main.pdf
  Video: https://www.youtube.com/embed/l43UVc1aWJ0?si=UusAhbMPEDEXRS5W
title: "Deep Shapely Portraits"
date: "2020-01-01"
pub_date: "2020"
permalink: "/publication/2020-Deep-Shapely-Portraits"
selected: "false"
authors:
- Qinjie Xiao
- Xiangjun Tang
- You Wu
- Leyang Jin
- Yong-Liang Yang
- Xiaogang Jin
pub: "Proceedings of the 28th ACM International Conference on Multimedia"
---
## Abstract:

We present deep shapely portraits, a novel method based on deep learning, to automatically reshape an input portrait to be better proportioned and more shapely while keeping personal facial characteristics. Different from existing methods that may suffer from irrational face artifacts when dealing with portraits with large pose variations or reshaping adjustments, we utilize dense 3D face information and constraints instead of sparse facial landmarks based on 3D morphable models, resulting in better reshaped faces lying in rational face space. To this end, we first estimate the best shapely degree for the input portrait using a convolutional neural network (CNN) trained on our newly developed ShapeFaceNet dataset. Then the best shapely degree is used as the control parameter to reshape the 3D face reconstructed from the input portrait image. After that, we render the reshaped 3D face back to 2D and generate a seamless portrait image using a fast image warping optimization. Our work can deal with pose and expression free (PE-Free) portrait images and generate plausible shapely faces without noticeable artifacts, which cannot be achieved by prior work. We validate the effectiveness, efficiency, and robustness of the proposed method by extensive experiments and user studies.



**bibtex:**
```
@inproceedings{10.1145/3394171.3413873,
author = {Xiao, Qinjie and Tang, Xiangjun and Wu, You and Jin, Leyang and Yang, Yong-Liang and Jin, Xiaogang},
title = {Deep Shapely Portraits},
year = {2020},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
booktitle = {Proceedings of the 28th ACM International Conference on Multimedia},
pages = {1800–1808},
numpages = {9},
location = {Seattle, WA, USA},
series = {MM '20}
}


```
