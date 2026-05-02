# Payoff Evaluator Reference

## Table of contents

- [1. Decision routing](#1-decision-routing)
- [2. The lenses](#2-the-lenses)
- [3. quick exit](#3-quick-exit)
- [4. Anti-sycophancy check](#4-anti-sycophancy-check)
- [5. Burden of proof rules](#5-burden-of-proof-rules)
- [6. Final decision template](#6-final-decision-template)

For concrete phrasings and route-specific question banks, read `references/interview-strategy.md`.
For search timing and query patterns, read `references/search-strategy.md`.
For worked examples, read `references/examples.md`.

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

## 6. Final decision template

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

下一步行动：
给一个小而可执行的动作。若结论是没必要，优先给低成本替代方案。
```
