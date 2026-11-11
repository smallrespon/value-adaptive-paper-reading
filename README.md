# Research Paper Mentor · Value-Adaptive Paper Reading

[English](./README.en.md) · [使用示例](./examples/quick-start.md) · [设计说明](./docs/architecture.md) · [贡献指南](./CONTRIBUTING.md)

> **让 AI 先读论文，再为零基础读者生成有证据、有学习目标、有侧重的中文精读报告。**
>
> **AI reads the paper; you learn from the report.**

这是一个基于 [Agent Skills](https://agentskills.io/) 思路组织的开源论文阅读工作流。默认读者没有科研经验，不绑定个人专业或特定学科。

## 它解决什么问题？

普通 AI 论文总结经常只回答「论文讲了什么」，却没有讲清楚**为什么论文需要某个部件、它解决了什么具体问题，以及它如何接入整个流程**。直接从“回放机制”“策略网络”“调度器”等术语开始，初学者很难理解来龙去脉。

Research Paper Mentor 将论文变成分层教学材料：

**论文全文核查 → 价值评估（P0–P3）→ 掌握目标（M0–M4）→ 讲解深度（D0–D3）→ 先讲问题和目的 → 概念消歧与过程追踪 → 证据追踪的中文精读报告**。

## 功能概览

| 功能 | 说明 |
| --- | --- |
| **价值判断** | 区分领域学术价值和零基础学习价值 |
| **掌握目标** | 为核心方法、公式和辅助知识设置 M0–M4 学习目标与检验标准 |
| **自适应深度** | 高价值概念完整教学，次要背景简述 |
| **目的先行教学** | 先讲整体任务、流程位置、具体痛点、旧方法局限和为什么需要该部件，再引入术语 |
| **概念消歧** | 区分执行者、程序/策略、策略版本、一次调用、动作、执行尝试、数据结构、状态和指标 |
| **过程追踪** | 用同一个例子展示执行者、输入、操作、输出、状态变化和下游影响 |
| **在线/回放对照** | 先解释为什么要复用历史信息，再核对哪些记录被复用、哪些步骤被跳过或重新执行 |
| **证据可追溯** | 标注章节、公式、图表或证明位置，区分作者主张与实际证据 |
| **论文与代码对照** | 有可访问源码时映射公式、函数和数据流；默认只做静态分析 |
| **跨论文/跨学科** | 分析论文关系、先修依赖和不同论文类型 |

## 立即使用：Codex Skill

在支持 Skill 的 Codex 环境中安装到用户级目录（需要本机已安装 Git）：

**macOS / Linux**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME/.agents/skills/value-adaptive-paper-reading"
```

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME\.agents\skills\value-adaptive-paper-reading"
```

在 Codex 中调用：

```text
$value-adaptive-paper-reading
请完整阅读这篇论文，先判断学习价值并生成中文精读报告。
讲每个核心部件时，先讲整体任务、流程走到哪一步、遇到什么具体问题、
为什么需要这个部件，再介绍术语和输入输出。
不要只给部件定义，要讲清楚它为什么出现在这里，以及它让后续步骤能够做什么。
```

仓库公开前，克隆操作需要 GitHub 仓库访问权限。上述命令不会自动安装到 ChatGPT 移动客户端。

## ChatGPT 插件包（Skill-only）

```bash
python scripts/validate_skill.py
python scripts/build_plugin.py
# dist/research-paper-mentor-v1.5.0.zip
```

插件 ZIP 是可移植源码包，不代表已经上架、安装或获得手机端功能授权。宿主环境仍需提供 PDF、Git、浏览器等实际执行能力。

## 报告里有什么？

通常包括阅读决策卡、研究背景、前置知识、核心部件的来龙去脉、概念/角色表、核心方法、逐步运行示例、关键公式、结果证据、局限、掌握目标、自测题和证据索引。结构按论文类型调整。

**这是教学辅助，不是事实担保。** 没有读取的正文、图片或代码必须明确声明；“AI 已讲解”不代表读者已经掌握。论文结论、公式和实验仍应回原文核验。

## 开发与测试

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/build_plugin.py
```

这些检查验证结构与打包，不验证 AI 报告的科研事实正确性。

## 项目结构

```text
SKILL.md
references/              # 价值评估、目的先行、概念消歧、教学和源码阅读规则
assets/report-template.md
agents/openai.yaml
scripts/
mobile-plugin/plugin.json
examples/
tests/
docs/
```

## 参与贡献与开源

- [贡献指南](./CONTRIBUTING.md) · [安全反馈](./SECURITY.md) · [版本记录](./CHANGELOG.md)
- MIT 许可，见 [LICENSE](./LICENSE)；论文、代码、数据集和模型仍适用各自授权条款。
- 开源发布前请核查 [开源检查清单](./docs/open-source-checklist.md)。
- 本项目是独立社区项目，不是 OpenAI 官方产品或官方认证 Skill。
