# Payoff Evaluator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![linuxdo](https://img.shields.io/badge/linuxdo-skill-blue?style=flat)](https://linux.do)

**A platform-neutral skill / reusable prompt pack for anti-sycophancy necessity review.**

`payoff-evaluator` 用来判断一件事、一个计划、一次购买或一段投入到底是不是“有必要”，而不是顺着用户的原始想法补理由。

它的核心立场很简单：

- 计划必须证明自己的必要性
- 模型不能默认附和
- 模型不能替用户把欲望包装成必要性
- 最终必须收敛到 `结论：必要` 或 `结论：没必要`

这个仓库刻意保持平台中立，所以公开内容只保留真正给模型使用的 skill 本体和参考资料，不包含供应商专属元数据、测试目录或本地维护脚本。

## Key Features

| Feature | Description |
|---------|-------------|
| Anti-sycophancy review | 先找为什么可能没必要，而不是先替计划辩护 |
| Necessity-only output | 只做 `必要 / 没必要` 判断，不做 weighted A-vs-B 比较 |
| Decision routing | 先分流为 `小而可逆`、`购买/支出`、`承诺型投入` |
| Layered references | 主规则在 `SKILL.md`，详细镜头、问法、搜索策略、例子按需读取 |
| Cross-platform packaging | 可作为 skill 目录、custom instruction、system prompt 或 reusable prompt 使用 |

## Supported Platforms

只要平台支持下面任一方式，就可以使用这份 skill：

- 可发现的 skill / agent / command 目录
- 可复用的 system prompt / custom instruction / reusable prompt
- 可按需追加参考文档作为上下文

这意味着它可以被接入 Codex、Cursor、Claude，或其他支持类似能力的 agent 平台。

## Installation

### 方式一：作为目录式 skill 接入

如果你的平台支持“把一个目录当成 skill / prompt 包”加载，直接把 `payoff-evaluator/` 放到对应目录即可。

推荐用软链接，后续更新更简单：

```bash
git clone https://github.com/QuarterNomad/payoff.git
mkdir -p /path/to/your/skills
ln -s "$(pwd)/payoff/payoff-evaluator" /path/to/your/skills/payoff-evaluator
```

### 方式二：作为可复用提示词接入

如果你的平台不支持目录式 skill，只支持一段可复用提示词：

1. 把 `payoff-evaluator/SKILL.md` 作为主提示词模板。
2. 在需要时再附带 `payoff-evaluator/references/` 下的参考文档。
3. 让模型按 `SKILL.md` 中写的规则决定什么时候读取额外 reference。

## Usage

如果平台支持显式调用 skill，可以这样写：

```text
Use $payoff-evaluator to judge: 我想买一台新电脑，有没有必要？
```

如果平台不支持显式 skill 调用，直接自然语言提问也可以：

```text
我想花两个月做一个副业产品，值不值得？
```

适合的问题包括：

- "我想买一台新电脑，有没有必要？"
- "我想花两个月做一个副业产品，值不值得？"
- "我想重构某个系统模块，有没有必要？"
- "我想报名一个课程，是否值得投入？"
- "这个项目是不是为了醋包饺子？"

## Evaluation Workflow

这个 skill 保留“必要 / 没必要”的定位，但判断过程更稳：

1. `决策分流`
   - 先判断是 `小而可逆`、`购买/支出`，还是 `承诺型投入`。
2. `quick exit`
   - 对低成本、低影响、可逆的小决策，不做冗长访谈，快速给判断。
3. `四个判断镜头`
   - `measure`：这件事会影响多久、多频繁。
   - `reversibility`：做错以后能不能撤回，切换成本有多高。
   - `inversion`：从失败、后悔、误判路径反推。
   - `commitment`：你是否真的愿意承受它对应的长期代价和苦。
4. `反附和检查`
   - 不替用户补理由，先找为什么它可能没必要。
5. `强制结论`
   - 最终仍然只给 `结论：必要` 或 `结论：没必要`。

## Interaction Rules

- 每轮只问一个关键问题，最多追问 7 轮。
- 对 `小而可逆` 的事优先走 `quick exit`，通常 0-2 个问题就收束。
- 如果不是明确的二选一、主因排序或最终确认题，默认按多选事实题处理。
- 如果平台提供真正的多选结构化输入，优先使用它。
- 如果平台只有单选加 `Other`，那它只适合明确单选题；多选事实题改用 Markdown 多选格式。
- 不额外伪造“自定义”选项，直接依赖平台原生的 `Other...` 即可。
- 如果界面会自动显示“推荐”标记，题干里应明确让用户忽略它。
- 最终必须给出 `结论：必要` 或 `结论：没必要`。

## Output Shape

默认输出包含这些部分：

- `结论：必要 / 没必要`
- `决策分流`
- `镜头摘要`
- `最强反方证据`
- `关键理由`
- `最大不确定性`
- `最早的打脸信号`
- `下一步行动`

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

这个仓库当前不包含：

- 供应商专属 `agents/openai.yaml` 之类的接口元数据
- 公共仓库里的测试目录和维护脚本
- 平台绑定的安装器、登录器或本地状态管理
- 用于 A-vs-B 方案权重比较的决策框架

## Update

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

MIT License - see [LICENSE](LICENSE) file for details.

---

本项目支持 [LINUX DO](https://linux.do) 社区
