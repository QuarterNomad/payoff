# Payoff Evaluator

`payoff-evaluator` 是一个 Codex skill，用来反附和地评估一件事、一个计划、一次购买或一段投入有没有必要。

它的核心立场是：计划必须证明自己的必要性。模型不能默认附和用户，也不能替用户补理由。它会先追问真实目的、收益、代价和替代方案，再主动寻找反方证据，必要时搜索失败案例或反面观点，最后给出 `必要` 或 `没必要` 的二选一判断。

## 快速安装

推荐用软链接安装，后续只需要 `git pull` 就能更新：

```bash
git clone https://github.com/QuarterNomad/payoff.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/payoff/payoff-evaluator" ~/.codex/skills/payoff-evaluator
```

如果不想使用软链接，也可以复制 skill 目录：

```bash
git clone https://github.com/QuarterNomad/payoff.git
mkdir -p ~/.codex/skills
cp -R payoff/payoff-evaluator ~/.codex/skills/
```

安装后重启或刷新 Codex，使 skill 被重新发现。

## 如何使用

在 Codex 中直接调用：

```text
Use $payoff-evaluator to judge: 我想买一台新电脑，有没有必要？
```

也可以用更自然的方式提问：

```text
我想花两个月做一个副业产品，值不值得？
```

适合的问题包括：

- "我想买一台新电脑，有没有必要？"
- "我想花两个月做一个副业产品，值不值得？"
- "我想重构某个系统模块，有没有必要？"
- "我想报名一个课程，是否值得投入？"
- "这个项目是不是为了醋包饺子？"

## 交互方式

- 每轮只问一个关键问题，最多追问 7 轮。
- 事实收集题允许多选，不标推荐，避免污染用户回答。
- 主因或优先级题才使用单选。
- 如果当前环境支持无推荐、多选、自定义输入的结构化控件，优先使用结构化控件。
- 如果当前环境只能显示带推荐的单选控件，事实收集题会退化成 Markdown 多选格式。
- 最终必须给出 `结论：必要` 或 `结论：没必要`。

## 为什么有这个项目

大模型很擅长获取信息和整合信息，但在个人决策里容易变成附和型助手：用户提出一个计划，模型会顺着计划补理由，最后给出模棱两可或偏支持的回答。

这个 skill 的目标是反过来做：先要求计划证明自己的必要性。它会主动寻找反方证据、低成本替代方案、机会成本和失败路径，帮助用户避免把真实目的包装成一个过大的计划，也就是避免“为了醋包饺子”。

## 行为原则

- 不默认支持用户的原始计划。
- 必要性由计划方证明。
- 判断前必须执行反附和检查。
- 外部搜索不是每次强制联网，而是先内部反证，必要时搜索反面案例。
- 开心、审美、身份感、新鲜感可以作为偏好背景，但不能单独证明“必要”。

## 目录结构

```text
payoff-evaluator/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── evaluation-framework.md
```

## 更新

如果使用软链接安装：

```bash
cd payoff
git pull
```

如果使用复制安装：

```bash
cd payoff
git pull
rm -rf ~/.codex/skills/payoff-evaluator
cp -R payoff-evaluator ~/.codex/skills/
```
