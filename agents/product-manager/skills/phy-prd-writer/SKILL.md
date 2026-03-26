---
name: prd-writer
description: "PRD creation assistant with two modes: (1) Multi-turn Q&A for unclear requirements, (2) Auto mode for self-reasoning and one-shot generation. Triggers on 'write PRD', 'create PRD', 'new feature', 'product requirements', '/prd', or 'autonomous PRD'."
metadata: {"openclaw": {"emoji": "📋", "os": ["darwin", "linux"]}}
---

# PRD Writer - Dual Mode Requirements Gathering

## Overview

Two modes available:

### Mode 1: Interactive (Multi-turn Q&A)
Guide users through creating a professional PRD by asking focused questions one at a time. Use when requirements are unclear or user wants to explore.

### Mode 2: Autonomous (Self-Reasoning)
Agent reasons through all phases internally, makes educated assumptions, and outputs a complete PRD in one shot. Use when user wants speed or has provided sufficient context upfront.

**Mode Selection:**
- If user says "autonomous", "auto", "自己生成", "快速" → Use Autonomous Mode
- If user provided rich context upfront (problem, users, goals, features) → Use Autonomous Mode
- Otherwise → Use Interactive Mode

## Autonomous Mode Workflow (Multi-Step Internal Reasoning)

When in Autonomous Mode, follow this **multi-step internal reasoning process**:

### Step 1: Extract Available Information (思考第 1 步)
Parse user's initial request for:
- Problem statement (explicit or implied)
- Target users
- Business context
- Any mentioned features or constraints
- Timeline or deadlines

**Output format (internal note)**:
```
【信息提取】
✅ 已提供：[列出用户明确给的信息]
❓ 缺失：[列出需要推断的信息]
```

### Step 2: Phase-by-Phase Reasoning (思考第 2-7 步)

For each of the 6 phases, reason internally:

```
【Phase 1: 问题发现】
- 核心问题是什么？→ [推理]
- 为什么现在重要？→ [推理]
- 现有解决方案？→ [推理]
- ⚠️ 不确定点：[标记]

【Phase 2: 用户与市场】
- 目标用户？→ [推理]
- 使用场景？→ [推理]
- 市场规模？→ [推理]
- ⚠️ 不确定点：[标记]

【Phase 3: 成功指标】
- 什么指标重要？→ [推理]
- 合理目标值？→ [推理]
- ⚠️ 不确定点：[标记]

【Phase 4: 范围定义】
- 核心功能？→ [推理]
- 不做啥？→ [推理]
- 未来功能？→ [推理]
- ⚠️ 不确定点：[标记]

【Phase 5: 约束与依赖】
- 技术约束？→ [推理]
- 依赖方？→ [推理]
- 时间线？→ [推理]
- ⚠️ 不确定点：[标记]

【Phase 6: 优先级】
- MoSCoW 分类？→ [推理]
- ⚠️ 不确定点：[标记]
```

### Step 3: Self-Challenge (思考第 8 步 - 自我质疑)

Before generating PRD, challenge your assumptions:

```
【自我质疑】
1. 这个假设合理吗？有没有反例？
2. 有没有遗漏重要干系人？
3. 时间线是否现实？
4. 成功指标可测量吗？
5. 最大风险是什么？
```

### Step 4: Generate Complete PRD (输出)

Output a full PRD document with:
- ✅ Confirmed information (from user input)
- ⚠️ Assumed information (clearly marked with reasoning)
- ❓ Open questions (need user confirmation)

**Include reasoning summary at the top**:

```markdown
## 🧠 生成说明

**生成模式**: 自主多步推理 (Autonomous Multi-Step Reasoning)

**推理过程**:
1. 问题发现 → [简述推理]
2. 用户分析 → [简述推理]
3. 指标定义 → [简述推理]
4. 范围界定 → [简述推理]
5. 约束识别 → [简述推理]
6. 优先级排序 → [简述推理]

**关键假设**:
- ⚠️ [假设 1] — 基于 [推理依据]
- ⚠️ [假设 2] — 基于 [推理依据]
```

### Step 5: Append Confirmation Checklist

At the end of the PRD, add:

```markdown
---

## ⚠️ 需要确认的事项

以下基于假设生成，请确认或修正：

| 编号 | 假设内容 | 推理依据 | 建议确认方式 |
|------|----------|----------|--------------|
| A1 | ... | ... | 与 XX 确认 |
| A2 | ... | ... | 数据验证 |

## ❓ 开放问题

| 问题 ID | 问题描述 | 影响范围 | 建议负责人 |
|---------|----------|----------|------------|
| Q-001 | ... | ... | ... |

## 📋 下一步建议

1. 确认上述假设（A1-An）
2. 回答开放问题（Q-001~Q-n）
3. 与干系人评审 PRD
4. 进入技术设计阶段
```

## Mode Selection Logic

```
IF user request contains:
  - "autonomous", "auto", "自己生成", "快速", "一次性"
  OR user provided >3 key details upfront (problem, users, goals, features)
THEN → Use Autonomous Mode

ELSE → Use Interactive Mode (ask questions one at a time)
```

## Interactive Mode: The Process

### Phase 1: Problem Discovery (2-3 questions)

Start by understanding the core problem:

1. **Problem Statement**: "What specific problem are you trying to solve? Describe the user pain point."
2. **Why Now**: "Why is this important to solve now? What happens if we don't solve it?"
3. **Existing Solutions**: "How are users currently solving this problem (workarounds, competitors)?"

### Phase 2: User & Market (2-3 questions)

4. **Target Users**: Ask who the primary users are. Offer common persona types:
   - End consumers (B2C)
   - Business users (B2B)
   - Internal team members
   - Developers/Technical users
   - Other (specify)

5. **User Context**: "In what context will users encounter this? (e.g., mobile on-the-go, desktop at work, specific workflow)"

6. **Market Size/Impact**: "How many users will this affect? Is this a core feature or nice-to-have?"

### Phase 3: Success Metrics (1-2 questions)

7. **Definition of Success**: Ask what success looks like. Offer metric types:
   - User engagement (DAU, retention, time spent)
   - Business metrics (revenue, conversion, cost reduction)
   - Technical metrics (performance, reliability, error rates)
   - User satisfaction (NPS, CSAT, support tickets)

8. **Specific Targets**: "What specific numbers would indicate success? (e.g., 'reduce load time to <2s', 'increase conversion by 15%')"

### Phase 4: Scope Definition (2-3 questions)

9. **Core Features**: "What are the MUST-have features for v1? List the absolute minimum for launch."

10. **Out of Scope**: "What should we explicitly NOT build in this phase? (This prevents scope creep)"

11. **Future Considerations**: "What features might come in v2/v3? (Park these for later)"

### Phase 5: Constraints & Dependencies (1-2 questions)

12. **Technical Constraints**: Ask about limitations:
    - Existing tech stack requirements
    - Integration dependencies
    - Performance requirements
    - Security/compliance needs
    - Budget/resource constraints

13. **Timeline**: "What's the target launch date or deadline? Any external dependencies?"

### Phase 6: Prioritization (1 question)

14. **MoSCoW Ranking**: Present the collected features and ask user to categorize:
    - **Must**: Essential for launch
    - **Should**: Important but can defer if needed
    - **Could**: Nice-to-have
    - **Won't**: Explicitly excluded

## Questioning Guidelines

- **One question at a time** - Never overwhelm with multiple questions
- **Use AskUserQuestion tool** with multiple choice options when categories are clear
- **Offer "Other" option** for open-ended responses
- **Summarize understanding** after each phase before moving on
- **Allow backtracking** - If user wants to revise earlier answers, accommodate
- **Skip if already answered** - If user provided info upfront, don't re-ask

## Example Question Flow

```
Q1: "What problem are you solving?"
→ User describes pain point

Q2: "Why is solving this urgent now?"
→ User explains timing

[Summary]: "So we're solving [X] because [Y]. Correct?"
→ User confirms or corrects

Q3: "Who are the primary users?"
→ [Multiple choice with AskUserQuestion]

... continue through phases ...
```

## Autonomous Mode: Complete Example

Below is a full example of Autonomous Mode output with multi-step reasoning:

```markdown
# PRD: IM 即时通讯系统

---

## 🧠 生成说明

**生成模式**: 自主多步推理 (Autonomous Multi-Step Reasoning)  
**输入**: "生成一个 IM 系统的 PRD"  
**推理时长**: 6 个阶段 + 自我质疑

**推理过程摘要**:

| 阶段 | 推理内容 | 置信度 |
|------|----------|--------|
| 1. 问题发现 | 团队需要轻量级内部沟通工具，现有方案过重 | 70% |
| 2. 用户分析 | 20-50 人企业团队，日常协作场景 | 65% |
| 3. 指标定义 | DAU、消息送达率、NPS 为核心指标 | 80% |
| 4. 范围界定 | MVP 聚焦消息 + 群聊，砍掉视频会议等 | 75% |
| 5. 约束识别 | 企业内部部署，安全优先，6-7 周上线 | 60% |
| 6. 优先级 | P0: 消息/群聊，P1: 已读回执/搜索 | 80% |

**关键假设**:
- ⚠️ 目标用户 20-50 人 — 基于常见中小企业规模
- ⚠️ 内部部署 — 基于数据隐私考量
- ⚠️ 6-7 周周期 — 基于 MVP 复杂度估算

---

## 1. 问题陈述

### 核心问题
企业团队需要轻量级即时通讯解决方案，用于内部快速沟通与协作。

**用户原话**（推断）:
> "微信群太乱，钉钉太重，想要个简单的内部沟通工具"

### Why Now（紧迫性）

| 因素 | 说明 | 置信度 |
|------|------|--------|
| 团队扩张 | ⚠️ 假设团队达 20+ 人，现有工具效率下降 | 65% |
| 远程办公 | 混合办公成为常态，沟通需求增加 | 80% |
| 数据安全 | 企业对数据隐私关注度提升 | 75% |

**如果不解决会怎样**:
- 沟通效率持续下降
- 信息分散在多个平台
- 敏感数据可能泄露到外部平台

### 现有解决方案

| 方案类型 | 具体方案 | 缺点/局限 |
|----------|----------|-----------|
| 竞品 | 企业微信/钉钉 | 功能过重，学习成本高 |
| 竞品 | 微信群 | 信息混杂，无组织结构 |
| 竞品 | Slack/Teams | 成本高，国内访问不稳定 |
| 维持现状 | 邮件 + 微信 | 效率低，信息分散 |

---

## 2. 目标与成功指标

### 业务目标
- [ ] 3 个月内覆盖 80% 内部团队
- [ ] 日均活跃用户达到 50+

### 成功指标（KPI）

| 指标类型 | 指标名称 | 当前基线 | 目标值 | 测量方法 | 时间窗口 |
|----------|----------|----------|--------|----------|----------|
| 用户 engagement | DAU | 0 | 50 | 后台统计 | 3 个月 |
| 用户 engagement | 消息送达率 | N/A | 99.9% | 日志监控 | 持续 |
| 用户满意度 | NPS | N/A | 40+ | 季度调研 | 季度 |
| 技术 | 消息延迟 (P95) | N/A | <200ms | APM 监控 | 持续 |

### 非目标（Explicitly NOT doing）
- [ ] 不追求用户规模（仅限内部）
- [ ] 不做开放平台（v1 不考虑第三方集成）

---

## 3. 用户与市场

### 目标用户画像

**主要用户**:
| 属性 | 描述 |
|------|------|
| 用户类型 | 企业内部员工 |
| 年龄段 | 25-45 岁 |
| 使用场景 | 日常工作沟通、项目协作、快速决策 |
| 核心需求 | 快速、简洁、可靠、安全 |
| 痛点 | 信息杂乱、找不到历史记录、多平台切换 |

**次要用户**（如有）:
- 管理者：需要查看团队沟通状态、已读回执

### 用户故事

| ID | 用户角色 | 想要... | 以便... | 优先级 |
|----|----------|---------|---------|--------|
| US-001 | 普通员工 | 发送即时消息 | 快速沟通工作事项 | P0 |
| US-002 | 普通员工 | 创建/加入群聊 | 组织项目讨论 | P0 |
| US-003 | 普通员工 | 查看历史消息 | 找回之前的讨论 | P0 |
| US-004 | 管理者 | 查看消息已读状态 | 确保信息传达 | P1 |
| US-005 | 普通员工 | 搜索消息历史 | 快速定位信息 | P1 |

### 使用场景

**典型场景**（成功路径）:
1. 员工 A 有新想法 → 打开 IM → 给员工 B 发消息 → 立即收到回复
2. 项目经理创建项目群 → 邀请成员 → 大家在群里讨论 → 形成决策

**边缘场景**（失败/异常路径）:
1. 网络不稳定 → 消息发送失败 → 显示重试按钮 → 用户重试成功
2. 用户离线 → 消息暂存服务器 → 用户上线后推送

### 竞争格局

| 竞品 | 优势 | 劣势 | 我们的差异化 |
|------|------|------|--------------|
| 企业微信 | 功能全，生态好 | 太重，学习成本高 | 轻量，专注核心功能 |
| 钉钉 | 免费，功能多 | 太复杂，小团队用不上 | 简洁，上手快 |
| 飞书 | 体验好，文档强 | 成本高，功能过载 | 低价/免费，够用就好 |
| Slack | 体验好，集成多 | 国内访问不稳定，贵 | 本地部署，数据可控 |

---

## 4. 范围定义

### In Scope（v1.0）

| 功能模块 | 功能描述 | 优先级 | 验收标准摘要 |
|----------|----------|--------|--------------|
| 即时消息 | 文本、表情、图片发送 | P0 | 消息延迟<200ms，送达率 99.9% |
| 群组聊天 | 创建群聊、邀请成员、群公告 | P0 | 支持 50 人群，管理员权限 |
| 消息历史 | 查看历史消息、分页加载 | P0 | 支持 6 个月历史，加载<1s |
| 已读回执 | 显示消息已读/未读状态 | P1 | 准确率 100% |
| 消息搜索 | 按关键词搜索历史消息 | P1 | 搜索结果<1s 返回 |

### Out of Scope（本次不做）

| 功能 | 排除原因 | 可能 reconsider 的时间 |
|------|----------|----------------------|
| 视频会议 | MVP 聚焦核心功能 | v2.0 |
| 文件管理 | 使用现有云盘 | 暂不考虑 |
| 机器人集成 | 增加复杂度 | v2.0 |
| 移动端 APP | 先用 H5/小程序 | v2.0 |

### Future Considerations（v2.0+）
- [ ] 视频会议集成
- [ ] 机器人/自动化
- [ ] 与现有系统集成（OA、CRM）
- [ ] 移动端原生 APP

---

## 5. 功能需求详情

### 5.1 功能：即时消息

**功能 ID**: FEAT-001

**优先级**: P0

**功能描述**:
支持用户之间发送文本、表情、图片消息，实时送达。

**用户流程**:
```
用户 A 输入消息 → 点击发送 → 消息显示（发送中）→ 
服务器确认 → 消息显示（已送达）→ 用户 B 收到推送
```

**验收标准**（Gherkin）:
```gherkin
Feature: 即时消息

Scenario: 发送文本消息
  Given 用户 A 和 B 已建立联系
  When 用户 A 发送文本消息
  Then 消息在 200ms 内显示在 B 的对话框
  And 消息状态显示为"已送达"

Scenario: 网络异常时发送消息
  Given 网络不稳定
  When 用户 A 发送消息
  Then 消息显示"发送失败"
  And 显示"重试"按钮

Scenario: 发送图片消息
  Given 用户选择图片
  When 用户发送图片
  Then 图片压缩后上传
  And 在对方对话框显示缩略图
```

**UI/UX 要求**:
- [ ] 消息气泡样式（左收右发）
- [ ] 发送中/已送达/已读状态图标
- [ ] 图片支持点击放大
- [ ] 表情面板

**数据要求**:
- [ ] 消息持久化存储（6 个月）
- [ ] 图片存储（CDN 加速）
- [ ] 消息状态实时更新

---

## 6. 非功能需求（NFR）

### 6.1 性能要求

| 指标 | 要求 | 测量条件 |
|------|------|----------|
| 响应时间 (P95) | <200ms | 正常负载 |
| 响应时间 (P99) | <500ms | 峰值负载 |
| 吞吐量 | 1000 msg/s | |
| 并发用户数 | 100 | |

### 6.2 可靠性要求
- [ ] 可用性目标：99.9%
- [ ] MTTR（平均恢复时间）：<30 分钟
- [ ] 数据持久性：99.999%
- [ ] 容灾要求：单机房部署，支持备份

### 6.3 安全要求
- [ ] 认证方式：企业账号登录
- [ ] 数据加密：TLS 传输加密
- [ ] 敏感数据处理：消息内容加密存储
- [ ] 审计日志：登录日志、操作日志

---

## 7. 时间线与里程碑

### 7.1 项目计划

| 阶段 | 开始日期 | 结束日期 | 交付物 | 负责人 |
|------|----------|----------|--------|--------|
| 需求评审 | Week 1 | Week 1 | PRD 定稿 | 产品经理 |
| 技术设计 | Week 2 | Week 2 | 架构文档 | 技术负责人 |
| 开发 | Week 3 | Week 5 | 可运行代码 | 研发团队 |
| 测试 | Week 6 | Week 6 | 测试报告 | 测试团队 |
| 上线 | Week 7 | Week 7 | 全量发布 | 全体 |

---

## 8. 风险评估与缓解

### 8.1 风险矩阵

| 风险 ID | 风险描述 | 可能性 | 影响 | 风险等级 | 缓解措施 |
|---------|----------|--------|------|----------|----------|
| R-001 | 技术选型不当 | 中 | 高 | 🟡 | 前期技术验证 |
| R-002 | 开发延期 | 中 | 中 | 🟡 | 每周进度检查 |
| R-003 | 用户接受度低 | 低 | 中 | 🟢 | 早期用户参与 |
| R-004 | 安全问题 | 低 | 高 | 🟡 | 安全评审 |

### 8.2 Pre-mortem 分析

**假设项目失败了，可能的原因是**:

| 类别 | 潜在问题 | 预防措施 |
|------|----------|----------|
| 🐯 Tigers（真实威胁） | 技术架构无法支撑并发 | 前期压测验证 |
| 📃 Paper Tigers（表面威胁） | 竞品功能更多 | 聚焦差异化 |
| 🐘 Elephants（大家回避的问题） | 团队没时间用新工具 | 高层推动 |

---

## ⚠️ 需要确认的事项

以下基于假设生成，请确认或修正：

| 编号 | 假设内容 | 推理依据 | 建议确认方式 |
|------|----------|----------|--------------|
| A1 | 目标用户 20-50 人内部团队 | 基于常见中小企业规模 | 与发起人确认 |
| A2 | 部署方式：企业内部服务器 | 基于数据隐私考量 | 与 IT 部门确认 |
| A3 | 开发周期 6-7 周 | 基于 MVP 功能复杂度估算 | 与研发团队确认 |
| A4 | 并发用户 100 人 | 基于团队规模×80% 估算 | 与 HR 确认团队规划 |
| A5 | 不需要移动端 APP | 基于 MVP 聚焦原则 | 与用户代表确认 |

## ❓ 开放问题

| 问题 ID | 问题描述 | 影响范围 | 建议负责人 |
|---------|----------|----------|------------|
| Q-001 | 是否需要与现有系统集成（OA/CRM）？ | 技术架构设计 | 技术负责人 |
| Q-002 | 消息历史保留多久？6 个月还是永久？ | 存储成本 | 产品经理 |
| Q-003 | 是否需要支持外部联系人？ | 功能范围 | 产品经理 |
| Q-004 | 预算范围是多少？ | 技术选型 | 财务/发起人 |

## 📋 下一步建议

1. ✅ 确认上述假设（A1-A5）
2. ✅ 回答开放问题（Q-001~Q-004）
3. ✅ 与干系人评审 PRD（产品 + 技术 + 测试）
4. ✅ 进入技术设计阶段（架构文档）
5. ✅ 确认后更新 PRD 状态为"Approved"

---

*PRD 生成完成 | 状态：Draft | 待确认事项：9 项*
```

```markdown
# PRD: IM 即时通讯系统

## 📋 文档说明

**生成模式**: 自主生成（Autonomous Mode）
- ✅ 基于用户提供信息
- ⚠️ 基于合理假设推断
- ❓ 需要确认的事项

---

## 1. 问题陈述

### 核心问题
用户需要轻量级即时通讯解决方案，用于团队内部快速沟通。

**用户原话**（推断）:
> "微信群太乱，钉钉太重，想要个简单的内部沟通工具"

### Why Now（紧迫性）
- ⚠️ **假设**: 团队规模扩大至 20+ 人，现有沟通工具效率下降
- 📈 远程办公/混合办公成为常态
- 🔒 数据隐私关注度提升

### 现有解决方案
| 方案类型 | 具体方案 | 缺点/局限 |
|----------|----------|-----------|
| 竞品 | 企业微信/钉钉 | 功能过重，学习成本高 |
| 竞品 | 微信群 | 信息混杂，无组织结构 |
| 竞品 | Slack/Teams | 成本高，国内访问不稳定 |
| 维持现状 | 邮件 + 微信 | 效率低，信息分散 |

---

## 2. 目标与成功指标

### 业务目标
- [ ] 3 个月内覆盖 80% 内部团队
- [ ] 日均活跃用户达到 50+

### 成功指标（KPI）

| 指标类型 | 指标名称 | 当前基线 | 目标值 | 测量方法 |
|----------|----------|----------|--------|----------|
| 用户 engagement | DAU | 0 | 50 | 后台统计 |
| 用户满意度 | NPS | N/A | 40+ | 季度调研 |
| 技术 | 消息送达率 | N/A | 99.9% | 日志监控 |

---

## 3. 用户与市场

### 目标用户画像

**主要用户**:
| 属性 | 描述 |
|------|------|
| 用户类型 | 企业内部员工 |
| 年龄段 | 25-45 岁 |
| 使用场景 | 日常工作沟通、项目协作 |
| 核心需求 | 快速、简洁、可靠 |

### 用户故事

| ID | 用户角色 | 想要... | 以便... | 优先级 |
|----|----------|---------|---------|--------|
| US-001 | 普通员工 | 发送即时消息 | 快速沟通工作事项 | P0 |
| US-002 | 项目经理 | 创建项目群组 | 组织团队讨论 | P0 |
| US-003 | 管理者 | 查看消息已读状态 | 确保信息传达 | P1 |

---

## 4. 范围定义

### In Scope（v1.0）

| 功能模块 | 功能描述 | 优先级 |
|----------|----------|--------|
| 即时消息 | 支持文本、表情、图片 | P0 |
| 群组聊天 | 创建群聊、邀请成员 | P0 |
| 消息历史 | 查看历史消息记录 | P0 |
| 已读回执 | 显示消息已读状态 | P1 |

### Out of Scope（本次不做）

| 功能 | 排除原因 |
|------|----------|
| 视频会议 | v2.0 考虑 |
| 文件管理 | 使用现有云盘 |
| 机器人集成 | v2.0 考虑 |

---

## 5. 非功能需求

### 性能要求
- ⚠️ **假设**: 支持 100 并发用户
- 消息延迟 < 200ms
- 可用性 99.9%

### 安全要求
- 端到端加密
- 企业内部网络部署
- 访问控制（员工账号）

---

## 6. 时间线

| 阶段 | 时间 | 交付物 |
|------|------|--------|
| 需求评审 | Week 1 | PRD 定稿 |
| 技术设计 | Week 2 | 架构文档 |
| 开发 | Week 3-5 | 可运行版本 |
| 测试 | Week 6 | 测试报告 |
| 上线 | Week 7 | 全量发布 |

---

## ⚠️ 需要确认的事项

以下基于假设生成，请确认或修正：

| 编号 | 假设内容 | 建议确认方式 |
|------|----------|--------------|
| A1 | 目标用户 20-50 人内部团队 | 与发起人确认 |
| A2 | 部署方式：企业内部服务器 | 与 IT 部门确认 |
| A3 | 开发周期 6-7 周 | 与研发团队确认 |
| A4 | 预算范围：中等 | 与财务确认 |

## ❓ 开放问题

| 问题 ID | 问题描述 | 影响范围 | 负责人 |
|---------|----------|----------|--------|
| Q-001 | 是否需要与现有系统集成？ | 技术架构 | 待定 |
| Q-002 | 是否需要移动端 APP？ | 开发工作量 | 待定 |
| Q-003 | 数据保留策略？ | 存储设计 | 待定 |

---

## 📋 下一步建议

1. ✅ 确认上述假设（A1-A4）
2. ✅ 回答开放问题（Q-001~Q-003）
3. ✅ 与干系人评审 PRD
4. ✅ 进入技术设计阶段
```

After gathering all information, generate a complete PRD with this structure:

```markdown
# PRD: [Product/Feature Name]

## Metadata
| Field | Value |
|-------|-------|
| Author | [User name] |
| Status | Draft |
| Created | [Date] |
| Last Updated | [Date] |

## 1. Problem Statement
[Clear description of the problem and why it matters]

### Why Now?
[Urgency and timing rationale]

## 2. Goals & Success Metrics
### Objectives
- [SMART goal 1]
- [SMART goal 2]

### Success Metrics (KPIs)
| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| [Metric 1] | [Baseline] | [Goal] | [When] |

## 3. User & Market
### Target Users
[Primary persona description]

### User Stories
- As a [user type], I want [action] so that [benefit]

### Competitive Landscape
[How users solve this today]

## 4. Scope
### In Scope (v1)
- [Must-have feature 1]
- [Must-have feature 2]

### Out of Scope
- [Explicitly excluded 1]
- [Explicitly excluded 2]

### Future Considerations (v2+)
- [Deferred feature 1]

## 5. Feature Requirements
### Feature: [Name]
**Priority**: Must/Should/Could
**Description**: [What it does]
**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## 6. Technical Constraints
- [Constraint 1]
- [Constraint 2]

### Dependencies
- [External dependency 1]

## 7. Timeline & Milestones
| Milestone | Target Date |
|-----------|-------------|
| Design Complete | [Date] |
| Development Start | [Date] |
| Beta/Testing | [Date] |
| Launch | [Date] |

## 8. Open Questions
- [Unresolved question 1]
- [Unresolved question 2]

## 9. Appendix
[Any additional context, wireframes references, research links]
```

## After PRD Generation

### Step 1: Save & Share
1. **Save PRD**: Ask where to save (`docs/prd/`, `docs/specs/`, or custom path)
2. **Commit to git**: Create a commit with the PRD document
3. **Share for review**: Suggest sending to stakeholders for feedback

### Step 2: Design (if UI/UX involved)
Ask: "Does this feature need UI design?"
- **Yes** → Suggest using `/brainstorming` skill to explore design approaches
- **Yes + need mockups** → Suggest `/frontend-design` for wireframes/prototypes
- **No** → Skip to implementation planning

### Step 3: Technical Architecture
Ask: "Is this feature complex enough to need a technical architecture design?"
- **Complex feature** → Use `architect` subagent for system design
  - Output: component breakdown, data flow, tech selection, interface design
- **Simple feature** → Skip to task breakdown

### Step 4: Break into Tasks
Ask: "Do you want to break the PRD into development tasks?"
- **Yes** → Use `planner` subagent to create implementation plan
  - Break down based on architecture design
  - Generate TaskCreate items with:
    - Clear acceptance criteria from PRD
    - Dependencies marked (blockedBy)
    - Priority from MoSCoW ranking

### Step 5: Implementation
Once tasks are created:
1. `planner` → Detailed implementation plan per task
2. Write code
3. `code-reviewer` → Auto-review before commit
4. `test-creator` → Generate tests
5. `security-reviewer` → If sensitive code

### Step 6: Validation
Before shipping:
1. `e2e-runner` → Automated testing
2. Compare against PRD success metrics
3. Update PRD status to "Shipped"

## Workflow Cheatsheet

```
Phase 0: Requirements
/prd-writer          → Multi-turn Q&A to gather requirements, generate PRD

Phase 1: Planning
architect agent      → Technical architecture design (how to build it)
planner agent        → Break into implementation tasks (what to build)

Phase 2: Implementation
[write code]

Phase 3: Quality Assurance (parallel)
code-reviewer + security-reviewer  → simultaneous review
test-creator                       → add tests

Phase 4: Validation
e2e-runner           → end-to-end validation
doc-updater          → update documentation

PRD status → Shipped
```

## Handoff Prompts

After PRD is complete, offer these next actions:

```
PRD generated! What would you like to do next?

1. UI/UX Design Exploration (/brainstorming) - if there's an interface
2. Technical Architecture Design (architect) - decide how to build it
3. Break into Development Tasks (planner) - decide what to build
4. Save for now, continue later
```

Use AskUserQuestion to let user choose.

## Key Principles

- **Problem before solution** - Never jump to features before understanding the problem
- **Quantify success** - Vague goals lead to vague outcomes
- **Explicit exclusions** - What you DON'T build is as important as what you do
- **Living document** - Remind user to update as requirements evolve
- **YAGNI** - Ruthlessly cut features that aren't essential for v1

---

## Lenny's Podcast Wisdom Integration

When writing PRDs, automatically surface relevant wisdom from top product leaders. Use these to enrich the PRD process:

### Phase 1: Problem Discovery
> **April Dunford**: "Really great positioning feels so clear, so simple - of course that's what it is."
- Ask: What are competitive alternatives (including status quo)?
- Remember: 40% of B2B deals are lost to "no decision" - you're competing with spreadsheets!

> **Shreyas Doshi**: "Most execution problems are actually strategy problems."
- If user describes execution problems, dig deeper into strategy clarity

### Phase 2: Why Now?
> **Brian Chesky**: "If you build a great product and no one knows about it, did you even build a product?"
- Ask: How will you tell the story of this product?
- Think about every release as a chapter of a story

### Phase 3: Scope Definition
> **Brian Chesky**: "Five teams should do one thing rather than one team do five things."
- Ruthlessly cut scope
- Ask: "What would you cut to concentrate on fewer things?"

> **Brian Chesky**: "The best way to slow a project down is add more people to it."
- Small team, focused scope = faster delivery

### Phase 4: Success Metrics
> **Marty Cagan**: "Optimization is easier than innovation; but only innovation wins."
- Don't just optimize metrics - ask what new value is created
- Everything in the backlog is a bet - make better bets

### Phase 5: Risk Assessment
> **Shreyas Doshi**: Pre-mortem framework
After PRD is drafted, suggest running a pre-mortem:
- **Tigers**: Real threats that could kill the project
- **Paper Tigers**: Seeming threats that aren't real
- **Elephants**: Things nobody is talking about

Ask: "What 3 tigers (real threats) could derail this project?"

### Phase 6: Prioritization
> **Shreyas Doshi**: LNO Framework
- **L (Leverage)**: Which features give 10-100x return? Focus here.
- **N (Neutral)**: Standard features, 1x return
- **O (Overhead)**: Features with less return than effort

### Reference: Wisdom Source
All wisdom sourced from Lenny's Podcast. If you have local transcripts, search them for additional context.

## Quick Mode

If user says "quick PRD" or "lean PRD", use abbreviated flow:
1. Problem (1 question)
2. Users (1 question)
3. Success metric (1 question)
4. Must-have features (1 question)
5. Generate One-Pager PRD format

## Autonomous Mode Triggers

Activate Autonomous Mode when user says:
- "autonomous PRD", "auto PRD", "自己生成 PRD"
- "快速生成", "一次性生成", "不用问我"
- "基于以下信息生成 PRD" + 提供了详细信息
- Agent 判断用户已提供足够上下文（>3 个关键信息点）

In Autonomous Mode:
- Do NOT ask questions one at a time
- DO reason through all 6 phases internally
- DO make educated assumptions for missing info
- DO mark assumptions clearly with ⚠️
- DO output complete PRD in one shot
- DO append confirmation checklist at the end
