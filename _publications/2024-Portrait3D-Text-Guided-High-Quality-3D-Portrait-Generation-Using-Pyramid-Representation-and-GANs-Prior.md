---
collection: "publications"
citation: "/assets/files/publications/2024_portrait3D_tog/citation.txt"
cover: "/assets/files/publications/2024_portrait3D_tog/teaser.png"
layout: "publication"
links:
  Arxiv: https://arxiv.org/abs/2404.10394
  Project: https://onethousandwu.com/portrait3d.github.io/
  Video: https://www.youtube.com/embed/z7xWiD1p1_4?si=AZ-pFojUk-6u1pze
  Code: https://github.com/oneThousand1000/Portrait3D
  Supplemental: https://drive.google.com/file/d/1LasG-urCA7rEoITHofBwEk0CloXM0DwX/view?pli=1
title: "Portrait3D: Text-Guided High-Quality 3D Portrait Generation Using Pyramid Representation and GANs Prior"
date: "2024-07-01"
pub_date: "2024"
permalink: "/publication/2024-Portrait3D-Text-Guided-High-Quality-3D-Portrait-Generation-Using-Pyramid-Representation-and-GANs-Prior"
selected: "false"
authors:
- Yiqian Wu
- Hao Xu
- Xiangjun Tang
- Xien Chen
- Siyu Tang
- Zhebin Zhang
- Chen Li
- Xiaogang Jin
pub: "ACM Transactions on Graphics (TOG)"
pub_ab: "TOG"
---
## Abstract:
Existing neural rendering-based text-to-3D-portrait generation methods typically make use of human geometry prior and diffusion models to obtain guidance. However, relying solely on geometry information introduces issues such as the Janus problem, over-saturation, and over-smoothing.
We present Portrait3D, a novel neural rendering-based framework with a novel joint geometry-appearance prior to achieve text-to-3D-portrait generation that overcomes the aforementioned issues. To accomplish this, we train a 3D portrait generator, 3DPortraitGAN-Pyramid, as a robust prior. This generator is capable of producing 360° canonical 3D portraits, serving as a starting point for the subsequent diffusion-based generation process. To mitigate the "grid-like" artifact caused by the high-frequency information in the feature-map-based 3D representation commonly used by most 3D-aware GANs, we integrate a novel pyramid tri-grid 3D representation into 3DPortraitGAN-Pyramid. To generate 3D portraits from text, we first project a randomly generated image aligned with the given prompt into the pre-trained 3DPortraitGAN-Pyramid's latent space. The resulting latent code is then used to synthesize a pyramid tri-grid. Beginning with the obtained pyramid tri-grid, we use score distillation sampling to distill the diffusion model's knowledge into the pyramid tri-grid. Following that, we utilize the diffusion model to refine the rendered images of the 3D portrait and then use these refined images as training data to further optimize the pyramid tri-grid, effectively eliminating issues with unrealistic color and unnatural artifacts.
Our experimental results show that Portrait3D can produce realistic, high-quality, and canonical 3D portraits that align with the prompt.


**bibtex:**
```
@article{10.1145/3658162,
author = {Wu, Yiqian and Xu, Hao and Tang, Xiangjun and Chen, Xien and Tang, Siyu and Zhang, Zhebin and Li, Chen and Jin, Xiaogang},
title = {Portrait3D: Text-Guided High-Quality 3D Portrait Generation Using Pyramid Representation and GANs Prior},
year = {2024},
issue_date = {July 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {43},
number = {4},
issn = {0730-0301},
url = {https://doi.org/10.1145/3658162},
doi = {10.1145/3658162},
journal = {ACM Transactions on Graphics (TOG)},
month = {jul},
articleno = {45},
numpages = {12},
keywords = {3D portrait generation, 3D-aware GANs, diffusion models}
}
```
