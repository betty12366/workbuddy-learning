# Agent、上下文、Skill 三者关系说明

## 一句话概括

**上下文是"输入信息"，Agent是"执行者"，Skill是"经验手册"。**

---

## 关系图（Mermaid）

```mermaid
graph TD
    A[用户输入/环境信息] --> B[上下文 Context]
    B --> C[Agent 智能体]
    D[Skill 技能库] --> C
    C --> E[执行动作/生成结果]
    E --> F[反馈/经验]
    F --> D