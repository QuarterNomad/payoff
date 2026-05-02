# Payoff Evaluator Interview Strategy

## Table of contents

- [Interview strategy](#interview-strategy)
- [Input mode rules](#input-mode-rules)
- [Multi-select format](#multi-select-format)
- [Single-select format](#single-select-format)
- [Route-specific question bank](#route-specific-question-bank)

## Interview strategy

Ask only one question per turn. Pick the single question that most reduces decision uncertainty.

Every interview question should be offered as choices plus custom input, but choose the input mode by question type. Do not intentionally recommend a factual answer.

## Input mode rules

- Fact collection: if the question is not inherently single-choice, use multi-select.
- Priority selection: use single-select only when there is genuinely one dominant answer.
- Decision confirmation: use single-select only after enough facts are collected.
- Free explanation: use custom input when options would distort the answer.

If the environment provides a structured UI that supports true multi-select without a recommendation, use it. If the environment only provides single-select plus `Other`, remember that it is not multi-select. In that environment:

- use structured single-select only for genuinely single-choice questions
- use Markdown multi-select for fact collection that can have multiple true answers
- never add a fake "自定义" option because the structured UI already has `Other...`
- if the UI auto-adds a recommendation marker, explicitly tell the user to ignore it

## Multi-select format

```text
<one focused question>

可多选：
A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
D. <meaningful option if useful>
其他：<ask the user to type their own answer>
```

## Single-select format

```text
请先选最接近的一项。忽略界面上的“推荐”标记，它只是 UI 限制；如果都不准确，使用系统自带的 Other。

A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
```

Do not include fake choices. The options should expose the decision pattern, not merely restate yes/no.

## Route-specific question bank

### 小而可逆

Ask for the minimum signal:

- "如果不做，接下来一周到底损失什么？"
- "做错了以后，能不能轻松撤回？"
- "有没有更小的试法，现在就能验证？"

### 购买/支出

Focus on present friction, total cost, and reversibility:

- "你现在到底卡在哪个具体任务上？"
- "这个问题每周损失多少时间、钱或机会？"
- "你试过哪些更便宜、更小或可租可借的替代方案？"
- "完整成本是多少，包括迁移、维护、学习和注意力？"
- "如果买了以后发现不值，退货、转卖、停用的代价有多大？"

### 承诺型投入

Focus on whether this solves the right problem and whether the user will actually sustain it:

- "这件事真正要解决的结果是什么？如果不说方案，只说结果，它是什么？"
- "这个方案解决的是核心瓶颈，还是只是让你感觉像在推进？"
- "如果只允许做 10% 的版本，你会保留什么？"
- "最具体的长期代价是什么？你真的愿意承受它吗？"
- "如果一个月后还没开始执行，最可能卡在哪里？"
