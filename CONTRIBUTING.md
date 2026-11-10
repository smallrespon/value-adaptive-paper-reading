# Contributing / 贡献指南

感谢你愿意改进 Research Paper Mentor。欢迎 Issue、Pull Request、文档修订和可复现的精读质量案例。

## 建议的贡献方向

- 更清楚、可验证的论文价值与掌握目标评价方法。
- 从零基础到数学形式化之间的循序渐进教学案例。
- PDF/公式/图表、论文与源码对应分析中的准确性防护。
- 不同学科、论文类型的高质量适配。
- 对插件打包、兼容性与说明文档的改善。

## 提交变更

1. 先搜索是否已有相关 Issue/PR，避免重复工作。
2. Fork 仓库并创建功能分支。
3. 保持 `SKILL.md` 作为唯一核心 Skill 来源；**不要直接提交复制版** `mobile-plugin/skills/...`。
4. 修改时尽量明确意图、错误案例和预期行为；不要上传有版权限制的整篇论文或未获授权的源码。
5. 执行以下本地检查：

   ```bash
   python scripts/validate_skill.py
   python -m unittest discover -s tests -v
   python scripts/build_plugin.py
   ```

6. PR 中说明行为变化、验证方式、影响的文件和仍未解决的问题。

## 报告质量反馈

如果某份报告编造公式、误解图表或遗漏重要方法，请提供可公开分享的论文链接、对应页码/章节、期望结论，以及 AI 报告的最小出错片段。请勿提交私人文件或访问密钥。

## 代码安全

本仓库的 `scripts/repo_inventory.py` 只生成文件清单，不执行第三方仓库代码。请勿向普通论文分析工作流加入自动执行未知项目安装脚本、下载敏感数据或泄露运行环境信息的步骤。敏感漏洞请参考 [SECURITY.md](./SECURITY.md)。
