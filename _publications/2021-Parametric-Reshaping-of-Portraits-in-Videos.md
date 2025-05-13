---
collection: "publications"
citation: "/files/publications/2021ReshapingVideo/citation.txt"
paperurl: "/files/publications/2021ReshapingVideo/main.pdf"
teaser: "/files/publications/2021ReshapingVideo/teaser.jpeg"
video: "http://www.cad.zju.edu.cn/home/jin/ACMMM2021/demo.mp4"
title: "Parametric Reshaping of Portraits in Videos"
date: "2021-01-01"
year: "2021"
permalink: "/publication/2021-Parametric-Reshaping-of-Portraits-in-Videos"
first_author: "yes"
author: "Xiangjun Tang, WenXin Sun, [Yong-Liang Yang](https://www.yongliangyang.net/), [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "Proceedings of the 29th ACM International Conference on Multimedia"
---
## Abstract:

Sharing short personalized videos to various social media networks has become quite popular in recent years. This raises the need for digital retouching of portraits in videos. However, applying portrait image editing directly on portrait video frames cannot generate smooth and stable video sequences. To this end, we present a robust and easy-to-use parametric method to reshape the portrait in a video to produce smooth retouched results. Given an input portrait video, our method consists of two main stages: stabilized face reconstruction, and continuous  video reshaping. In the first stage, we start by estimating face rigid pose transformations across video frames. Then we jointly optimize multiple frames to reconstruct an accurate face identity, followed by recovering face expressions over the entire video. In the second stage, we first reshape the reconstructed 3D face using a parametric reshaping model reflecting the weight change of the face, and then utilize the reshaped 3D face to guide the warping of video frames. We develop a novel signed distance function based dense mapping method for the warping between face contours before and after reshaping, resulting in stable warped video frames with minimum distortions. In addition, we use the 3D structure of the face to correct the dense mapping to achieve temporal consistency. We generate the final result by minimizing the background distortion through optimizing a content-aware warping mesh. Extensive experiments show that our method is able to create visually pleasing results by adjusting a simple reshaping parameter, which facilitates portrait video editing for social media and visual effects.



**bibtex:**
```
@inproceedings{10.1145/3474085.3475334,
author = {Tang, Xiangjun and Sun, WenXin and Yang, Yong-Liang and Jin, Xiaogang},
title = {Parametric Reshaping of Portraits in Videos},
year = {2021},
isbn = {9781450386517},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
booktitle = {Proceedings of the 29th ACM International Conference on Multimedia},
pages = {4689–4697},
numpages = {9},
location = {Virtual Event, China},
series = {MM '21}
}
```
