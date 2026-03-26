# CI/CD 配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 自动化代码检查和部署

---

## 🎯 CI/CD 流程

```
代码提交 → Lint → Test → Build → Security Scan → Deploy
   ↓        ↓      ↓      ↓         ↓            ↓
 Push    Gate3  Gate3  Gate3     Gate5      Staging/Prod
```

---

## 📁 工作流配置

### 1. CI/CD Pipeline (ci.yml)

**触发条件**:
- Push 到 main/develop 分支
- Pull Request 到 main 分支

**检查项**:
- ✅ Lint (0 errors)
- ✅ Test (100% pass)
- ✅ Coverage (≥80%)
- ✅ Build (0 errors)
- ✅ Security Scan (0 issues)

**部署**:
- develop → Staging
- main → Production

---

### 2. Agent Notifications (notify-agents.yml)

**触发条件**: CI/CD Pipeline 完成

**通知**:
- 成功 → 通知 QA/DevOps 准备测试/部署
- 失败 → 通知 Dev/Tech 修复问题

---

## 🚀 使用方式

### 触发 CI/CD
```bash
# 提交代码自动触发
git add .
git commit -m "feat: 新功能"
git push origin develop
```

### 查看状态
```bash
# GitHub Actions 页面
https://github.com/your-repo/actions
```

### 手动触发
```bash
# GitHub UI → Actions → Run workflow
```

---

## 📊 检查门禁

### Gate 3: 开发质量
| 检查 | 工具 | 标准 |
|------|------|------|
| Lint | ESLint | 0 errors |
| Test | Jest | 100% pass |
| Coverage | Coverage | ≥80% |
| Build | TypeScript | 0 errors |

### Gate 5: 安全
| 检查 | 方法 | 标准 |
|------|------|------|
| 硬编码密钥 | grep | 0 发现 |
| 健康检查 | grep | 已配置 |
| SQL 注入 | grep | 0 发现 |

---

## 📈 预期效果

| 指标 | 手动 | 自动 | 提升 |
|------|------|------|------|
| **检查时间** | 30 分钟 | 5 分钟 | -83% |
| **漏检率** | 15% | 1% | -93% |
| **部署频率** | 每周 | 每天 | +5x |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
