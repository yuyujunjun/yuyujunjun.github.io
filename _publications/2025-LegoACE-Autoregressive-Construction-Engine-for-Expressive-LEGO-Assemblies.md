---
collection: "publications"
citation: "/assets/files/publications/2025Lego/citation.txt"
cover: "/assets/files/publications/2025Lego/teaser.jpg"
layout: "publication"
links:
  Paper: /assets/files/publications/2025Lego/main.pdf
  Project: https://xh38.github.io/LegoACE/
  Code: https://github.com/xh38/LegoACE-code
title: "LegoACE: Autoregressive Construction Engine for Expressive LEGO® Assemblies"
date: "2025-01-01"
pub_date: "2025"
permalink: "/publication/2025-LegoACE-Autoregressive-Construction-Engine-for-Expressive-LEGO-Assemblies"
selected: "false"
authors:
- Hao Xu
- Yuqing Zhang
- Yiqian Wu
- Xinyang Zheng
- Yutao Liu
- Xiangjun Tang
- Yunhan Yang
- Ding Liang
- Yingtian Liu
- Yuanchen Guo
- Yanpei Cao
- Xiaogang Jin
pub: "Proceedings of the SIGGRAPH Asia 2025 Conference Papers"
pub_ab: "SIGGRAPH Asia"
---
## Abstract

Automated LEGO design is challenging due to the extensive variety of LEGO brick types and the necessity of constructing semantically meaningful models from individually meaningless components. Current automatic LEGO generation methods face two key challenges: i) They typically rely on explicit modeling of brick connectivity to ensure structural validity. However, this requires extensive manual annotation, which is labor-intensive as the variety of LEGO primitives increases. This limits training data diversity, restricting the variety of LEGO bricks that can be effectively utilized. ii) To facilitate learning within neural networks, current methods often employ either volume or text-based descriptions to represent LEGO models. However, volumetric representations are computationally expensive and hamper large-scale generative training, while text-based approaches rely on large language models and dedicated text-to-brick mapping rules, introducing a semantic gap between language tokens and 3D brick structures. To address these challenges, we propose LegoACE, an autoregressive construction engine for expressive LEGO assembly generation conditioned on text prompts or multi-view normal maps. By leveraging the sequential nature of LEGO assemblies, LegoACE implicitly learns connection relationships by modeling the conditional distribution of each brick’s position, orientation, and type based on previously placed bricks. This formulation enables us to construct a large-scale dataset, LegoVerse, which comprises over 55,000 unique models with 9,314 different brick types. To precisely represent LEGO primitives while minimizing computational overhead, we propose a tokenization strategy, LEGO Native Tokenization Algorithm, which transforms unstructured bricks into compact tokens encoding position, rotation, and type. This enables a decoder-only transformer to autoregressively generate LEGO models based on conditional inputs. Furthermore, to enhance model performance, we apply Direct Preference Optimization (DPO) to fine-tune LegoACE. Our experimental results show that LegoACE demonstrates the ability to generate diverse and expressive LEGO assemblies with robust brick connectivity, significantly advancing the state-of-the-art in LEGO model generation.

**bibtex:**
```
@inproceedings{10.1145/3757377.3763881, 
author = {Xu, Hao and Zhang, Yuqing and Wu, Yiqian and Zheng, Xinyang and Liu, Yutao and Tang, Xiangjun and Yang, Yunhan and Liang, Ding and Liu, Yingtian and Guo, Yuanchen and Cao, Yanpei and Jin, Xiaogang}, 
title = {LegoACE: Autoregressive Construction Engine for Expressive LEGO® Assemblies}, 
year = {2025}, 
booktitle = {Proceedings of the SIGGRAPH Asia 2025 Conference Papers},
articleno = {40},
numpages = {11}, 
series = {SA Conference Papers '25} }

```
