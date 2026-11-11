# Portable plugin source / 可移植插件模板

这个目录只保留 plugin.json 元数据模板。Skill 唯一原始版本位于仓库根目录 SKILL.md、agents/、assets/、references/ 和相关 scripts/ 中，不维护重复副本。

## 构建

```bash
python scripts/validate_skill.py
python scripts/build_plugin.py
```

输出：dist/research-paper-mentor-v1.5.0.zip

ZIP 包含根目录 Skill、purpose-first teaching protocol、concept clarity protocol、报告模板和所需 references。

本版本最重要的教学变化是：**先解释为什么需要这个部件，再讲它叫什么、怎么工作。** 对回放等复用机制，先从“前面已经做过什么、后面为什么还要用到、如果重新做会有什么问题”讲起，再核对具体复用了什么以及哪些步骤仍然执行。

插件没有打包本地 MCP 服务和桌面专属钩子。可移植插件源码包不代表用户的 ChatGPT 账号已经安装。导入渠道、手机端可用性、外部代码仓库访问以及执行权限由宿主环境决定。详见 [官方插件说明](https://developers.openai.com/plugins/build/plugins) 与 [ChatGPT 插件帮助](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)。
