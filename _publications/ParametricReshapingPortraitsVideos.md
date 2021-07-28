---
title: Parametric Reshaping of Portraits in Videos
collection: publications
date: 2021-10-20
permalink: /publication/VideoPortraitReshaping
venue: "ACM International Conference on Multimedia" 
oriurl: https://dl.acm.org/doi/abs/10.1145/3474085.3475334
citation: Xiangjun Tang, Wenxin Sun, Yong-Liang Yang, and Xiaogang Jin. 2021. Parametric Reshaping of Portraits in Videos. In Proceedings of the 29th ACM International Conference on Multimedia (MM ’21), October 20–24, 2021, Virtual Event, China. ACM, New York, NY, USA, 9 pages.
---


 **Xiangjun Tang**, Wenxin Sun, Yong-Liang Yang, and Xiaogang Jin.



## Abstract:

Sharing short personalized videos to various social media networks has become quite popular in recent years. This raises the need for digital retouching of portraits in videos. However, applying portrait image editing directly on portrait video frames cannot generate smooth and stable video sequences. To this end, we present a robust and easy-to-use parametric method to reshape the portrait in a video to produce smooth retouched results. Given an input portrait video, our method consists of two main stages: stabilized face reconstruction, and continuous  video reshaping. In the first stage, we start by estimating face rigid pose transformations across video frames. Then we jointly optimize multiple frames to reconstruct an accurate face identity, followed by recovering face expressions over the entire video. In the second stage, we first reshape the reconstructed 3D face using a parametric reshaping model reflecting the weight change of the face, and then utilize the reshaped 3D face to guide the warping of video frames. We develop a novel signed distance function based dense mapping method for the warping between face contours before and after reshaping, resulting in stable warped video frames with minimum distortions. In addition, we use the 3D structure of the face to correct the dense mapping to achieve temporal consistency. We generate the final result by minimizing the background distortion through optimizing a content-aware warping mesh. Extensive experiments show that our method is able to create visually pleasing results by adjusting a simple reshaping parameter, which facilitates portrait video editing for social media and visual effects.