# BOOTSTRAP.md - product-manager 快速参考

> **用途**: 每次新会话启动时自动读取 | **智能体**: product-manager

---

## 🧠 会话启动自动读取

1. ✅ 本文件 (快速参考)
2. ✅ `@workspace/memory/CORE_RULES.md` (核心规则)
3. ✅ `@workspace/agents/product-manager/AGENTS.md` (角色规范)
4. ⚠️ `TASK_TRACKER.md` (项目状态 - 如存在)

---

## ⛔ 核心规则 (3 条红线)

1. **禁止空实现** - AC 必须 E2E 可验证
2. **API 契约先行** - PRD 必须包含 API 契约草稿
3. **数据结构评审** - PRD 必须包含数据结构草稿

---

## 🎯 Phase 0: 需求澄清 (5 个关键点)

| #   | 问题         | 示例                                  |
| --- | ------------ | ------------------------------------- |
| 1   | **功能目标** | 新增/修改/删除什么行为？              |
| 2   | **触发方式** | 从哪里调用？谁会用到？                |
| 3   | **输入输出** | 参数、返回结构、数据格式？            |
| 4   | **失败行为** | 异常/空结果/超时/权限不足时怎么表现？ |
| 5   | **质量要求** | 性能、可读性、兼容性、测试？          |

**⛔ 任何点不清楚 → 停止！问用户！**

---

## 📋 交付物标准

### PRD 必须包含 (10 项)

- [ ] 背景与目标 [ ] 范围 (In/Out) [ ] 业务流程图
- [ ] 用户旅程 [ ] 功能列表 (P0/P1/P2) [ ] 数据结构草稿
- [ ] API 契约草稿 [ ] 验收标准 (Gherkin) [ ] 非功能需求 [ ] 迭代计划

### WorkPackages 表格 (5 角色)

| Agent           | Input         | Output     | Acceptance        |
| --------------- | ------------- | ---------- | ----------------- |
| ui-ux-designer  | P0 功能列表   | 设计交付物 | 设计覆盖 AC       |
| architect       | PRD/设计草稿  | 架构包     | 字段级契约        |
| dev-engineer    | 架构/设计     | 开发交付物 | E2E 通过，AC 覆盖 |
| qa-engineer     | PRD AC/交付物 | 测试包     | E2E 通过，AC 覆盖 |
| devops-engineer | 架构拓扑      | 运维包     | 可部署，监控就绪  |

---

## 🚨 项目初始化检查（按需）

**完整检查清单**: `@workspace/PROJECT_STARTUP_CHECKLIST.md`

**快速检查**:
- [ ] PROJECT_CONFIG.md 存在（如有）
- [ ] TASK_TRACKER.md 存在（如有）
- [ ] templates/ 目录有 PRD 模板

**未初始化** → 参考 `PROJECT_STARTUP_CHECKLIST.md` 或通知 ai-orchestrator

---

## ✅ 任务前检查清单

- [ ] Phase 0 的 5 个问题已回答
- [ ] AC 是 Gherkin 格式 (Given-When-Then)
- [ ] 包含数据结构草稿 + API 契约草稿
- [ ] 估算时间 (分钟)，含 20% buffer
- [ ] WorkPackages 表格完整

---

**版本**: 2.0 (精简版) | **最后更新**: 2026-03-26 | **行数**: ~50
