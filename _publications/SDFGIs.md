---
title: "Efficient real-time dynamic diffuse global illumination using signed distance fields"
collection: publications
permalink: /publication/Efficient-real-time-dynamic-diffuse-global-illumination-using-signed-distance-fields
date: 2021-06-02
venue: 'The Visual Computing'
oriurl: https://doi.org/10.1007/s00371-021-02197-0
paperurl: 'https://yuyujunjun.github.io/files/sdfGI.pdf'
citation: Hu, J., Yip, M.K., Alonso, G.E. et al. Efficient real-time dynamic diffuse global illumination using signed distance fields. Vis Comput (2021). 
---
Jinkai Hu, Milo K. Yip, Guillermo Elias Alonso, Shihao Gu, **Xiangjun Tang** & Xiaogang Jin



## Abstract:

We present SDFDDGI, a novel approach to compute dynamic diffuse global illumination in real time using signed distance fields (SDF). For an input scene, we first construct its compact representation using SDF. Different from traditional SDF which are stored by discrete voxels, our approach approximates the scene by a set of simple primitive shapes, which facilitates real-time computation and dynamic changes. Then, we reconstruct the irradiance function in the space domain by discrete samples (referred to as probes), which are positioned heuristically for real-time performance. The probe irradiance can be updated and interpolated effectively supported by our compact SDF representation. Subsequently, a screen-space refinement method is developed to enhance rendering details and visual quality. We validate our approach by comparing the performance and quality of our method to other state-of-the-art real-time global illumination methods. Our approach is able to calculate real-time diffuse global illumination for both dynamic geometry and dynamic lighting efficiently without any precomputation, while also supporting multi-bounced light. It is also hardware free and can manage both large open scenes and indoor high-detailed scenes.