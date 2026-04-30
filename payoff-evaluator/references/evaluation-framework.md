# Payoff Evaluator Reference

## 1. Evaluation Frame

Use this frame to judge whether a plan is necessary:

1. Purpose: What real outcome does the user want?
2. Current pain: What concrete loss, friction, risk, or missed opportunity exists now?
3. Fit: Does the proposed plan directly solve that pain?
4. Payoff: What measurable or observable benefit should appear?
5. Cost: What money, time, attention, maintenance, switching cost, and opportunity cost are required?
6. Alternatives: What cheaper, smaller, reversible, delayed, borrowed, rented, reused, or manual option exists?
7. Counterfactual: What happens if the user does nothing, waits, or narrows the plan?
8. Reversibility: If the plan fails, how much loss remains?

The phrase "为了醋包饺子" maps to this failure pattern:

- The stated plan is much larger than the real purpose.
- The user over-invests in infrastructure before proving the need.
- The plan creates new maintenance or attention costs.
- A cheaper direct path can satisfy the purpose.

## 2. Anti-Sycophancy Check

Before deciding, explicitly create the strongest opposing case:

- Failure path: How could this plan fail even if executed well?
- Desire laundering: Is the user turning a desire into a fake necessity?
- Tool-first thinking: Is the user buying/building/preparing instead of doing the real work?
- Scale mismatch: Is the solution too large for the actual problem?
- Future-use fiction: Is the plan justified by vague future scenarios?
- Social/status pressure: Is the real payoff identity, novelty, or comparison?
- Hidden cost: What recurring cost will appear after the initial decision?

If this opposing case is stronger than the supporting case, decide `没必要`.

## 3. Burden Of Proof Rules

`必要` requires strong evidence:

- The user has a concrete, recurring, costly problem.
- The plan solves the core bottleneck, not a side issue.
- Alternatives were tried or are clearly insufficient.
- The payoff is near-term enough to verify.
- The cost is proportional to the problem.
- Delay would produce meaningful loss.

`没必要` is appropriate when:

- The purpose is vague or mostly emotional.
- The plan is justified by "maybe later", "could be useful", or "I feel I should".
- The user has not tried cheaper alternatives.
- The cost is high but the benefit is speculative.
- The plan creates a new commitment before validating demand.
- The same outcome can be reached by a smaller action.

When uncertain after the maximum interview depth, default to `没必要`, and recommend the smallest validation step.

## 4. Question Bank

Ask only one question per turn. Pick the single question that most reduces decision uncertainty.

Every interview question should be offered as choices plus custom input, but choose the input mode by question type. Do not use a recommended option for fact collection.

Input mode rules:

- Fact collection: use multi-select, no recommended option. This includes symptoms, motives, costs, risks, constraints, alternatives, and current pain.
- Priority selection: use single-select, no recommended option. This is only for asking the user to identify the primary bottleneck or most important goal.
- Decision confirmation: use single-select only after enough facts are collected.
- Free explanation: use custom input when options would distort the answer.

If the environment provides a structured UI that supports multi-select without a recommendation, use it. If the only available structured UI forces a recommended single choice, do not use it for fact collection; render a Markdown multi-select question instead.

Multi-select format:

```text
<one focused question>

可多选：
A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
D. <meaningful option if useful>
自定义：<ask the user to type their own answer>
```

Single-select format:

```text
请选择最主要的一项：
A. <meaningful option>
B. <meaningful option>
C. <meaningful option>
自定义：<ask the user to type their own answer>
```

Do not include fake choices. The options should expose the decision pattern, not merely restate yes/no.

Purpose questions:

- "这件事真正要解决的结果是什么？如果只说结果，不说方案，它是什么？"
- "你希望它改善哪一个具体指标、状态或痛点？"
- "如果这个计划成功了，你会看到什么变化？"

Pain and urgency questions:

- "如果不做这件事，接下来一个月会有什么具体损失？"
- "这个问题发生过几次？每次大概损失多少时间、钱或机会？"
- "为什么是现在，而不是等一周或一个月？"

Fit questions:

- "这个方案解决的是核心瓶颈，还是只是让你感觉更像在推进？"
- "如果只允许做最小动作，你会删掉哪些部分？"
- "有没有证据表明问题真的出在这个环节？"

Cost questions:

- "这件事完整成本是多少，包括钱、时间、学习、迁移、维护和注意力？"
- "做了它会挤掉哪件更重要的事？"
- "失败或闲置后，无法收回的成本是什么？"

Alternative questions:

- "有没有更便宜、更小、可租、可借、可试用或先手动完成的替代方案？"
- "你已经试过哪些低成本替代方案，结果如何？"
- "能不能先做一个 10% 版本来验证需求？"

Counterfactual questions:

- "如果完全不做，会发生什么？"
- "如果延后一个月，会损失什么？"
- "如果把规模缩小一半，还能达到核心目的吗？"

## 5. External Counter-Evidence Search

Search externally when the decision depends on unstable facts, costly purchases, tool choice, current prices/specs, health/legal/financial claims, or user explicitly asks.

Search negative evidence first. Useful query patterns:

- `<plan or product> regret`
- `<plan or product> not worth it`
- `<plan or product> hidden cost`
- `<plan or product> failure case`
- `<plan or product> cheaper alternative`
- `<plan or product> overkill`
- `<product category> common mistakes`
- `<project type> why it failed`
- `<tool/framework> migration cost`
- `<purchase> do I really need`

For Chinese searches:

- `<计划或产品> 后悔`
- `<计划或产品> 不值得`
- `<计划或产品> 隐性成本`
- `<计划或产品> 失败案例`
- `<计划或产品> 平替`
- `<计划或产品> 过度设计`
- `<购买对象> 有没有必要`

Use sources as evidence, not authority. A source can show common failure modes, but the final decision still depends on the user's purpose, cost, and alternatives.

## 6. Final Decision Template

```text
结论：必要/没必要

必要性是否被证明：
用 1-3 句话说明计划是否完成举证。

最强反方证据：
列出最强的反对理由，说明为什么它重要。

关键理由：
1. 目的是否明确。
2. 收益和代价是否匹配。
3. 替代方案是否足够。

最大不确定性：
指出一个最影响判断但仍未验证的点。

下一步行动：
给一个小而可执行的动作。若结论是没必要，优先给低成本替代方案。
```

## 7. Example: New Computer

User: "我想买一台新电脑，有没有必要？"

Good first question:

```text
先确认真实瓶颈。你现在这台电脑具体卡在哪类任务上？

可多选：
A. 工作/学习任务已经明显被性能、兼容性或稳定性拖慢
B. 主要是续航、屏幕、便携或外观体验不满意
C. 现在还能用，是为未来可能的任务提前准备
D. 没有明确任务，更多是想换新或被新品吸引
自定义：请说明具体任务和每周大概损失多少时间或机会
```

Possible follow-up path:

1. Confirm the real bottleneck: performance, portability, reliability, software compatibility, professional need, or pure desire.
2. Ask whether the user has tried cheaper fixes: clean storage, reinstall system, add memory/storage, external monitor/keyboard, cloud machine, rental, repair, used device.
3. Ask what task requires the new computer and whether that task already exists today.
4. Ask total budget and what else that money would otherwise support.
5. Check anti-sycophancy: is the user buying a new device to feel ready before doing the real work?

Likely `必要` case:

- Current machine blocks recurring work.
- Loss is concrete and frequent.
- Cheaper fixes are tried or impossible.
- New machine directly removes the bottleneck.
- Budget is proportional to the work value.

Likely `没必要` case:

- The current pain is vague.
- The main reason is freshness, aesthetics, identity, or imagined future productivity.
- The user has not tried cheaper fixes.
- The task requiring the new computer has not actually started.
- A repair, used machine, rental, or workflow change can solve the real issue.

## 8. Example: New iPhone

User: "我现在想买一部 iPhone，你觉得有必要吗？"

Do not immediately search prices or give a conclusion. The first response should start the interview:

```text
先不下结论。买新 iPhone 的必要性取决于它解决的具体问题。你现在这台手机主要卡在哪里？

可多选：
A. 已经影响刚需任务，比如通话、支付、工作、拍摄、导航或安全
B. 主要是续航、存储、卡顿、屏幕或维修成本问题
C. 现在还能用，但想要新功能、审美、手感或更好的体验
D. 只是看到新品、优惠或别人推荐后产生了购买冲动
自定义：请说明当前手机型号、具体问题和这个问题每周造成的损失
```

Only after the user answers should the evaluator decide whether to ask follow-up questions, search current facts, or make a final decision.
