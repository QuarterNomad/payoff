# Payoff Evaluator Reference

## Table of contents

- [1. Decision routing](#1-decision-routing)
- [2. The lenses](#2-the-lenses)
- [3. quick exit](#3-quick-exit)
- [4. Anti-sycophancy check](#4-anti-sycophancy-check)
- [5. Burden of proof rules](#5-burden-of-proof-rules)
- [6. Interview strategy](#6-interview-strategy)
- [7. Route-specific question bank](#7-route-specific-question-bank)
- [8. External counter-evidence search](#8-external-counter-evidence-search)
- [9. Final decision template](#9-final-decision-template)

For concrete phrasings and worked examples, read `references/examples.md`.

## 1. Decision routing

Route the decision before asking a long chain of questions. This skill stays focused on one output: `必要` or `没必要`.

Classify the user's situation into one of these lanes:

| Lane | When to use it | Primary lenses | Default depth |
|---|---|---|---|
| `小而可逆` | Cheap, low-risk, easy to undo, low-measure decisions | `measure` + `reversibility` | `quick exit`, usually 0-2 questions |
| `购买/支出` | Devices, subscriptions, tools, courses, services | `measure` + `reversibility` + alternatives + total cost | Moderate |
| `承诺型投入` | Projects, side businesses, refactors, learning paths, career moves | `measure` + `reversibility` + `inversion` + `commitment` | Deepest |

If the user has not described a concrete plan, ask them to make it concrete before routing.

If the user is really asking an A-vs-B comparison, do not turn this into a weighted comparison framework. Narrow it back to necessity:

- Is either option actually necessary?
- Is this a decision that needs to be made now?
- Is there a smaller or reversible step before choosing?

## 2. The lenses

### measure

`measure` asks how long and how often the decision acts on the user's life.

- High `measure`: recurring, compounding, or identity-shaping effects over months or years.
- Low `measure`: one-off, short-lived, easily forgotten.

High `measure` decisions deserve more analysis. Low `measure` decisions should not borrow seriousness from fantasy future use.

### reversibility

`reversibility` asks how hard it is to back out if the decision is wrong.

| Type | Meaning | Default stance |
|---|---|---|
| Easy to reverse | Low cost, low switching friction | Lean toward `quick exit` |
| Reversible but costly | Can undo, but not cheaply | Ask more before deciding |
| Hard to reverse | Irrecoverable loss, major lock-in, social or legal consequences | Be conservative and run `inversion` |

### inversion

`inversion` flips the desire-driven framing and asks what failure looks like.

Useful prompts:

- If this turns out to be a mistake, what will have caused it?
- What are the 3 most likely failure paths?
- If they wait 30 days, what real loss occurs?
- If they do nothing, what actually breaks?
- What would make this look like classic overkill in hindsight?

### commitment

Use `commitment` for long-horizon effort, not for every small purchase.

Minimum checks:

1. **Specific grind test**: what exact pain, boredom, maintenance, or embarrassment comes with this path?
2. **Absorbed values check**: would the user still want this if nobody else saw it?
3. **Motivation check**: are they choosing it because it matters, or because indecision feels uncomfortable?
4. **100% check**: are they willing to seriously do it for the required period, instead of half-committing?

Failing 1 or 4 is strong evidence for `没必要`.

## 3. quick exit

Use `quick exit` when the decision is small, reversible, and low-measure.

The goal is not to sound profound. The goal is to avoid wasting analysis on tiny calls.

Default `quick exit` logic:

- If the downside is tiny and fully reversible, one clean reason may be enough.
- If the upside is vague and the user is only mood-driven, lean `没必要`.
- If doing nothing costs almost nothing, do not manufacture urgency.
- If a trial version exists, recommend the smallest trial instead of a big commitment.

You can still ask one question, but it should be decisive:

- "如果现在不做，接下来一周到底会损失什么？"
- "做错了以后，能不能轻松撤回？"

If both answers are weak, stop and decide `没必要`.

## 4. Anti-sycophancy check

Before deciding, explicitly create the strongest opposing case:

- Failure path: how could this plan fail even if executed competently?
- Desire laundering: is the user turning a want into a fake necessity?
- Tool-first thinking: are they buying, preparing, or restructuring instead of doing the real work?
- Scale mismatch: is the proposed solution much larger than the actual problem?
- Future-use fiction: is the case built on imagined future scenarios rather than present friction?
- Hidden cost: what recurring maintenance, switching, or attention cost appears after the initial move?

If the opposing case is stronger than the supporting case, decide `没必要`.

The phrase "为了醋包饺子" maps especially well to these patterns:

- The stated plan is much larger than the real purpose.
- The user over-invests in infrastructure before proving the need.
- The plan creates a new commitment before solving today's bottleneck.
- A cheaper direct path can satisfy the same real goal.

## 5. Burden of proof rules

`必要` requires strong evidence:

- The user has a concrete and important goal.
- The current pain is real, recurring, and costly enough.
- The issue has enough `measure` to justify attention.
- The plan directly addresses the core bottleneck.
- Cheaper or smaller alternatives were tried or are clearly insufficient.
- `reversibility` and downside are acceptable.
- If the plan is long-horizon, `commitment` is real rather than imagined.
- Delay would produce meaningful loss.

`没必要` is appropriate when:

- The purpose is vague, status-driven, novelty-driven, or mostly emotional.
- The plan is justified by "maybe later", "could be useful", or "I feel I should".
- The user has not tried smaller or cheaper alternatives.
- The cost is real but the payoff is speculative.
- The decision is low-measure but wrapped in high-drama language.
- The user wants the upside but avoids the real grind.

When uncertain after the maximum interview depth, default to `没必要`, and recommend the smallest validation step.

## 6. Interview strategy

Ask only one question per turn. Pick the single question that most reduces decision uncertainty.

Every interview question should be offered as choices plus custom input, but choose the input mode by question type. Do not intentionally recommend a factual answer.

Input mode rules:

- Fact collection: if the question is not inherently single-choice, use multi-select.
- Priority selection: use single-select. In Plan mode, prefer `request_user_input`.
- Decision confirmation: use single-select only after enough facts are collected.
- Free explanation: use custom input when options would distort the answer.

If the environment provides a structured UI that supports true multi-select without a recommendation, use it. If Plan mode only provides `request_user_input`, remember that it is single-select plus `Other`, not multi-select. In that environment:

- use `request_user_input` only for genuinely single-choice questions
- use Markdown multi-select for fact collection that can have multiple true answers
- never add a fake "自定义" option because the structured UI already has `Other...`

Multi-select format:

```text
<one focused question>

可多选：
A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
D. <meaningful option if useful>
其他：<ask the user to type their own answer>
```

Single-select format:

```text
请先选最接近的一项。忽略界面上的“推荐”标记，它只是 UI 限制；如果都不准确，使用系统自带的 Other。

A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
```

Do not include fake choices. The options should expose the decision pattern, not merely restate yes/no.

## 7. Route-specific question bank

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

## 8. External counter-evidence search

Search externally when the decision depends on unstable facts, costly purchases, tool choice, current prices/specs, health/legal/financial claims, or the user explicitly asks.

Search negative evidence first. Useful query patterns:

- `<plan or product> regret`
- `<plan or product> not worth it`
- `<plan or product> hidden cost`
- `<plan or product> failure case`
- `<plan or product> cheaper alternative`
- `<plan or product> overkill`
- `<project type> why it failed`
- `<tool/framework> migration cost`

For Chinese searches:

- `<计划或产品> 后悔`
- `<计划或产品> 不值得`
- `<计划或产品> 隐性成本`
- `<计划或产品> 失败案例`
- `<计划或产品> 平替`
- `<计划或产品> 过度设计`

Use sources as evidence, not authority. A source can show common failure modes, but the final decision still depends on the user's purpose, costs, and alternatives.

## 9. Final decision template

Present results in a compact structure. Show only the lenses that were actually used.

```text
结论：必要/没必要

决策分流：
- 类型：...
- 为什么归到这一类：...

镜头摘要：
| Lens | Signal | Finding |
|---|:---:|---|
| measure | 绿/黄/红 | ... |
| reversibility | 绿/黄/红 | ... |
| inversion | 绿/黄/红 | ... |
| commitment | 绿/黄/红 | 仅长期投入时展示 |

必要性是否被证明：
用 1-3 句话说明计划是否完成举证。

最强反方证据：
列出最强的反对理由，说明为什么它重要。

关键理由：
1. ...
2. ...
3. ...

最大不确定性：
指出一个最影响判断但仍未验证的点。

最早的打脸信号：
如果这个判断是错的，最早会出现什么信号。

What to watch:
The earliest signal that should trigger a re-check or a stop.

下一步行动：
给一个小而可执行的动作。若结论是没必要，优先给低成本替代方案。
```
