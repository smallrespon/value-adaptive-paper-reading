# Architecture / 设计架构

## One canonical Skill / 唯一源码

仓库根目录 `SKILL.md` 是唯一核心指令；`references/` 定义具体工作流；`agents/openai.yaml` 提供 UI 描述；`assets/report-template.md` 作为输出模板；`scripts/repo_inventory.py`、`scripts/validate_report.py` 是可选的只读辅助工具。

所有发布包都由这些文件自动生成，而非单独修改插件版本。`scripts/build_plugin.py` 将它们复制到 ZIP 的 `skills/value-adaptive-paper-reading/` 路径；`mobile-plugin/plugin.json` 是插件元数据模板。

## 阅读流程

1. **原文核查**：识别全文、公式、图表、附录和源码的可访问范围。
2. **论文学术价值与新手学习价值**：P0–P3 推荐优先级，不凭空判断项目相关性。
3. **掌握目标**：分模块设置 M0–M4 和可验证达标标准。
4. **解释深度**：根据重要性、知识依赖和目标，在 D0–D3 中分配篇幅。
5. **证据驱动教学**：前置知识、例子、数学形式、真实论文证据逐层衔接。
6. **代码映射（可选）**：若论文与源码相关且可访问，定位官方实现、记录版本，并按学习价值讲解。
7. **审计与交付**：记录无法读取的内容、未证实的主张、原文位置及自测目标。

## Capability boundaries / 运行边界

- **Skill 指令不等于执行权限。** 需要宿主工具才能获取 PDF、浏览网页、运行 Git 或 Python。
- **可移植插件 ZIP 不等于安装完成。** 用户还需使用宿主支持的渠道安装或通过 Plugin Creator 完成设置。
- **源码静态分析不等于代码已运行。** 默认不运行第三方代码。
- **结构性测试不等于科研正确性。** 仓库检查脚本不会判断 AI 生成报告的公式、数据或结论真伪。

## Versioning

仓库与插件包统一使用公开发行版本，例如 `1.3.0`。改动 Skill 的行为时更新 CHANGELOG；打包不复制永久维护的第二份 Skill。
