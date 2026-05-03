# Payoff Evaluator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![linuxdo](https://img.shields.io/badge/linuxdo-skill-blue?style=flat)](https://linux.do)

**A platform-neutral skill pack for one job: deciding whether something is actually necessary.**

> Many assistants help users justify a plan.  
> `payoff-evaluator` does the opposite: it asks whether the plan is needed at all.

`payoff-evaluator` 是一个反附和的决策审查 skill。  
它不负责帮用户把欲望包装成“刚需”，而是要求一个计划先证明自己为什么有必要。

无论用户想买设备、重构系统、做副业、报课程，还是准备投入一段长期精力，这个 skill 都会先问：

- 这件事真的在解决当前问题吗？
- 不做它，真实损失到底是什么？
- 有没有更小、更便宜、更可逆的做法？
- 这是不是典型的“为了醋包饺子”？

最终它必须收敛到一个明确判断：

- `结论：必要`
- `结论：没必要`

## Why This Exists

很多“值不值得”“要不要做”的讨论，最后都会滑向两种坏结果：

- 模型默认顺着用户说话，先替计划找优点
- 用户其实还没证明需求，就已经开始买工具、搭系统、做大方案

`payoff-evaluator` 的目标不是给出温和、平衡、面面俱到的陪聊式建议，而是提供一次有摩擦的必要性审查。

## What Makes It Different

和普通的决策建议 prompt 相比，它有几个很刻意的限制：

- **反附和优先**：先找“不必要”的证据，再看是否值得通过。
- **只做必要性判断**：不做 A vs B 打分表，不做复杂权重模型。
- **先分流再深挖**：把问题区分成 `小而可逆`、`购买/支出`、`承诺型投入`。
- **对小事快速收束**：不把 49 元会员、一次小工具购买聊成一场人生咨询。
- **对长期投入更苛刻**：项目、重构、副业、学习计划必须经得起长期代价和失败反推。

## Good Fit

这个 skill 适合处理下面这类问题：

- “我想买一台新电脑，有没有必要？”
- “我想花两个月做一个副业产品，值不值得？”
- “我想重构这个模块，现在做是不是过度设计？”
- “我想报一个课程，是否值得投入？”
- “这个方案是不是为了醋包饺子？”

如果你的目标是做**方案比较**、**优先级排序**、**路线打分**，那这不是最合适的 prompt。  
它只回答一个问题：**这件事现在到底有没有必要。**

## Quick Example

用户输入：

```text
我想重构我们这个支付模块，有没有必要？
```

这个 skill 不会直接顺着“重构”往下展开，而会先压回真实代价：

```text
先别证明重构方案，先确认现在的真实代价。

可多选：
A. 当前 bug、回归或发布风险已经频繁影响交付
B. 主要是代码难看、命名混乱或工程洁癖带来的不适
C. 已经有明确的新需求，但现有结构真的阻塞实现
其他：请说明最近一次具体事故或被阻塞的真实场景
```

这就是它的核心风格：  
**先确认是不是在解决真实问题，而不是先帮用户把方案讲圆。**

## Quick Start

### Option 1: Use it as a skill directory

如果你的平台支持把一个目录作为 skill / prompt 包加载，直接接入 `payoff-evaluator/` 即可。

```bash
git clone https://github.com/QuarterNomad/payoff.git
mkdir -p /path/to/your/skills
ln -s "$(pwd)/payoff/payoff-evaluator" /path/to/your/skills/payoff-evaluator
```

### Option 2: Use it as a reusable prompt

如果你的平台不支持目录式 skill，只支持复用提示词：

1. 使用 `payoff-evaluator/SKILL.md` 作为主提示词。
2. 按需附加 `payoff-evaluator/references/` 下的参考文档。
3. 让模型根据 `SKILL.md` 中的规则决定何时读取额外 reference。

## How To Invoke

如果平台支持显式 skill 调用：

```text
Use $payoff-evaluator to judge: 我想买一台新电脑，有没有必要？
```

如果平台不支持显式调用，直接自然语言提问也可以：

```text
我想花两个月做一个副业产品，值不值得？
```

## How It Works

完整规则写在 `payoff-evaluator/SKILL.md`，但它的骨架很简单：

1. 先识别用户到底要评估什么计划。
2. 把问题分流为 `小而可逆`、`购买/支出`、`承诺型投入`。
3. 只问最能降低不确定性的关键问题，每轮只问 1 个，最多 7 轮。
4. 先做反附和检查，再强制收敛到 `必要` 或 `没必要`。

更细的配套文档分别放在：

- `references/evaluation-framework.md`：判断框架与输出模板
- `references/interview-strategy.md`：追问策略与题型规则
- `references/search-strategy.md`：什么时候该联网、该搜什么
- `references/examples.md`：典型场景示例

## Repository Structure

```text
payoff/
├── payoff-evaluator/
│   ├── SKILL.md
│   └── references/
│       ├── evaluation-framework.md
│       ├── interview-strategy.md
│       ├── search-strategy.md
│       └── examples.md
├── LICENSE
└── README.md
```

## Boundaries

这个仓库当前刻意不包含：

- 供应商专属元数据或平台绑定配置
- 公共仓库里的测试目录和维护脚本
- 安装器、登录器或本地状态管理
- 用于 A-vs-B 权重比较的决策框架

换句话说，这里公开的是**真正给模型使用的 skill 本体**，而不是某个平台私有的一整套运行时包装。

## Updating

如果你是用软链接接入：

```bash
cd payoff
git pull
```

如果你是复制目录接入：

```bash
cd payoff
git pull
rm -rf /path/to/your/skills/payoff-evaluator
cp -R payoff-evaluator /path/to/your/skills/
```

## License

MIT License. See [LICENSE](LICENSE).

---

本项目支持 [LINUX DO](https://linux.do) 社区。
