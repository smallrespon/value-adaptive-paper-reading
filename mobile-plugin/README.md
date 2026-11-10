# Portable plugin source / 可移植插件模板

这个目录只保留 `plugin.json` 元数据模板。**Skill 唯一的原始版本放在仓库根目录 `SKILL.md`、`agents/`、`assets/`、`references/` 和相关 `scripts/` 中。**

为了避免与 Codex Skill 长期不同步，不再在 Git 中维护重复的 `mobile-plugin/skills/` 目录。

## 构建

在仓库根目录执行：

```bash
python scripts/validate_skill.py
python scripts/build_plugin.py
```

输出到 `dist/research-paper-mentor-v1.3.0.zip`，其中包含：

```text
plugin.json
skills/value-adaptive-paper-reading/SKILL.md
skills/value-adaptive-paper-reading/agents/openai.yaml
skills/value-adaptive-paper-reading/references/...
skills/value-adaptive-paper-reading/assets/...
skills/value-adaptive-paper-reading/scripts/...
```

插件没有打包本地 MCP 服务和桌面专属钩子。可移植插件源码包**不代表用户的 ChatGPT 账号已经安装**。导入渠道、手机端可用性、外部代码仓库访问以及执行权限仍由宿主环境决定。详见 [官方插件说明](https://developers.openai.com/plugins/build/plugins) 与 [ChatGPT 插件帮助](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)。

请不要将 ZIP 路径或插件导入能力描述为“所有手机端均支持”或“可自动克隆代码”。
