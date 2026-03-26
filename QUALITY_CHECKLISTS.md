# 质量门禁检查清单

**用途**: 开发前、开发中、交付前的质量检查

---

## ✅ 开发前评审清单 (Gate 2.5)

**负责人**: TechLeader  
**时机**: 开发开始前  
**耗时**: 5-10 分钟

### 检查项

- [ ] **PRD 已读**
  - 确认已阅读 PRD 最新版本
  - 理解业务目标和用户需求

- [ ] **API Schema 已确认**
  - API 接口定义清晰
  - 请求/响应格式明确
  - 错误码定义完整

- [ ] **数据结构已确认**
  - 数据库表结构设计合理
  - 索引设计到位
  - 一致性策略明确

- [ ] **技术方案清晰**
  - 技术选型合理
  - 架构设计清晰
  - 风险已识别

- [ ] **设计稿已评审**
  - UI 设计稿已确认
  - 交互细节明确
  - 所有状态定义完整

- [ ] **风险已识别**
  - 技术风险
  - 依赖风险
  - 时间风险

### 评审结论

- [ ] ✅ **通过** - 可以开始开发
- [ ] ⚠️ **有条件通过** - 小问题，开发中修复
- [ ] ❌ **不通过** - 重新设计，不准开始

### 签字确认

**TechLeader**: [姓名]  
**时间**: [YYYY-MM-DD HH:mm]  
**备注**: [任何条件或关注点]

---

## ✅ 开发中自检查清单

**负责人**: DevEngineer  
**时机**: 每 30 分钟或完成一个功能点后  
**耗时**: 2-5 分钟

### 检查项

- [ ] **代码能编译**
  - 无编译错误
  - 无编译警告 (或警告已评估)

- [ ] **单元测试通过**
  - 新增功能有对应测试
  - 现有测试全部通过
  - 覆盖率≥80%

- [ ] **代码规范**
  - 遵循命名规范
  - 函数职责单一
  - 无重复代码

- [ ] **错误处理**
  - 异常场景有处理
  - 错误信息清晰
  - 日志记录完整

- [ ] **安全检查**
  - 无硬编码密钥
  - 输入验证完整
  - 无 SQL 注入风险

- [ ] **性能检查**
  - 无 N+1 查询
  - 缓存使用合理
  - 资源正确释放

### 问题记录

如发现问题，记录到 [ERROR_LOG.md](ERROR_LOG.md)

---

## ✅ 交付前自验证清单 (Gate 3)

**负责人**: DevEngineer  
**时机**: 交付 QA 测试前  
**耗时**: 10-15 分钟

### 1. 静态检查

```bash
# Lint 检查
npm run lint
# 期望：0 errors, <10 warnings
```

- [ ] Lint 通过 (0 errors)

```bash
# 类型检查
npm run type-check
# 期望：0 errors
```

- [ ] 类型检查通过

---

### 2. 单元测试

```bash
# 运行测试
npm run test
# 期望：100% pass, coverage ≥80%
```

- [ ] 测试全部通过
- [ ] 覆盖率≥80%
- [ ] 新增功能有对应测试

---

### 3. 构建检查

```bash
# 构建项目
npm run build
# 期望：build success
```

- [ ] 构建成功
- [ ] 构建产物在预期位置

---

### 4. 健康检查

```bash
# 服务健康检查
curl http://localhost:3000/health
# 期望：{"status":"ok"} 200 OK
```

- [ ] 健康检查通过

```bash
# 数据库连接检查
curl http://localhost:3000/health/db
# 期望：{"status":"ok"} 200 OK
```

- [ ] 数据库连接正常

---

### 5. 关键 API 测试

```bash
# Login API 测试
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456"}'
# 期望：{"token":"...","expiresIn":3600} 200 OK
```

- [ ] Login API 测试通过

```bash
# Register API 测试
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"newuser","password":"123456","email":"test@example.com"}'
# 期望：{"id":"...","username":"newuser"} 201 Created
```

- [ ] Register API 测试通过

---

### 6. 安全自查

- [ ] 无硬编码密钥 (密码、Token、Secret)
- [ ] 敏感信息不进日志
- [ ] SQL 使用参数化查询
- [ ] 输入验证完整

---

### 7. 文档更新

- [ ] CODEBASE_INDEX.md 已更新
- [ ] API 文档已更新
- [ ] 变更已记录

---

### 验证结论

**验证人**: DevEngineer  
**验证时间**: [YYYY-MM-DD HH:mm]

```bash
# 验证输出摘要
$ npm run lint
✓ 0 problems

$ npm run test
PASS (85% coverage)

$ npm run build
✓ Build completed in 3.2s

$ curl http://localhost:3000/health
{"status":"ok"}
```

- [ ] ✅ **全部通过** - 可以交付 QA
- [ ] ⚠️ **部分通过** - 有问题，需要修复
- [ ] ❌ **未通过** - 大量问题，重新开发

### QA 接收确认

**QAEngineer**: [姓名]  
**时间**: [YYYY-MM-DD HH:mm]  
**结论**: 
- [ ] ✅ 接收 - 开始测试
- [ ] ❌ 拒绝 - 修复后重新提交

---

## ✅ 测试评审清单 (Gate 4)

**负责人**: QAEngineer  
**时机**: E2E 测试完成后  
**耗时**: 10-15 分钟

### 检查项

- [ ] **E2E 测试通过**
  - 所有 P0 用例通过
  - 所有 P1 用例≥90% 通过
  - 使用真实 API（非 Mock）

- [ ] **性能测试通过**
  - 响应时间达标
  - 吞吐量达标
  - 资源使用合理

- [ ] **安全测试通过**
  - 无 P0/P1 安全漏洞
  - OWASP Top 10 检查通过

- [ ] **Bug 状态**
  - 所有 P0 Bug 已修复
  - P1 Bug 修复率≥90%

- [ ] **测试报告完整**
  - 测试结果清晰
  - Bug 列表完整
  - 发布建议明确

### 评审结论

- [ ] ✅ **通过** - 可以发布
- [ ] ⚠️ **有条件通过** - 小问题，监控发布
- [ ] ❌ **不通过** - 修复后重新测试

---

## ✅ 部署评审清单 (Gate 5)

**负责人**: DevOpsEngineer  
**时机**: 生产部署前  
**耗时**: 10-15 分钟

### 检查项

- [ ] **测试评审通过**
  - Gate 4 已通过
  - QAEngineer 签字

- [ ] **部署脚本就绪**
  - CI/CD 配置完成
  - 回滚脚本测试通过

- [ ] **监控告警就绪**
  - 监控 Dashboard 配置
  - 告警规则配置
  - 通知渠道测试

- [ ] **健康检查就绪**
  - /health 端点配置
  - /ready 端点配置
  - /live 端点配置

- [ ] **密钥配置**
  - 所有密钥通过环境变量
  - 无硬编码密钥
  - 密钥轮换计划

- [ ] **回滚计划**
  - 回滚步骤明确
  - 回滚时间<10 分钟
  - 回滚测试通过

### 评审结论

- [ ] ✅ **批准发布** - 可以部署生产
- [ ] ⚠️ **谨慎发布** - 密切监控
- [ ] ❌ **推迟发布** - 修复后重新评审

---

## 📊 质量门禁汇总

| 门禁 | 负责人 | 时机 | 耗时 | 状态 |
|------|-------|------|------|------|
| Gate 1: PRD 评审 | AI Orchestrator | PRD 完成后 | 5min | ✅ |
| Gate 2: 架构评审 | TechLeader | 架构完成后 | 15min | ✅ |
| Gate 2.5: 开发前评审 | TechLeader | 开发开始前 | 5min | ⚪ |
| Gate 3: 开发评审 | TechLeader + QA | 交付 QA 前 | 15min | ⚪ |
| Gate 4: 测试评审 | QAEngineer | E2E 完成后 | 15min | ⚪ |
| Gate 5: 部署评审 | DevOpsEngineer | 生产部署前 | 15min | ⚪ |

---

**维护**: TechLeader + AI Orchestrator  
**最后更新**: 2026-03-26 15:35
