# Research Paper Mentor · Value-Adaptive Paper Reading

> 一个以**零科研基础读者**为默认对象、让 AI 主导阅读原始论文并生成中文教学型精读报告的 Codex Skill。

## 特点

- **先评估价值，再决定精读深度**：分别评估论文的学术价值与零基础学习价值，给出 P0–P3 阅读优先级。
- **明确掌握目标**：按照 M0–M4 等级为论文的不同部分设定可验证的学习目标。
- **自适应讲解**：按照 D0–D3 讲解深度，把篇幅放在值得深入理解的背景、核心机制、公式、论证和证据上。
- **小白友好，保持严谨**：先解释必要概念，再解释原理、公式、算法和实验，不默认任何专业背景。
- **证据可追溯**：区分论文中的原始陈述、实验或证明结果、AI 的解释与独立推测，注明章节、公式、图表等位置。
- **配套代码精读**：当论文存在可访问且可信的官方仓库时，可定位代码、建立论文公式与源码的对应关系，并按价值决定讲解深度。默认仅静态分析，不自动执行不可信代码或训练。
- **多篇论文学习地图**：评估论文间的关系、先修知识、推荐顺序与不同的掌握目标。

## 安装

将本仓库目录放到 Codex 用户级 Skills 目录（通常为 `~/.agents/skills/value-adaptive-paper-reading`）。Windows PowerShell 可使用：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/smallrespon/value-adaptive-paper-reading.git "$HOME\.agents\skills\value-adaptive-paper-reading"
```

> 该仓库计划设为私有。请先在 GitHub 登录有访问权限的账号，并确保 Git 的 GitHub 身份验证可用。创建仓库之前，上面的 `git clone` 命令无法运行。

## 使用方式

在 Codex 中调用：

```text
$value-adaptive-paper-reading
请阅读这篇论文，先评估它对零基础读者的学习价值与阅读优先级，
再制定掌握目标，按照价值自适应分配深度，生成完整中文教学型精读报告。
```

多篇论文：

```text
$value-adaptive-paper-reading
这些是待学习的论文，请先分析它们之间的关系，推荐阅读顺序，
说明每一篇值得掌握到什么程度，再针对核心论文生成深度精读报告。
```

## 文件结构

```text
SKILL.md                         # 主要技能指令
agents/openai.yaml                # 界面元数据
references/                      # 评估、教学、证据、代码精读等详细规则
assets/report-template.md        # 中文报告模板
scripts/validate_report.py       # 检查报告章节完整性（不校验事实）
scripts/repo_inventory.py         # 代码仓库静态清单工具
```

## 安全与限制

- 无法访问的全文、附录或源码必须如实标注，不能假装读过。
- 拉取代码取决于运行环境的网络访问、Git 工具和仓库权限。
- 不会默认安装未知依赖、执行未知项目代码或启动训练任务。
- 自动生成的评价和学习时间估计是判断与建议，不等于客观测量。
- 报告中出现的知识点不等于读者已经掌握；掌握程度必须经过实际验证。

## 版本

当前准备上传的是 **v1.1**，包含代码辅助精读模块。
