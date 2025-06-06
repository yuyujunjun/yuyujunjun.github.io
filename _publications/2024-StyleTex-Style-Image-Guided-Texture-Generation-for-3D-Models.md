---
collection: "publications"
citation: "/files/publications/2024StyTex/citation.txt"
video: "http://www.cad.zju.edu.cn/home/jin/SigA20241/demo.mp4"
paperurl: "https://arxiv.org/abs/2411.00399"
supplementary_materials: "http://www.cad.zju.edu.cn/home/jin/SigA20242/supplemental_material.pdf"
teaser: "/files/publications/2024StyTex/teaser.jpg"
title: "StyleTex: Style Image-Guided Texture Generation for 3D Models"
date: "2024-01-01"
year: "2024"
permalink: "/publication/2024-StyleTex-Style-Image-Guided-Texture-Generation-for-3D-Models"
first_author: "no"
author: "Zhiyu Xie, Yuqing Zhang, Xiangjun Tang, [Yiqian Wu](https://onethousandwu.com), Dehan Chen, Gongsheng Li, [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin/)."
venue: "ACM Transactions on Graphics (TOG)"
---
## Abstract
Style-guided texture generation aims to generate a texture that is harmonious with both the style of the reference image and the geometry of the input mesh, given a reference style image and a 3D mesh with its text description. Although diffusion-based 3D texture generation methods, such as distillation sampling, have numerous promising applications in stylized games and films, it requires addressing two challenges: 1) decouple style and content completely from the reference image for 3D models, and 2) align the generated texture with the color tone, style of the reference image, and the given text prompt. To this end, we introduce StyleTex, an innovative diffusion model-based framework for creating stylized textures for 3D models. Our key insight is to decouple style information from the reference image while disregarding content in diffusion-based distillation sampling. Specifically, given a reference image, we first decompose its style feature from the image CLIP embedding by subtracting the embedding’s orthogonal projection in the direction of the content feature, which is represented by a text CLIP embedding. Our novel approach to disentangling the reference image’s style and content information allows us to generate distinct style and content features. We then inject the style feature into the cross-attention mechanism to incorporate it into the generation process, while utilizing the content feature as a negative prompt to further dissociate content information. Finally, we incorporate these strategies into StyleTex to obtain stylized textures. We utilize Interval Score Matching to address over-smoothness and over-saturation, in combination with a geometry-aware ControlNet that ensures consistent geometry throughout the generative process. The resulting textures generated by StyleTex retain the style of the reference image, while also aligning with the text prompts and intrinsic details of the given 3D mesh. Quantitative and qualitative experiments show that our method outperforms existing baseline methods by a significant margin.



**bibtex:**
```
@article{xie2024styletex,
  title={StyleTex: Style Image-Guided Texture Generation for 3D Models},
  author={Xie, Zhiyu and Zhang, Yuqing and Tang, Xiangjun and Wu, Yiqian and Chen, Dehan and Li, Gongsheng and Jin, Xiaogang},
  journal={ACM Transactions on Graphics (TOG)},
  volume={43},
  number={6},
  pages={1--14},
  year={2024},
  publisher={ACM New York, NY, USA}
}
```
