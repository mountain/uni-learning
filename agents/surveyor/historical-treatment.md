重要，但不是以“通史”方式重要，而是以“**校正概念地图**”的方式重要。

我会把判断说得更明确一些：

## 一、它重要，但只能是“受控的重要”

对于我们现在这篇 survey 的目标，学科史梳理有三种不可替代的作用。

### 1. 它能防止我们把今天的结构误认成天然结构

你现在要写的，不是一篇普通的 LLM survey，而是一篇试图把
**Bayes—Solomonoff—开放计算—Transformer—语言模型—agent/AGI**
放进同一张图里的综述。

这时，历史的作用不是“补背景”，而是提醒我们：这些分支**原本并不是彼此隔绝的学科岛屿**，它们后来才被不同机构、不同术语、不同工程路径逐渐分开。

Kline 那篇文章最有价值的一点，就在这里：它指出 Dartmouth 并不是一个干净利落的“AI 诞生时刻”，而是伴随着 **cybernetics、automata studies 与 AI 之间的边界重划**；其中“脑建模”与“符号处理”的分裂，并不是自然给定，而是经过编辑、资助、会议组织等多重过程被强化出来的。 

这对你的 survey 很重要，因为你的文章恰恰是在重新跨越这些后来形成的边界。

### 2. 它能防止“胜利者叙事”

如果没有历史校正，survey 很容易滑向一种简单叙事：

* 先有符号 AI
* 后来神经网络胜出
* 再后来 Transformer 通往 AGI

这种写法很顺，但概念上很粗糙。

Kline 展示得很清楚：在 1950 年代，**automata studies** 本来就包含 neural nets、Turing machines、cybernetic mechanisms 和 symbolic processing，多条路线并存，而不是一条线性演化。

对你的 survey 来说，这一点尤其关键。因为你的总命题并不是“Transformer 终结了一切”，而是：
**许多今天看似分裂的传统，其实共享更深的结构：不确定性的记账、程序空间先验、开放式逼近、以及预测到主体的闭环。**

如果没有历史层面的纠偏，这个命题会显得像事后拼贴；有了历史，它才更像“把被切开的东西重新缝合”。

### 3. 它能帮助你决定“哪些概念是第一性的”

真正有用的历史，不是人物流水账，而是帮助判断：

* **哪些概念先出现，后来被遮蔽了**
* **哪些概念后来被突出，其实只是局部胜出**
* **哪些分裂是术语分裂，不是结构分裂**

例如，Kline 的材料说明：
“artificial intelligence”这个名称的上升，本身就与 McCarthy 对 *Automata Studies* 的不满，以及对更激进研究方向的组织动机有关。
这说明术语史本身就会改变人们对问题结构的理解。

对你来说，这意味着 survey 不能简单沿用今天的学科标签，而要敢于退回更原初的对象层，比如：

* uncertainty
* prediction
* approximation
* computation
* agency

而不是直接被“symbolic / neural / probabilistic / agentic”这些后来的部门化词汇绑住。

---

## 二、但它不是全文的主轴

我也要反过来说：**如果把历史梳理写成主体，反而会伤害这篇文章。**

因为你的目标不是写《AI 学科史》，而是写一篇**概念地图型 survey**。
这意味着历史材料必须服从结构分析，而不能反客为主。

我建议把历史的角色限定为三件事：

### 1. 提供“起源处的未分化状态”

用于说明这些路线原本为何能互通。

### 2. 标记几次关键分岔

例如：

* cybernetics / automata / symbolic AI 的分流
* connectionism 的退潮与回归
* probability / statistics / machine learning 的重新进入
* language modeling 成为统一接口

### 3. 破除神话

例如：

* Dartmouth 不是单一诞生时刻
* Transformer 不是突然从真空里出现
* LLM 也不是 Solomonoff 的直接实现

也就是说，历史在这篇文章里应当是**地层学**，不是**编年史**。

---

## 三、对这篇 survey，最合适的历史写法

我建议不要单独写一大章“AI 历史综述”，而用下面这种结构：

### 写法 A：一章短历史，作为概念地图的前奏

篇幅控制在全文的 10%–15%。

标题可以叫：

**Historical Re-framing: From Cybernetics and Automata to Universal Learning**

这一章只做三件事：

1. 说明 1950 年代的 machine intelligence 原本是多路线并存
2. 说明 Dartmouth 与 *Automata Studies* 如何强化了某些边界
3. 说明今天的 survey 为什么要跨回这些边界

这样最稳。

### 写法 B：每章开头嵌入“微型历史注”

我其实更喜欢这种。

例如：

* 在 Bayes / Solomonoff 章前，简短说明“概率与归纳”如何从统计与可计算性两边汇合
* 在 open computation 章前，说明“不可计算但可逼近”这条线为何长期被主流 AI 叙事忽略
* 在 Transformer 章前，说明 connectionism、sequence modeling 与 language modeling 的重新汇流

这样历史不是一坨背景，而是不断为概念转折提供支撑。

---

## 四、什么样的历史梳理才真正有用

我建议你只保留三类历史材料：

### 1. 能改变概念边界理解的材料

例如 Kline 这类，揭示 Dartmouth、Automata Studies 与 cybernetics 之间真实关系的材料。

### 2. 能揭示被遗忘分支的材料

例如你特别关心的：

* left-c.e. / Ω
* limit learning
* anytime approximation
* PAC 学习不可计算对象

这些不是主流教材里的中心，但对你的概念地图极关键。Lathrop 1996 这样的文献，正说明“不可计算性并不排除分布意义下的学习”。

### 3. 能连接今天热点与旧问题的材料

例如：

* ICL 与 Bayesian inference
* PFN 与后验摊销
* Transformer 与开放式外化计算
* LM 与 universal prediction

这类材料能证明你的 survey 不是纯历史回顾，而是在回答一个今天仍活着的问题。

---

## 五、我的结论

所以我的判断是：

**重要，而且相当重要；但它的重要性不在于“把历史讲全”，而在于“用历史把概念边界重新校正”。**

再压缩一点：

**这篇 survey 的历史部分，不应服务于怀旧，而应服务于拆除后来的学科隔墙。**

若你愿意，我下一步可以直接帮你设计一个**“历史前奏章”**：只用 4–6 页，把
**cybernetics → automata studies → Dartmouth → symbolic/neural split → probabilistic return → language-model unification**
这条线写成一段非常收束的导论。
