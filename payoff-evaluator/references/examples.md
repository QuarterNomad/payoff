# Payoff Evaluator Examples

## Table of contents

- [New computer](#new-computer)
- [Side project](#side-project)
- [Small purchase](#small-purchase)
- [Refactor](#refactor)

Use these examples when you need concrete phrasings, route-specific openings, or worked examples for realistic user requests.

## New computer

User: "我想买一台新电脑，有没有必要？"

Likely route:

- `购买/支出`

Good first question:

```text
先确认真实瓶颈。

可多选：
A. 工作或学习任务已经被性能、兼容性或稳定性拖慢
B. 主要是续航、屏幕、便携或整体体验不满意
C. 现在还能用，这次更多是在为未来需求或换新冲动做准备
其他：请说明具体任务和每周大概损失多少时间或机会
```

Likely `必要` case:

- Current machine blocks recurring work.
- Loss is concrete and frequent.
- Cheaper fixes are tried or impossible.
- The upgrade directly removes the bottleneck.

Likely `没必要` case:

- The pain is vague.
- The main reason is freshness, aesthetics, identity, or imagined future productivity.
- The user has not tried cheaper fixes.

## Side project

User: "我想花两个月做一个副业产品，值不值得？"

Likely route:

- `承诺型投入`

Good first question:

```text
先别证明方案，先确认真实目标。

可多选：
A. 我已经看到明确需求，只是还没验证最小成交路径
B. 我主要是想摆脱当前停滞感，想通过做项目找回推进感
C. 我更像是在为“也许以后能用上”的机会提前搭基础设施
其他：请直接说你想解决的结果，以及两个月后什么变化算成功
```

Then ask:

- What is the smallest version that proves demand?
- What exact maintenance burden comes with this?
- If the product gets no users in 30 days, what will have been misjudged?
- Are they willing to do the boring distribution work, not just the building?

## Small purchase

User: "我想买一个 49 元的效率 app 会员，有必要吗？"

Likely route:

- `小而可逆`

Possible `quick exit` response path:

- Ask whether not buying it creates a real short-term loss.
- Ask whether they can cancel or switch easily.
- If both the downside and switching cost are tiny, do not over-analyze.
- If the app mainly represents mood, identity, or procrastination-by-tooling, decide `没必要`.

## Refactor

User: "我想重构我们这个支付模块，有没有必要？"

Likely route:

- `承诺型投入`

Good first question:

```text
先别证明重构方案，先确认现在的真实代价。

可多选：
A. 当前 bug、回归或发布风险已经频繁影响交付
B. 主要是代码难看、命名混乱或工程洁癖带来的不适
C. 已经有明确的新需求，但现有结构真的阻塞实现
其他：请说明最近一次具体事故或被阻塞的真实场景
```

Then ask:

- If only 10% of the code could change, what is the smallest safe cut?
- What cheaper alternatives exist: tests, isolation, adapters, strangler migration?
- If the refactor fails, what delivery cost will remain?
- Is this solving a current bottleneck, or buying the feeling of control?
