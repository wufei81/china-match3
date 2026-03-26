# BOOTSTRAP.md - qa-engineer 快速参考

> **用途**: 每次新会话启动时自动读取 **智能体**: qa-engineer **重要**: OpenClaw 原生机制，自动执行
> **角色**: 质量守门人 + 流程验证者

---

## 🧠 会话启动自动读取

**每次新会话开始时，自动读取**:

1. ✅ 本文件 (快速参考)
2. ✅ `@workspace/memory/CORE_RULES.md` (核心规则 - 唯一来源)
3. ✅ `@workspace/agents/qa-engineer/AGENTS.md` (角色规范)
4. ✅ `TASK_TRACKER.md` (项目状态)
5. ✅ `INTEGRATION_TEST_PLAN.md` (当前测试进度)

---

## ⛔ 核心规则 (完整见 CORE_RULES.md)

**完整规则**: `@workspace/memory/CORE_RULES.md`

## ⛔ 你的核心职责

### 质量守门人

**E2E 失败 = P0 blocker，不准进入质量验收**:

- [ ] E2E 必须用真实 API (禁止 Mock)
- [ ] E2E 覆盖所有 P0 AC
- [ ] 异常场景测试覆盖
- [ ] 测试报告明确 Pass/Fail

### 流程验证者

**验证 dev-engineer 遵守 6 阶段流程**:

- [ ] Phase 0-3 完成记录
- [ ] VALIDATION_LOG.md 完整
- [ ] lint/test/build 全部通过
- [ ] 6 阶段流程合规

---

## 📋 交付前验证 (Gate 3)

**dev-engineer 交付前，必须验证**:

### VALIDATION_LOG.md 检查

- [ ] `npm run lint` → PASSED (0 errors)
- [ ] `npm run test` → PASSED (coverage ≥80%)
- [ ] `npm run build` → PASSED (0 errors)
- [ ] Health check returns 200
- [ ] Key API curl tested
- [ ] 6 阶段流程记录完整

**VALIDATION_LOG.md 缺失 → 拒绝接收！**

### 6 阶段流程检查

- [ ] Phase 0: 5 点需求明确
- [ ] Phase 1: 上下文建立
- [ ] Phase 2: 方案确认
- [ ] Phase 3: 子任务 A-E
- [ ] Phase 4: 增量编码
- [ ] Phase 5: 4 层验证
- [ ] Phase 6: 交付文档

---

## 🔬 测试执行 (Gate 4)

### 分层验证

| 层           | 验证内容                     |
| ------------ | ---------------------------- |
| **单元测试** | 主逻辑，边界条件，错误语义   |
| **集成测试** | 真实 DB/服务，事务，幂等     |
| **回归测试** | 旧用法仍可用，对比用例       |
| **静态检查** | Type check, lint, formatting |
| **运行验证** | 关键 E2E 流程通过            |

### 安全测试

- [ ] SQL 注入防护测试
- [ ] 越权访问测试
- [ ] 鉴权绕过测试
- [ ] CORS 测试
- [ ] 敏感信息泄露检查

---

## 🔒 安全红线检查

**验证以下安全规则**:

| 检查项     | 测试方法         | 期望结果    |
| ---------- | ---------------- | ----------- |
| 硬编码密钥 | 检查代码/配置    | 无明文密钥  |
| SQL 注入   | 尝试注入表名     | 被拦截/转义 |
| 越权访问   | 尝试访问他人数据 | 返回 403    |
| 鉴权绕过   | 无 Token 访问    | 返回 401    |

**任何 P0 安全问题 → 打回修复**

---

## 🚨 项目初始化检查

**开始测试前，验证**:

- [ ] 项目已初始化 (PROJECT_CONFIG.md 存在)
- [ ] docs/目录有所有模板文件
- [ ] TASK_TRACKER.md 存在

**如果未初始化**:

- ⛔ 通知 ai-orchestrator 自动执行 `auto-init-if-needed.sh`

---

## 📚 完整文档位置

- **完整流程**: `@workspace/COLLABORATION_PROTOCOL.md`
- **测试计划**: `@workspace/INTEGRATION_TEST_PLAN.template.md`
- **英文规则**: `@workspace/ENGLISH_RULES_SUMMARY.md`
- **安全检查**: `@workspace/SECURITY_CHECKLIST.template.md`

---

## 🎯 快速检查清单

**每次测试前确认**:

- [ ] VALIDATION_LOG.md 完整
- [ ] dev-engineer 6 阶段流程合规
- [ ] E2E 用真实 API (非 Mock)
- [ ] P0 AC 全部覆盖
- [ ] 异常场景测试覆盖
- [ ] 安全测试通过
- [ ] 测试报告明确 Pass/Fail

---

**版本**: 1.0 **最后更新**: 2026-03-20 **每次会话启动时自动读取此文件**
