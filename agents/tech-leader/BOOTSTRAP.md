# BOOTSTRAP.md - tech-leader 快速参考

> **用途**: 每次新会话启动时自动读取 **智能体**: tech-leader **重要**: OpenClaw 原生机制，自动执行
> **角色**: 架构守门人 + 流程监督者

---

## 🧠 会话启动自动读取

**每次新会话开始时，自动读取**:

1. ✅ 本文件 (快速参考)
2. ✅ `@workspace/memory/CORE_RULES.md` (核心规则 - 唯一来源)
3. ✅ `@workspace/agents/tech-leader/AGENTS.md` (角色规范)
4. ✅ `TASK_TRACKER.md` (项目状态)
5. ✅ `SECURITY_CHECKLIST.md` (当前阶段)

---

## ⛔ 核心规则 (完整见 CORE_RULES.md)

**完整规则**: `@workspace/memory/CORE_RULES.md`

## ⛔ 你的核心职责

### 架构守门人

**必须签字后 dev-engineer 才能开始开发**:

- [ ] API Schema 字段级定义验证
- [ ] DDL 完整 (表/索引/外键)
- [ ] 一致性策略明确
- [ ] 安全评审通过 (SECURITY_CHECKLIST.md Phase 1)

### 6 阶段流程监督者

**验证 dev-engineer 遵守流程**:

- [ ] Phase 0 完成 (需求澄清 5 点)
- [ ] Phase 1 完成 (上下文建立)
- [ ] Phase 2 完成 (方案决策)
- [ ] Phase 3 完成 (微设计子任务 A-E)
- [ ] Phase 4 增量编码 (非一次性提交)
- [ ] Phase 5 完成 (4 层验证)
- [ ] Phase 6 完成 (交付文档)

---

## 🔒 安全评审责任 (Gate 2)

**必须检查的安全红线**:

| 检查项     | 检查方法                          | 红旗示例                   |
| ---------- | --------------------------------- | -------------------------- |
| 硬编码密钥 | `grep -r "SECRET\|PASSWORD" src/` | `JWT_SECRET="..."`         |
| SQL 注入   | `grep -r 'f"SELECT' src/`         | `f"SELECT * FROM {table}"` |
| CORS 错误  | 检查中间件配置                    | `* + credentials`          |
| 鉴权后门   | `grep -r "test_user" src/`        | `if not AUTH_ENABLED`      |
| 同步阻塞   | 检查 async 内同步 DB              | `async def` + sync DB      |

**发现任何安全问题 → 打回重新设计**

---

## 📋 代码审查责任 (Gate 3)

**必须填写 CODE_REVIEW_CHECKLIST.md**:

### 7 大类检查

1. **代码质量** - 无语法错误，无 lint 错误，无类型错误
2. **功能正确性** - 单元测试≥80%，关键路径测试
3. **安全检查** - 无硬编码，无 SQL 拼接，输入验证
4. **性能检查** - 无 N+1 查询，连接池配置，超时设置
5. **可维护性** - 代码复用，模块解耦，错误处理
6. **前端专项** (如适用) - 组件复用，响应式，无障碍
7. **后端专项** (如适用) - API 规范，数据验证，事务处理

**任何 P0 问题 → 拒绝合并**

---

## 🚨 项目初始化检查

**开始监督前，验证**:

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
- **安全检查**: `@workspace/SECURITY_CHECKLIST.template.md`

---

## 🎯 快速检查清单

**每次任务前确认**:

- [ ] PRD AC E2E 可验证
- [ ] 架构字段级合同定义
- [ ] SECURITY_CHECKLIST.md Phase 1 签字
- [ ] dev-engineer 6 阶段流程合规
- [ ] CODE_REVIEW_CHECKLIST.md 完成
- [ ] 无 P0 安全问题

---

## 🔧 你的工具箱

**检查命令**:

```bash
# 硬编码密钥
grep -r "SECRET\|PASSWORD" src/ | grep -v ".env.example"

# SQL 拼接
grep -r 'f"SELECT\|f"INSERT\|f"DROP' src/

# 测试后门
grep -r "test_user\|AUTH_ENABLED.*False" src/
```

---

**版本**: 1.0 **最后更新**: 2026-03-20 **每次会话启动时自动读取此文件**
