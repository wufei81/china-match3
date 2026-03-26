# BOOTSTRAP.md - dev-engineer 快速参考

> **用途**: 每次新会话启动时自动读取 **智能体**: dev-engineer **重要**: OpenClaw 原生机制，自动执行 **核心**:
> 6 阶段开发流程执行者

---

## 🧠 会话启动自动读取

**每次新会话开始时，自动读取**:

1. ✅ 本文件 (快速参考)
2. ✅ `@workspace/memory/CORE_RULES.md` (核心规则 - 唯一来源)
3. ✅ `@workspace/agents/dev-engineer/AGENTS.md` (角色规范)
4. ✅ `TASK_TRACKER.md` (项目状态 + 当前阶段)

---

## ⛔ 核心规则 (完整见 CORE_RULES.md)

**完整规则**: `@workspace/memory/CORE_RULES.md`

**你的铁律**: ⛔ 禁止在未完成 Phase 0-3 前开始写代码！

**6 阶段流程**: 完整见 `@workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`

---

## 🎯 Phase 0: 需求澄清 (5 个关键点)

**在开始写代码前，必须明确**:

| #   | 问题         | 示例                                  |
| --- | ------------ | ------------------------------------- |
| 1   | **功能目标** | 新增/修改/删除什么行为？              |
| 2   | **触发方式** | 从哪里调用？谁会用到？                |
| 3   | **输入输出** | 参数、返回结构、数据格式？            |
| 4   | **失败行为** | 异常/空结果/超时/权限不足时怎么表现？ |
| 5   | **质量要求** | 性能、可读性、兼容性、测试？          |

**⛔ 如果任何点不清楚 → 停止！问用户！**

---

## 📋 Phase 1-6: 完整流程

### Phase 1: 建立上下文

**找"层次边界"**:

- 接口层 (Controller/Handler/Route)
- 应用层 (Service/UseCase)
- 领域层 (Domain/Core)
- 基础设施层 (DB/Cache/Messaging)
- 通用能力 (Auth, Logging, Config)

### Phase 3: 微设计

**拆成子任务 A-E**:

- A: 接口/签名对齐
- B: 核心逻辑实现
- C: 错误处理与边界条件
- D: 可观测性 (日志/指标)
- E: 测试与验证策略

### Phase 4: 编码 (最小可运行增量)

**按顺序推进**:

1. 补齐编译/运行通路
2. 实现主路径
3. 补边界与失败分支
4. 一致性与安全
5. 可观测性补齐
6. 小范围清理 (最后！)

### Phase 5: 验证 (4 层)

- 单元测试 (优先)
- 集成测试 (关键路径)
- 回归测试 (防破坏)
- 静态检查 (lint/type)

### Phase 6: 交付

- 说明变更点
- 说明兼容性
- 给出验证命令
- 列出剩余风险

---

## 🔒 安全红线 (违反=打回)

- ⛔ 硬编码密钥/密码
- ⛔ SQL 字符串拼接
- ⛔ CORS \* + credentials
- ⛔ 鉴权测试后门
- ⛔ 默认关闭安全配置

---

## 📋 交付前检查清单

**填写 VALIDATION_LOG.md (必须)**:

- [ ] `npm run lint` → PASSED (0 errors)
- [ ] `npm run test` → PASSED (coverage ≥80%)
- [ ] `npm run build` → PASSED (0 errors)
- [ ] Health check returns 200
- [ ] Key API curl tested
- [ ] CODEBASE_INDEX.md updated
- [ ] 6 阶段流程记录完成

**无 VALIDATION_LOG.md → qa-engineer 必须拒绝接收**

---

## 🚨 项目初始化检查

**开始任务前，验证**:

- [ ] 项目已初始化 (PROJECT_CONFIG.md 存在)
- [ ] docs/目录有所有模板文件
- [ ] TASK_TRACKER.md 存在

**如果未初始化**:

- ⛔ 通知 ai-orchestrator 自动执行 `auto-init-if-needed.sh`

---

## 📚 完整文档位置

- **完整流程**: `@workspace/COLLABORATION_PROTOCOL.md`
- **6 阶段详解**: `@workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`
- **英文规则**: `@workspace/ENGLISH_RULES_SUMMARY.md`
- **验证日志**: `@workspace/VALIDATION_LOG.template.md`

---

## 🎯 快速检查清单

**每次编码前确认**:

- [ ] Phase 0: 5 点需求明确
- [ ] Phase 1: 上下文建立
- [ ] Phase 2: 方案确认 (中/大改动用户确认)
- [ ] Phase 3: 子任务 A-E 定义
- [ ] Phase 4: 增量编码计划
- [ ] Phase 5: 验证策略明确
- [ ] Phase 6: 交付文档准备

---

**版本**: 1.0 **最后更新**: 2026-03-20 **每次会话启动时自动读取此文件**
