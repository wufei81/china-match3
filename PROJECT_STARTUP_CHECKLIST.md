# PROJECT_STARTUP_CHECKLIST.md - 项目启动检查清单

**项目**: OpenClaw 智能体系统  
**创建日期**: 2026-03-26  
**维护者**: ai-orchestrator

---

## 🚨 项目初始化检查（首次启动前）

### 基础配置
- [ ] `PROJECT_CONFIG.md` 存在
- [ ] `.env` 文件配置完成（API 密钥等）
- [ ] 工作目录权限正确

### 文档模板
- [ ] `docs/` 目录存在
- [ ] PRD 模板就绪 (`templates/PRD-Template.md`)
- [ ] 架构模板就绪
- [ ] 测试模板就绪

### 追踪文件
- [ ] `TASK_TRACKER.md` 存在
- [ ] `ERROR_LOG.md` 存在（可选）
- [ ] `VALIDATION_LOG.md` 存在（可选）

### 智能体就绪
- [ ] product-manager 可调用
- [ ] architect 可调用
- [ ] dev-engineer 可调用
- [ ] qa-engineer 可调用
- [ ] ai-orchestrator 可调用

---

## ✅ 任务前检查（每次任务前）

### Phase 0: 需求澄清
- [ ] 功能目标明确（新增/修改/删除什么？）
- [ ] 触发方式明确（从哪里调用？）
- [ ] 输入输出明确（参数、返回结构？）
- [ ] 失败行为明确（异常如何处理？）
- [ ] 质量要求明确（性能、测试要求？）

### PRD 质量检查
- [ ] AC 是 Gherkin 格式 (Given-When-Then)
- [ ] 包含数据结构草稿
- [ ] 包含 API 契约草稿
- [ ] 估算时间（分钟，含 20% buffer）
- [ ] WorkPackages 表格完整

### 下游交付检查
- [ ] architect 收到字段级契约
- [ ] dev-engineer 收到清晰 AC
- [ ] qa-engineer 收到测试场景
- [ ] devops-engineer 收到部署需求

---

## 📋 快速启动命令

```bash
# 检查项目状态
./check-project-status.sh

# 初始化项目（如未初始化）
./init-project.sh

# 自动修复缺失文件
./auto-init-if-needed.sh
```

---

## 📊 检查记录

| 日期 | 检查类型 | 结果 | 操作人 | 备注 |
|------|----------|------|--------|------|
| 2026-03-26 | 初始化检查 | ✅ 通过 | Y9000P | 创建检查清单 |

---

## 🔗 相关文档

- **核心规则**: `@workspace/memory/CORE_RULES.md`
- **协作协议**: `@workspace/COLLABORATION_PROTOCOL.md`
- **6 阶段流程**: `@workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`

---

**模板版本**: 1.0 | **创建日期**: 2026-03-26
