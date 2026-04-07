---
collection: "publications"
citation: "/assets/files/publications/2026HumanAnimate/citation.txt"
cover: "/assets/files/publications/2026HumanAnimate/teaser.png"
layout: "publication"
links:
  Arxiv: https://arxiv.org/abs/2512.07459v1
  Video: /assets/files/publications/2026HumanAnimate/demo.mp4
title: "Human Geometry Distribution for 3D Animation Generation"
date: "2026-01-01"
pub_date: "2026"
permalink: "/publication/2026-Human-Geometry-Distribution-for-3D-Animation-Generation"
selected: "true"
authors:
- Xiangjun Tang
- Biao Zhang
- Peter Wonka
pub: "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition"
pub_ab: "CVPR"
---
## Abstract:
Generating realistic human geometry animations remains a challenging task, as it requires modeling natural clothing dynamics with fine-grained geometric details under limited data.
To address these challenges, we propose two novel designs. First, we propose a compact distribution-based latent representation that enables efficient and high-quality geometry generation. We improve upon previous work by establishing a more uniform mapping between SMPL and avatar geometries. Second, we introduce a generative animation model that fully exploits the diversity of limited motion data. We focus on short-term transitions while maintaining long-term consistency through an identity-conditioned design. These two designs formulate our method as a two-stage framework: the first stage learns a latent space, while the second learns to generate animations within this latent space.
We conducted experiments on both our latent space and animation model. We demonstrate that our latent space produces high-fidelity human geometry surpassing previous methods ($90\%$ lower Chamfer Dist.). The animation model synthesizes diverse animations with detailed and natural dynamics ($2.2 \times$ higher user study score), achieving the best results across all evaluation metrics.

**bibtex:**
```
@inproceedings{tang2026geo,
  title={Human Geometry Distribution for 3D Animation Generation},
  author={Tang, Xiangjun and Zhang, Biao and Wonka, Peter},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2026}
}

```
