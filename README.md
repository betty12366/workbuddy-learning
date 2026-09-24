# workbuddy-learning

统计与数据分析课程的学习仓库，同时承载 WorkBuddy 作业产出（概念学习 Skill + 学习资料）。

## 目录结构

| 目录 | 用途 |
| --- | --- |
| `notes/` | 课程笔记（按章节/主题整理） |
| `homework/` | 课程作业 |
| `data/` | 练习用数据文件 |
| `scripts/` | 练习代码（Python / R 等） |
| `resources/` | 参考资料、拓展阅读 |
| `learning-materials/` | WorkBuddy 作业：学习资料 |
| `python-basics/` | Python 基础语法可运行教材（5 章 + README） |
| `.workbuddy/skills/` | WorkBuddy 作业：Skill 定义 |

## 学习路线

1. 描述性统计：均值、中位数、方差、分布
2. 概率基础：随机变量、常见分布
3. 统计推断：抽样、置信区间、假设检验
4. 相关与回归：线性回归、多元回归
5. 数据可视化：图表类型与适用场景
6. 实践项目：用真实数据完成一次完整分析

## 作业产出

- `.workbuddy/skills/概念学习资料生成器/SKILL.md` —— 概念学习资料生成器 Skill 定义
- `learning-materials/agent.html` —— Agent（智能体）学习资料
- `learning-materials/llm-context.html` —— 大模型上下文（Context）学习资料
- `learning-materials/skill.html` —— Skill（技能）学习资料
- `learning-materials/concept-relationship.md` —— 三者关系说明（含 Mermaid 关系图）

三份学习资料均按「概念学习资料生成器」Skill 的输出结构编写：学习目标、个人解释、核心机制、应用场景、易混淆辨析、自测问题、参考来源。

关系的概括：**上下文是输入信息，Agent 是执行者，Skill 是经验手册。**

## 使用说明

- 每次学习后在 `notes/` 添加或更新笔记
- 作业提交前先在本地 commit，再 push 到 GitHub

## 问题与解决记录

| 问题 | 解决方式 |
|------|---------|
| 电脑未安装 Git，终端无法识别 git 命令 | 访问 git-scm.com 下载安装 Git for Windows，安装后重启终端 |
| GitHub 网页访问超时（ERR_CONNECTION_TIMED_OUT） | 使用 GitHub 个人访问令牌（PAT）通过终端推送，不依赖网页访问 |
| 终端提示「Support for password authentication was removed」 | 使用 PAT 令牌代替密码进行身份验证 |
| WorkBuddy 因网络问题无法直接调用 GitHub API | 由 WorkBuddy 生成文件内容后，通过本地终端配合 PAT 令牌完成推送 |
| HTTPS 推送时 Git Credential Manager 要求 /dev/tty，非交互环境必失败 | 远程地址改用 SSH：`git@github.com:betty12366/workbuddy-learning.git` |
