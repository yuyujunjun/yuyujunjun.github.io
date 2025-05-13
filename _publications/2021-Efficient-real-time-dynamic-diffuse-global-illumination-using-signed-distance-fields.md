---
collection: "publications"
citation: "/files/publications/2021SDFGI/citation.txt"
paperurl: "/files/publications/2021SDFGI/main.pdf"
teaser: "/files/publications/2021SDFGI/teaser.jpeg"
video: "http://www.cad.zju.edu.cn/home/jin/tvc2021/demo.mp4"
title: "Efficient real-time dynamic diffuse global illumination using signed distance fields"
date: "2021-01-01"
year: "2021"
permalink: "/publication/2021-Efficient-real-time-dynamic-diffuse-global-illumination-using-signed-distance-fields"
first_author: "no"
author: "Jinkai Hu, Milo Yip, Guillermo Alonso, Shihao Gu, Xiangjun Tang, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "The Visual Computer"
---
## Abstract:
We present SDFDDGI, a novel approach to compute dynamic diffuse global illumination in real time using signed distance fields (SDF). For an input scene, we first construct its compact representation using SDF. Different from traditional SDF which are stored by discrete voxels, our approach approximates the scene by a set of simple primitive shapes, which facilitates real-time computation and dynamic changes. Then, we reconstruct the irradiance function in the space domain by discrete samples (referred to as probes), which are positioned heuristically for real-time performance. The probe irradiance can be updated and interpolated effectively supported by our compact SDF representation. Subsequently, a screen-space refinement method is developed to enhance rendering details and visual quality. We validate our approach by comparing the performance and quality of our method to other state-of-the-art real-time global illumination methods. Our approach is able to calculate real-time diffuse global illumination for both dynamic geometry and dynamic lighting efficiently without any precomputation, while also supporting multi-bounced light. It is also hardware free and can manage both large open scenes and indoor high-detailed scenes.




**bibtex:**
```
@article{hu2021efficient,
  title={Efficient real-time dynamic diffuse global illumination using signed distance fields},
  author={Hu, Jinkai and Yip, Milo K and Alonso, Guillermo Elias and Gu, Shihao and Tang, Xiangjun and Jin, Xiaogang},
  journal={The Visual Computer},
  volume={37},
  pages={2539--2551},
  year={2021},
  publisher={Springer}
}
```
