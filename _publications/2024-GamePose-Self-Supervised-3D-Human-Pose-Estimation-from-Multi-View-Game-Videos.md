---
collection: "publications"
citation: "/assets/files/publications/2024Gamepose/citation.txt"
cover: "/assets/files/publications/2024Gamepose/teaser.jpg"
layout: "publication"
links:
  Paper: https://diglib.eg.org/items/ad02ce02-c87d-4bcf-840b-fbd2d0a13c2f
title: "GamePose: Self-Supervised 3D Human Pose Estimation from Multi-View Game Videos"
date: "2024-01-01"
pub_date: "2024"
permalink: "/publication/2024-GamePose-Self-Supervised-3D-Human-Pose-Estimation-from-Multi-View-Game-Videos"
selected: "false"
authors:
- Yang Zhou
- Tianze Guo
- Hao Xu
- Xilei Wei
- Lang Xu
- Xiangjun Tang
- Sipeng Yang
- Qilong Kou
- Xiaogang Jin
pub: "Pacific Graphics Conference Papers and Posters"
---
## Abstract:

Recovering 3D character animations from published games is crucial when original animation assets are lost. One solution for recovering such animation assets is to use 3D human pose estimation with single or multiple views. Our insight is to preserve the ease of use of single-view estimation while enhancing its accuracy by leveraging information from multi-view videos. It is a difficult task that requires explicitly modelling the correlation of multi-view input to achieve superior accuracy and converting the multi-view correlation model to a single-view model without impacting the accuracy, which both are unresolved. To this end, we propose a novel self-supervised 3D pose estimation framework that models the correlation of multi-view input during training and can predict highly accurate estimation for single-view input. Our framework consists of two main components: the Single-View Module (SM) and the Cross-View Module (CM). The SM predicts approximate 3D poses and extracts features from a single viewpoint, while the CM enhances the learning process by modelling correlations across multiple viewpoints. This design facilitates effective self-distillation, improving the accuracy of single-view estimations. As a result, our method supports highly accurate inference with both multi-view data and single-view data. We validate our method on 3D human pose estimation benchmarks and create a new dataset using Mixamo assets to demonstrate its applicability in gaming scenarios. Extensive experiments show that our approach outperforms state-of-the-art methods in self-supervised learning scenarios.

**bibtex:**
```
@inproceedings{10.2312:pg.20241316,
booktitle = {Pacific Graphics Conference Papers and Posters},
title = {{GamePose: Self-Supervised 3D Human Pose Estimation from Multi-View Game Videos}},
author = {Zhou, Yang and Guo, Tianze and Xu, Hao and Wei, Xilei and Xu, Lang and Tang, Xiangjun and Yang, Sipeng and Kou, Qilong and Jin, Xiaogang},
year = {2024},
publisher = {The Eurographics Association},
ISBN = {978-3-03868-250-9},
DOI = {10.2312/pg.20241316}
}
```
