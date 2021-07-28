---
title: "Parametric Reshaping of Portraits in Videos"
collection: publications
date: 2021-10-20
venue: "ACM International Conference on Multimedia" 
oriurl: https://dl.acm.org/doi/abs/10.1145/3474085.3475334
citation: Xiangjun Tang, Wenxin Sun, Yong-Liang Yang, and Xiaogang Jin. 2021.
Parametric Reshaping of Portraits in Videos. In Proceedings of the 29th ACM International Conference on Multimedia (MM ’21), October 20–24, 2021, Virtual Event, China. ACM, New York, NY, USA, 9 pages.

---
**Xiangjun Tang**, Wenxin Sun, Yong-Liang Yang, and Xiaogang Jin.



## Abstract:

We present deep shapely portraits, a novel method based on deep learning, to automatically reshape an input portrait to be better proportioned and more shapely while keeping personal facial characteristics. Different from existing methods that may suffer from irrational face artifacts when dealing with portraits with large pose variations or reshaping adjustments, we utilize dense 3D face information and constraints instead of sparse facial landmarks based on 3D morphable models, resulting in better reshaped faces lying in rational face space. To this end, we first estimate the best shapely degree for the input portrait using a convolutional neural network (CNN) trained on our newly developed ShapeFaceNet dataset. Then the best shapely degree is used as the control parameter to reshape the 3D face reconstructed from the input portrait image. After that, we render the reshaped 3D face back to 2D and generate a seamless portrait image using a fast image warping optimization. Our work can deal with pose and expression free (PE-Free) portrait images and generate plausible shapely faces without noticeable artifacts, which cannot be achieved by prior work. We validate the effectiveness, efficiency, and robustness of the proposed method by extensive experiments and user studies.