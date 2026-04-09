---
collection: "publications"
citation: "/assets/files/publications/2025GenHuman/citation.txt"
highlight: "Oral (1.13%)"
cover: "/assets/files/publications/2025GenHuman/teaser.png"
layout: "publication"
links:
  Arxiv: https://arxiv.org/abs/2503.01448
  Video: /assets/files/publications/2025GenHuman/demo.mp4
title: "Generative Human Geometry Distribution"
date: "2026-01-01"
pub_date: "2026"
permalink: "/publication/2026-Generative-Human-Geometry-Distribution"
selected: "true"
authors:
- Xiangjun Tang
- Biao Zhang
- Peter Wonka
pub: "International Conference on Learning Representations"
pub_ab: "ICLR Oral (1.13%)"
---
## Abstract:
Realistic human geometry generation is an important yet challenging task, requiring both the preservation of fine clothing details and the accurate modeling of clothing-body interactions. 
To tackle this challenge, we build upon Geometry distributions—a recently proposed representation that can model a single human geometry with high fidelity using a flow matching model. However, extending a single-geometry distribution to a dataset is non-trivial and inefficient for large-scale learning. To address this, we propose a new geometry distribution model by two key techniques: (1) encoding distributions as 2D feature maps rather than network parameters, and (2) using SMPL models as the domain instead of Gaussian and refining the associated flow velocity field.
We then design a generative framework adopting a two-staged training paradigm analogous to state-of-the-art image and 3D generative models.
In the first stage, we compress geometry distributions into a latent space using a diffusion flow model; the second stage trains another flow model on this latent space. 
We validate our approach on two key tasks: pose-conditioned random avatar generation and avatar-consistent novel pose synthesis.
Experimental results demonstrate that our method outperforms existing state-of-the-art methods, achieving a $57\%$ improvement in geometry quality. 

**bibtex:**
```
@inproceedings{tang2025generative,
  title={Generative Human Geometry Distribution},
  author={Tang, Xiangjun and Zhang, Biao and Wonka, Peter},
  booktitle={International Conference on Learning Representations},
  year={2026},
  note={Oral}
}

```
