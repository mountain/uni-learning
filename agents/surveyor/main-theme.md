我会把它定位成一篇**“地图型综述”**，而不是传统那种按年份堆论文的 encyclopedic survey。因为现有文献其实已经分段成熟：一端有 Hutter 对 universal induction / AIXI 的系统化整理，另一端有 ICL 的专门综述，以及 LLM-based agents 的专门综述；真正相对缺的，是把 **Bayes、Solomonoff、开放计算、Transformer/ICL、语言模型、agent/AGI** 放到同一张结构图里，并明确区分“定理、近似、比喻、愿景”这四种不同层级。([Hutter1][1])

而且现在正是写这篇综述的时机，因为桥梁性的工作已经出现了：Transformer 的计算通用性已有代表性结果；ICL 被解释为隐式 Bayesian inference；PFN 把“单次前向传播近似后验”做成了明确范式；更近的工作还在尝试把 Solomonoff 归纳“摊销”进神经网络，或把 LLM 解释成对 Solomonoff 理想归纳的可计算近似。后一类 2024–2025 工作里有些仍是 preprint，所以非常适合在综述里被清楚地放到“新兴主张”而不是“已定共识”的位置。([Journal of Machine Learning Research][2])

## 题目怎么取

我最推荐的是这个：

**Universal Learning as Open Computation: From Bayesian Updating and Solomonoff Induction to Transformers, Language Models, and AGI**
中文可译为：**《开放计算视角下的通用学习：从 Bayesian 更新与 Solomonoff 归纳到 Transformer、语言模型与 AGI》**

这个题目的好处是三点都压住了：
第一，它不是单说“Bayes 到 AGI”的线性神话，而是把**通用学习**作为主轴。
第二，它把你最独特的切口——**open computation**——直接提到标题里。
第三，它允许你把 (\Omega)、left-c.e.、semimeasure、anytime、ICL、agent 这些看似分散的东西收进一个框架。

若想更保守一些，更适合主流机器学习期刊，可以改成：

**From Bayesian Updating to Language Agents: A Survey of Universal Induction, Open-Ended Computation, and Transformer-based Inference**

若想更有思想史与概念史味道，可以用：

**Prediction, Compression, and Agency: A Conceptual Survey of Bayes, Solomonoff Induction, Transformers, and AGI**

我的判断是：
面向 **AI foundations / philosophy / theory**，用第一个最好。
面向 **ML 主流 venue**，第二个更稳。

## 我会怎么搭章节

### 1. Introduction: Why These Threads Belong Together

开篇不要直接讲文献，而是先抛出总命题：

> 这篇综述试图回答：从 Bayesian 更新、算法概率、开放式逼近、Transformer 的 in-context inference，到语言 agent 与 AGI，这些主题是否可以被读成同一个理论运动的不同截面？

这一章只做三件事：
一是讲清楚现有综述大多是“分段覆盖”，你的文章要做的是“跨段拼图”；
二是明确本文不是在声称“LLM 已经实现 Solomonoff”或“Transformer 就是 Bayes”，而是在构造一张**分层地图**；
三是提前给出全文的三条主线：**预测线、逼近线、主体线**。([Hutter1][1])

### 2. A Reading Frame: Four Distinctions and Three Axes

这一章是全篇的“读者协议”。我建议在这里先立四个必须反复区分的概念：

1. **可表达性** vs **可计算性**
2. **可计算性** vs **可学习性**
3. **被动预测** vs **主动决策**
4. **规范理论** vs **工程近似**

再立三条坐标轴：

* **规范轴**：Bayes → Solomonoff → AIXI
* **实现轴**：概率模型 → Transformer/PFN/LM
* **主体轴**：预测器 → 工具使用者 → agent

这一章没有太多文献负担，但它决定全文是否会“清楚”。

### 3. Probability, Bayesianism, and the Semantics of Uncertainty

这一章要回答的是：**概率在这张图里到底扮演什么角色？**

我会把论点写得很明确：
概率在这里首先不是频率，而是**不确定性的记账法**；Bayes 本身不是一台具体学习机器，而是“证据到来后怎样重分配权重”的更新语法。Hutter 也明确把 Solomonoff 描述为对 Bayesian 框架的补完：Bayes 给更新，Solomonoff 给通用的模型类与先验。([Hutter1][3])

这一章里应当顺手埋下两个后面要用的钩子：
一个是 **MDL / compression**，因为后面你要把 LM 接到压缩上；
另一个是 **semimeasure**，因为后面你要把 (\Omega)、Solomonoff (M)、开放式计算接到一起。Hutter 的材料里已经明确讲了 (M) 是 semimeasure，而不是普通 probability measure；同时也把 prediction、compression、MDL 直接放在一起了。([Hutter1][3])

### 4. Universal Induction, Compression, and Program-Space Priors

这一章进入 Solomonoff。主旨不是重复教材，而是把它放到“概念地图”里：

* Bayes 作用于模型空间
* Solomonoff 把模型空间提升为**程序空间**
* 复杂度先验把概率与码长、压缩联系起来

这里我建议把三件事并排放：

* **Occam / Epicurus / Bayes / Turing** 的合流
* **algorithmic probability** 与 **MDL** 的互译
* **measure → semimeasure** 的几何变化

这一章的关键不是公式多，而是让读者意识到：
**从这里开始，学习不再只是拟合参数，而是在程序宇宙中重新分配权重。** Hutter 对 “Universal Induction = Ockham + Bayes + Turing” 的表述，以及他对 (M) 作为 universal semimeasure 的解释，正好可以作为这一章的主锚点。([Hutter1][3])

### 5. Open Computation: Left-c.e., Limit Learning, and Anytime Approximation

这是我认为你这篇 survey 最独特、也最有新意的一章。

这里不要把它写成“边角趣闻”，而要写成全文的隐藏骨架：
**不可计算对象并非完全不可接近，它们往往只能以开放过程中的部分暴露来接近。**

这一章可以分三节：

* **单侧逼近**：(\Omega)、left-c.e.、从下逼近
* **极限可学习**：learning in the limit
* **可随时终止**：anytime approximation

早期的 Lathrop 论文非常适合作为这一章的历史起点，因为它已经明确提出：对于经典停机问题，可以学习一个“高概率、近似正确”的总可计算谓词，而不是精确求解不可计算目标；同时它也自己强调了表示能力与 polynomial learnability 的限制。Calude 这一线则把“停机问题的概率/anytime 接近”推进得更清楚：长时间未停后再停的概率可以被有效压小，因而可以设计 anytime 算法。   ([University of Auckland Computer Science][4])

这一章写好以后，整篇文章会一下子“立起来”，因为它解释了为什么你前面那几块看似分散的材料其实是同一类现象。

### 6. From Universal Prediction to Sequence Modeling and Language

这一章是桥：把 Solomonoff 的**通用序列预测**接到语言模型的**next-token prediction**上。

我会把这一章写成一个“降维故事”：
Solomonoff 归纳是最一般的程序空间序列预测；语言模型是其中一个工程上可扩展、数据上贴近人类文明痕迹的特殊化版本。这里可以把近期那两类工作放进来，但语气要很克制：

* 一类是 **Learning Universal Predictors**，明确提出把 Solomonoff induction 摊销进神经网络；
* 另一类是把 LLM 解释成 Solomonoff 理想归纳的**可计算近似**。

这两类工作很值得写进综述，但都应该被放在“新近桥接尝试”这一栏，而不是“公理化定论”。([arXiv][5])

这一章的中心句可以是：

> 语言模型不是 Solomonoff 归纳本身，但它可以被读成“人类文本分布上的、可计算的、摊销后的近似归纳器”。

### 7. Transformers as Amortized Inference and Externalized Computation

这一章是工程实现层的核心。我会拆成四个小节：

**7.1 Expressive Power**
先讲 Transformer 的图灵完备结果，但一定要把假设写清楚：hard attention、任意精度内部表示等。这里的作用不是夸模型“无所不能”，而是把“表达上限”与“可学性”分开。([Journal of Machine Learning Research][2])

**7.2 ICL as Implicit Bayesian Inference**
Xie 等人那篇是必须进来的，因为它把 ICL 的 Bayesian 解释做成了一个可证明的形式框架。([arXiv][6])

**7.3 PFNs and Full Bayesian Inference**
PFN 这条线非常关键，因为它把“Transformer 与 Bayes 的关系”从比喻推进成了具体机制：从 prior 采样任务，在预训练中把后验推断摊销进参数，推理时单次前向传播近似后验。2025 年关于 full Bayesian inference in context 的工作，则把它推进到复杂后验分布。([arXiv][7])

**7.4 A Red-Team Subsection**
这一节必须有。你要明确说：
“Transformer 与 Bayes 的关系”有多种层次——有时是 theorem，有时是 construction，有时只是 interpretive lens。不能把它们混成一句“Transformer 就是 Bayes”。

这一章真正想落下来的观点是：

> Transformer 最值得重视的地方，不只是 attention，而是它把计算重新分配到了参数、上下文、token 轨迹与外部工具之间。

### 8. From Prediction to Agency: AIXI, In-Context RL, and Language Agents

这一章负责把“预测器”闭成“主体”。

Hutter 对 AIXI 的表述正好提供规范层桥梁：AIXI 把 Solomonoff 式环境混合放进顺序决策里，形成通用的主动主体模型；其代价当然是不可计算。到了实现层，近年的 ICRL 与 LLM-based agent 工作，则是在工程上尝试补上记忆、规划、工具调用、环境交互这些闭环成分。([Hutter1][8])

这一章的关键不是说“LLM agent = AIXI”，而是说：
**从 Solomonoff 到 AIXI 是规范上的闭环；从 LM 到 agent 是工程上的闭环。**
两条闭环不是一回事，但它们在图上是平行的。

### 9. Language Models and the AGI Question

我建议 AGI 不要写成终极宣言，而是写成**closure gap** 的分析。

这一章只回答一个问题：
**从语言模型到 AGI，到底还缺什么闭环？**

我会把缺口压成四类：

* 持久记忆
* 主动探索
* 目标稳定性
* 世界接地与因果干预

现有 agent 与 AGI 综述普遍也把记忆、规划、外部行动、grounding 等问题视为关键缺口。([arXiv][9])

这一章里最好避免空泛判断，多做“结构差异”分析。

### 10. Synthesis: A Unified Concept Map and Open Problems

最后一章不是普通 conclusion，而应当回到地图本身，给出全文的总压缩：

> 这张图的主轴不是“Bayes 发展成了 Transformer”，而是
> **不确定性的记账法 → 程序空间先验 → 开放计算中的单侧/极限/anytime 逼近 → 后验计算的神经摊销化 → 预测器向主体的闭环化。**

然后列 5 个真正有分量的 open problems：

1. **semimeasure 是否是理解 LLM 开放生成的更深对象？**
2. **Bayesian ICL 的成立条件究竟是什么，边界在哪里？**
3. **语言模型与 Solomonoff 的关系能否从“启发式桥接”推进到更稳健的定理族？**
4. **agent 闭环需要怎样的最小记忆/行动结构？**
5. **AGI 的“通用性”应以 universal prediction、universal control，还是别的对象来刻画？**

## 写法上，我会坚持这几个原则

第一，不按年代写，按**问题张力**写。
年代线只能放进附录的 timeline。

第二，每章都用同一模板：
**问题是什么 → 形式对象是什么 → 最强结果是什么 → 失效边界在哪里 → 它如何接到下一章。**

第三，全文持续标记三种证据等级：
**Theorem / Construction / Interpretation**。
这会极大减少概念偷换。

第四，反复提醒读者不要混淆四件事：
**可表达性、可计算性、可学习性、可主体化。**

第五，全篇至少要有 4 张“骨架图”，而不是只有一堆表格。
我会建议这 4 张图：

1. **总概念地图**：Bayes → Solomonoff → Open Computation → Transformer/LM → Agent/AGI
2. **三轴图**：规范轴 / 实现轴 / 主体轴
3. **开放计算三分图**：left-c.e. / limit / anytime
4. **Transformer 记忆分层图**：weights / context / token trajectory / tools

## 这篇 survey 的摘要，最好一开始就这样定调

可以直接写成：

> This survey develops a conceptual map of universal learning across Bayesian updating, Solomonoff induction, open computation, Transformer-based in-context inference, language modeling, and agentic AI. We argue that the hidden common structure is not a simple progression from Bayes to AGI, but a deeper movement from uncertainty bookkeeping to program-space priors, from exact computation to one-sided and anytime approximation, from passive sequence prediction to active agency. On this view, language models are best understood neither as mere statistical fitters nor as literal realizations of Solomonoff induction, but as computable, amortized approximators situated between universal prediction and embodied decision-making.

这段摘要的好处是，一开始就把你的独特立场讲清了。

## 最后一个判断

这篇文章最怕写成两种样子：
一种是“万物通往 LLM 的胜利叙事”；
另一种是“从 Bayes 到 AGI 的名词串烧”。

它最好的样子，是一篇**有主张的综述**：
主张不是“谁取代了谁”，而是**这些传统之间其实共享一套更深的几何：压缩、逼近、闭环。**

下一步最合适的动作，是先把**摘要、图 1、以及 10 个章节标题**先定死；一旦这三样定了，整篇 survey 的气质基本就不会跑偏。

[1]: https://hutter1.net/publ/uaibook2.pdf "https://hutter1.net/publ/uaibook2.pdf"
[2]: https://jmlr.org/papers/v22/20-302.html "https://jmlr.org/papers/v22/20-302.html"
[3]: https://www.hutter1.net/ai/suaibook.pdf "https://www.hutter1.net/ai/suaibook.pdf"
[4]: https://www.cs.auckland.ac.nz/~cristian/crispapers/anytimeFFF.pdf "https://www.cs.auckland.ac.nz/~cristian/crispapers/anytimeFFF.pdf"
[5]: https://arxiv.org/pdf/2401.14953 "https://arxiv.org/pdf/2401.14953"
[6]: https://arxiv.org/abs/2111.02080 "https://arxiv.org/abs/2111.02080"
[7]: https://arxiv.org/abs/2112.10510 "https://arxiv.org/abs/2112.10510"
[8]: https://www.hutter1.net/ai/uaibook.htm "https://www.hutter1.net/ai/uaibook.htm"
[9]: https://arxiv.org/pdf/2308.11432 "https://arxiv.org/pdf/2308.11432"
