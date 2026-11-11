# Research Paper Mentor · Value-Adaptive Paper Reading

[English](./README.en.md) · [使用示例](./examples/quick-start.md) · [设计说明](./docs/architecture.md) · [贡献指南](./CONTRIBUTING.md)

> **让 AI 先读论文，再为零基础读者生成有证据、有学习目标、有侧重的中文精读报告。**
>
> **AI reads the paper; you learn from the report.**

这是一个基于 [Agent Skills](https://agentskills.io/) 思路组织的、可用于兼容 Skill 运行环境的开源论文阅读工作流。它不绑定个人专业、历史聊天记录或特定学科；默认读者没有科研经验。

## 它解决什么问题？

普通 AI 论文总结经常只回答「论文讲了什么」，却不告诉读者这篇论文**为什么值得学、应该学到什么程度、哪些地方需要深入**，也容易把术语、角色和实际执行过程讲混。

Research Paper Mentor 将一份论文变成分层教学材料：

**论文全文核查 → 价值评估（P0–P3）→ 掌握目标（M0–M4）→ 讲解深度（D0–D3）→ 概念消歧与过程追踪 → 证据追踪的中文精读报告**。

## 功能概览

| 功能 | 说明 |
| --- | --- |
| **价值判断** | 区分领域学术价值和零基础学习价值；没有提供课题目标就不猜测项目相关性 |
| **掌握目标** | 为核心方法、重要公式和辅助知识分别设置 M0–M4 学习目标与检验标准 |
| **自适应深度** | 高价值概念完整教学，次要背景简述；避免平均分配篇幅 |
| **零基础教学** | 前置知识、研究动机、直观例子、数学细节、真实论文中的作用逐层衔接 |
| **概念消歧** | 明确区分执行者、程序/策略、策略版本、一次调用、动作、执行尝试、数据结构、状态和指标 |
| **过程追踪** | 用同一个具体例子展示每一步的执行者、输入、操作、输出、状态变化和下一步可见信息 |
| **在线/回放对照** | 说明真实执行与历史回放中哪些模型、评估器或工具会被调用，哪些结果只是读取/揭示 |
| **证据可追溯** | 标注章节、公式、图表或证明位置，并区分作者主张与实际证据 |
| **论文与代码对照** | 有可访问的相关源码时，按需对应公式、函数、数据流和实现差异；默认只做静态分析 |
| **多篇论文学习地图** | 分析论文间关系、先修依赖、阅读顺序和学习优先级 |
| **跨学科适配** | 方法、理论、实验、综述、数据集、系统、定性等不同论文类型分别处理 |

## 立即使用：Codex Skill

在支持 Skill 的 Codex 环境中安装到用户级目录（需要本机已安装 Git）：

**macOS / Linux**

\`\`\`bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME/.agents/skills/value-adaptive-paper-reading"
\`\`\`

**Windows PowerShell**

\`\`\`powershell
New-Item -ItemType Directory -Force "$HOME\\.agents\\skills" | Out-Null
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME\\.agents\\skills\\value-adaptive-paper-reading"
\`\`\`

如果没有自动出现，重启 Codex，然后使用：

\`\`\`text
$value-adaptive-paper-reading
请完整阅读这篇论文，先判断它对零基础读者的学习价值，
为不同内容设置掌握目标，并按重要性生成有原文依据的中文精读报告。
讲核心方法时，先区分对象、角色、程序、动作、数据结构、状态和指标，
再用一个具体例子逐步展示输入、执行者、输出和状态变化。
如果有官方源码，请对应讲解核心公式、训练过程和函数实现。
\`\`\`

仓库公开前，克隆操作需要 GitHub 仓库访问权限。上述命令不会自动安装到 ChatGPT 移动客户端。

## ChatGPT 插件包（Skill-only）

本仓库同时提供**可生成的可移植插件 ZIP**，并使用**同一份根目录 Skill**，不再维护两份独立指令。

\`\`\`bash
python scripts/validate_skill.py
python scripts/build_plugin.py
# 输出：dist/research-paper-mentor-v1.4.0.zip
\`\`\`

插件包包含根目录 Skill 和概念消歧协议。**ZIP 是插件源码包，不等于已经上架、已安装或获得手机端功能授权。** 实际导入、安装和运行需要你的 ChatGPT 账号或工作区支持相应流程。

插件不内置 MCP、后台服务器或桌面依赖；Git 克隆、执行 Python、解析 PDF 等能力仍取决于实际宿主环境提供的工具。见 [插件说明](./mobile-plugin/README.md)。

## 报告里有什么？

通常包括阅读决策卡、论文全局导读、必要前置知识、核心概念与角色表、问题链与贡献、核心方法、逐步运行示例、关键公式、证据与实验、局限、掌握目标、自测题、术语表和覆盖审计。结构会随论文类型变化，不强制每篇论文都出现算法或实验。

**这是教学辅助，不是事实担保。** 没有读取的正文、图片或代码必须明确声明；“AI 已讲解”不代表读者已经掌握。论文中的结论、公式和实验仍应回原文核验。

## 开发与测试

不需要第三方 Python 包：

\`\`\`bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/build_plugin.py
\`\`\`

这类检查主要验证文件结构、引用路径、插件封装和部分脚本行为，**不会验证 AI 读论文的事实正确性或学习效果**。

## 项目结构

\`\`\`text
SKILL.md                 # 唯一的 Skill 核心指令（原始单一事实源）
references/              # 价值评估、概念消歧、掌握目标、教学和源码阅读规则
assets/report-template.md
agents/openai.yaml        # Codex / Skill 界面描述
scripts/                  # 只读工具、结构检查、插件打包
mobile-plugin/plugin.json # 可移植插件清单模板
examples/                 # 实际调用示例
tests/                    # 结构与打包测试
docs/                     # 架构与发布检查
\`\`\`

## 参与贡献与开源

- [贡献指南](./CONTRIBUTING.md) · [安全反馈](./SECURITY.md) · [版本记录](./CHANGELOG.md)
- 开源协议：**MIT**，见 [LICENSE](./LICENSE)。使用时仍应遵守论文、代码、数据集和模型各自的授权条款。
- 当前仓库公开发布前请核查 [开源检查清单](./docs/open-source-checklist.md)。
- 本项目是独立的社区项目，**不是 OpenAI 官方产品或官方认证 Skill**。

欢迎提交 Issue 或 Pull Request，尤其欢迎提供可复现、附原文位置的论文精读质量案例。
