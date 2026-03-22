# Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data：第一遍（原初还原）

## 书目信息

- 标题：Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data
- 作者：John D. Lafferty、Andrew McCallum、Fernando C. N. Pereira
- 年份：2001
- 发表：ICML, pp.282-289

## 第一遍八项输出

### 1) 原始问题

引言聚焦如何避免局部归一化模型在序列标注中的偏置问题。

### 2) 问题重要性

论文提出条件随机场作为判别式序列建模框架，兼顾全局一致性与特征灵活性，成为结构化预测的重要基线。

### 3) 更大心理地图

作者将问题组织为：序列标注问题设定；CRF 模型定义与训练；与 HMM/MEMM 比较；实验评估。

### 4) 同一整体中的关键对象

- 序列标注问题设定
- CRF 模型定义与训练
- 与 HMM/MEMM 比较
- 实验评估

### 5) 核心概念（3–7）

1. 序列标注问题设定
2. CRF 模型定义与训练
3. 与 HMM/MEMM 比较
4. 实验评估
5. Bayes / probability
6. 问题建模
7. 边界条件

### 6) 方法承诺

作者在 Bayes / probability 路线内采用结构化建模与分层推进的方法承诺。

### 7) 主动切除的边界

- 优先处理文献中明确定义的问题对象，不外推到未定义任务
- 区分文献内部可证明主张与外部解释性扩展
- 重点防止误读：将条件建模优势误读为对任意任务的全面优势；忽略特征设计对 CRF 性能的决定性作用

### 8) 一句压缩：该文献开辟了何种问题空间

该文献开辟了一个围绕“Bayes / probability”组织问题并以结构化论证推进结论的问题空间。
