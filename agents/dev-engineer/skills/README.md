# DevEngineer Skills - 技能索引

**最后更新**: 2026-03-26
**版本**: 2.0 (能力增强版)

---

## 📚 技能列表

### 🔴 P0 核心能力增强 (2026-03-26 新增)

| 技能 | 路径 | 触发词 | 核心功能 |
|------|------|--------|---------|
| **代码质量** | `code-quality/` | "代码审查", "重构", "Clean Code" | 代码审查清单、重构技巧、Clean Code 原则、质量度量 |
| **调试诊断** | `debugging-diagnosis/` | "调试", "排查", "根因分析", "5 Whys" | 系统化调试、根因分析、故障模式库、诊断工具链 |
| **性能优化** | `performance-optimization/` | "性能优化", "profiling", "benchmark" | 性能分析、优化策略、基准测试、性能监控 |
| **安全编码** | `security-coding/` | "安全编码", "漏洞预防", "OWASP" | 安全编码规范、输入验证、认证授权、数据安全 |

### ✅ 原有核心技能

| 技能 | 路径 | 触发词 | 核心功能 |
|------|------|--------|---------|
| **API 测试** | `api-tester/` | "API 测试", "接口测试" | API 自动化测试 |
| **多 Agent 协作** | `claude-code-teams/` | "多 Agent", "协作开发" | 协调多个 Claude Code agents |
| **Cursor** | `cursor/` | "Cursor", "IDE" | Cursor IDE 集成 |
| **前端设计** | `frontend-design-pro/` | "前端", "UI 设计" | 前端设计和开发 |
| **UI 审计** | `ui-audit/` | "UI 审计", "前端审查" | UI 代码审查 |
| **文档处理** | `document-pro/` | "PDF", "DOCX" | 文档解析和处理 |
| **自我改进** | `self-improving-agent/` | "学习", "改进" | 持续学习和优化 |

---

## 🎯 技能使用场景

### 新功能开发

```
1. code-quality → 代码规范和设计审查
2. security-coding → 安全编码实践
3. claude-code-teams → 多 Agent 协作开发
4. api-tester → API 测试验证
```

### Bug 排查

```
1. debugging-diagnosis → 系统化排查
2. debugging-diagnosis → 根因分析 (5 Whys)
3. code-quality → 修复后代码审查
```

### 性能优化

```
1. performance-optimization → 性能分析和瓶颈定位
2. performance-optimization → 实施优化
3. performance-optimization → 基准测试验证
```

### 安全加固

```
1. security-coding → 安全代码审查
2. security-coding → 漏洞修复
3. api-tester → 安全测试验证
```

---

## 📋 技能组合模板

### 模板 1: 高质量功能开发

**使用技能**: `code-quality` + `security-coding` + `claude-code-teams`

**输出**:
- 符合 Clean Code 的代码
- 通过安全审查
- 完整的测试覆盖
- 代码审查报告

### 模板 2: 故障排查

**使用技能**: `debugging-diagnosis` + `code-quality`

**输出**:
- 根因分析报告 (5 Whys)
- 修复方案
- 回归测试
- 故障复盘文档

### 模板 3: 性能优化

**使用技能**: `performance-optimization` + `debugging-diagnosis`

**输出**:
- 性能分析报告
- 瓶颈定位
- 优化方案
- 基准测试对比

---

## 🔗 技能依赖关系

```
code-quality (质量基础)
    ↓
security-coding (安全基础)
    ↓
debugging-diagnosis (问题定位)
    ↓
performance-optimization (性能提升)
    ↓
api-tester + claude-code-teams (验证与协作)
```

---

## 📝 更新日志

### v2.0 (2026-03-26)
- ✅ 新增 `code-quality` 技能
- ✅ 新增 `debugging-diagnosis` 技能
- ✅ 新增 `performance-optimization` 技能
- ✅ 新增 `security-coding` 技能
- ✅ 更新 AGENTS.md 工具链

### v1.0 (2026-03-20)
- ✅ 初始版本，包含核心开发技能

---

**维护者**: DevEngineer
**反馈**: 在 `@workspace/agents/dev-engineer` 提交 issue
