---
collection: "publications"
citation: "/files/publications/2024FusionDeformer/citation.txt"
paperurl: "/files/publications/2024FusionDeformer/main.pdf"
teaser: "/files/publications/2024FusionDeformer/teaser.png"
title: "FusionDeformer: text-guided mesh deformation using diffusion models"
date: "2024-01-01"
year: "2024"
permalink: "/publication/2024-FusionDeformer-text-guided-mesh-deformation-using-diffusion-models"
first_author: "no"
author: "[Hao Xu](https://xh38.github.io), [Yiqian Wu](https://onethousandwu.com), Xiangjun Tang, Jing Zhang, Yang Zhang, Zhebin Zhang, Chen Li, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "The Visual Computer"
---
## Abstract:
Mesh deformation has a wide range of applications, including character creation, geometry modeling, deforming animation, and morphing. 
Recently, mesh deformation methods based on CLIP models demonstrated the ability to perform automatic text-guided mesh deformation. 
However, using 2D guidance to deform a 3D mesh attempts to solve an ill-posed problem and leads to distortion and unsmoothness, which cannot be eliminated by Clip-based methods because they focus on semantic-aware features and cannot identify these artifacts. 
To this end, we propose FusionDeformer, a novel automatic text-guided mesh deformation method that leverages diffusion models. The deformation is achieved by Score Distillation Sampling (SDS), which minimizes the KL-divergence between the distribution of rendered deformed mesh and the text-conditioned distribution. To alleviate the intrinsic ill-posed problem, we incorporate two approaches into our framework. The first approach involves combining multiple orthogonal views into a single image, providing robust deformation while avoiding the need for additional memory. The second approach incorporates a new regularization to address the unsmooth artifacts. 

Our experimental results show that the proposed method can generate high-quality, smoothly deformed meshes that align precisely with the input text description while preserving the topological relationships. 
Additionally, our method offers a text2morphing approach to animation design, enabling common users to produce special effects animation. 

**bibtex:**
```
@article{xu2024fusiondeformer,
  title={FusionDeformer: text-guided mesh deformation using diffusion models},
  author={Xu, Hao and Wu, Yiqian and Tang, Xiangjun and Zhang, Jing and Zhang, Yang and Zhang, Zhebin and Li, Chen and Jin, Xiaogang},
  journal={The Visual Computer},
  volume={40},
  number={7},
  pages={4701--4712},
  year={2024},
  publisher={Springer}
}
```
