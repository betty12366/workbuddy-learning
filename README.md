# workbuddy-learning

WorkBuddy 学习作业仓库：概念学习 Skill + 三份学习资料。

## 目录结构

```
.workbuddy/
  skills/
    概念学习资料生成器/SKILL.md   # Skill 定义文件
learning-materials/
  agent.html                     # Agent（智能体）学习资料
  llm-context.html               # 大模型上下文（Context）学习资料
  skill.html                     # Skill（技能）学习资料
  concept-relationship.md        # 三者关系说明（含 Mermaid 关系图）
```

## 说明

- 三份学习资料均按照「概念学习资料生成器」Skill 的输出结构编写：学习目标、个人解释、核心机制、应用场景、易混淆辨析、自测问题、参考来源。
- `concept-relationship.md` 用一句话概括三者关系：**上下文是"输入信息"，Agent 是"执行者"，Skill 是"经验手册"**。
## 问题与解决记录

| 问题 | 解决方式 |
|------|---------|
| 电脑未安装 Git，终端无法识别 git 命令 | 访问 git-scm.com 下载安装 Git for Windows，安装后重启终端 |
| GitHub 网页访问超时（ERR_CONNECTION_TIMED_OUT） | 使用 GitHub 个人访问令牌（PAT）通过终端推送，不依赖网页访问 |
| 终端提示“Support for password authentication was removed” | 使用 PAT 令牌代替密码进行身份验证 |
| WorkBuddy 因网络问题无法直接调用 GitHub API | 由 WorkBuddy 生成文件内容后，通过本地终端配合 PAT 令牌完成推送 |
