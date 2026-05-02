# Payoff Evaluator

`payoff-evaluator` 是一个 Codex skill，用来反附和地评估一件事、一个计划、一次购买或一段投入有没有必要。

它的核心立场是：计划必须证明自己的必要性。模型不能默认附和用户，也不能替用户补理由。它会先做 `决策分流`，再用 `measure`、`reversibility`、`inversion`、`commitment` 这些镜头拆开判断，主动寻找反方证据、替代方案和失败路径，最后给出 `必要` 或 `没必要` 的二选一结论。

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

## Cursor（项目级 Skill）

在本仓库内用 Cursor 打开项目时，Agent 会从 `.cursor/skills/payoff-evaluator/` 加载同一套流程（含 `references/evaluation-framework.md` 与 `references/examples.md`）。无需再链到全局 `~/.cursor/skills/`；克隆本仓库即可在团队间共享。

若你改动了根目录下的 `payoff-evaluator/`，请同步更新 `.cursor/skills/payoff-evaluator/` 中对应文件，避免 Cursor 与 Codex 安装源脱节。

仓库内提供了同步脚本：

```bash
python3 scripts/sync_skill_copies.py
```

它会把根目录下的 `payoff-evaluator/` 完整复制到 `.cursor/skills/payoff-evaluator/`。

仓库内还提供了完整自检脚本：

```bash
python3 scripts/validate_skill_repo.py
```

它会依次执行同步、副本一致性测试、仓库单测，以及 `skill-creator` 的 `quick_validate.py`。

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

## 升级后的判断结构

这个 skill 现在保留“必要 / 没必要”的定位，但判断过程更稳：

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

## 交互方式

- 每轮只问一个关键问题，最多追问 7 轮。
- 对 `小而可逆` 的事优先走 `quick exit`，通常 0-2 个问题就收束。
- 如果不是明确的二选一、主因排序或最终确认题，默认按多选事实题处理。
- 当前 Plan mode 的 `request_user_input` 只有单选加 `Other`，不支持多选，所以多选事实题默认使用 Markdown 多选格式。
- 结构化单选 UI 只留给明确单选题；如果界面自动显示“推荐”标记，skill 会在题干里明确让用户忽略它。
- 在结构化 UI 下不再额外伪造“自定义”选项，直接依赖系统自带的 `Other...`。
- 最终必须给出 `结论：必要` 或 `结论：没必要`。

## 输出结构

默认输出会包含这些部分：

- `结论：必要 / 没必要`
- `决策分流`
- `镜头摘要`
- `最强反方证据`
- `关键理由`
- `最大不确定性`
- `最早的打脸信号`
- `下一步行动`

## 为什么有这个项目

大模型很擅长获取信息和整合信息，但在个人决策里容易变成附和型助手：用户提出一个计划，模型会顺着计划补理由，最后给出模棱两可或偏支持的回答。

这个 skill 的目标是反过来做：先要求计划证明自己的必要性。它会主动寻找反方证据、低成本替代方案、机会成本和失败路径，帮助用户避免把真实目的包装成一个过大的计划，也就是避免“为了醋包饺子”。

## 行为原则

- 不默认支持用户的原始计划。
- 必要性由计划方证明。
- 先分流，再决定要不要深挖。
- 判断前必须执行反附和检查。
- 高 `measure` 和低 `reversibility` 的决策值得更重的审查。
- 对长期投入型问题，必须过 `commitment` 检查。
- 外部搜索不是每次强制联网，而是先内部反证，必要时搜索反面案例。
- 开心、审美、身份感、新鲜感可以作为偏好背景，但不能单独证明“必要”。

## 目录结构

```text
payoff-evaluator/              # Codex 安装源（软链接/复制目标）
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── evaluation-framework.md
    └── examples.md

.cursor/skills/payoff-evaluator/   # Cursor 项目级 Agent Skill（与上保持内容一致）
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── evaluation-framework.md
    └── examples.md

scripts/
├── sync_skill_copies.py
└── validate_skill_repo.py
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
