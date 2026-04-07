---
collection: "publications"
citation: "/assets/files/publications/2025RLACD/citation.txt"
cover: "/assets/files/publications/2025RLACD/teaser.png"
layout: "publication"
links:
  Paper: /assets/files/publications/2025RLACD/main.pdf
  URL: https://dl.acm.org/doi/abs/10.1145/3763270
title: "RL-ACD: Reinforcement Learning-based Approximate Convex Decomposition"
date: "2025-01-01"
pub_date: "2025"
permalink: "/publication/2025-RL-ACD-Reinforcement-Learning-based-Approximate-Convex-Decomposition"
selected: "false"
authors:
- Yuzhe Luo
- Zherong Pan
- Kui Wu
- Xingyi Du
- Yun Zeng
- Xiangjun Tang
- Yiqian Wu
- Xiaogang Jin
- Xifeng Gao
pub: "ACM Transactions on Graphics (TOG)"
pub_ab: "TOG"
---
## Abstract
Approximate Convex Decomposition (ACD) aims to approximate complex 3D shapes with convex components, which is widely applied to create compact collision representations for real-time applications, including VR/AR, interactive games, and robotic simulations. Efficiency and optimality are critical for ACD algorithms in approximating large-scale, complex 3D shapes, enabling high-quality decompositions with minimal components. Unfortunately, existing methods either employ sub-optimal greedy strategies or rely on computationally intensive multi-step searches. In this work, we propose RL-ACD, a data-driven, reinforcement learning-based approach for efficient and near-optimal convex shape decomposition. We formulate ACD as a Markov Decision Process (MDP), where cutting planes are iteratively applied based on the current stage's mesh fragments rather than the entire fine-grained mesh, leading to a novel, efficient geometric encoding. To train near-optimal policies for ACD, we propose a novel dual-state Bellman loss and analyze its convergence using a Q-learning algorithm. Comprehensive evaluations across diverse datasets validate the efficiency and accuracy of RL-ACD for convex decomposition tasks. Our method outperforms the multi-step tree search by 15× in terms of computational speed, while reducing the number of resulting components by 16% compared to the current state-of-the-art greedy algorithms, significantly narrowing the sub-optimality gap and enhancing downstream task performance.

**bibtex:**
```
@article{luo2025rl,
  title={RL-ACD: Reinforcement Learning-based Approximate Convex Decomposition},
  author={Luo, Yuzhe and Pan, Zherong and Wu, Kui and Du, Xingyi and Zeng, Yun and Tang, Xiangjun and Wu, Yiqian and Jin, Xiaogang and Gao, Xifeng},
  journal={ACM Transactions on Graphics (TOG)},
  volume={44},
  number={6},
  pages={1--12},
  year={2025},
  publisher={ACM New York, NY, USA}
}
```
