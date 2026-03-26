# CI/CD Pipeline Skill - CI/CD 流水线技能

**版本**: 1.0  
**创建日期**: 2026-03-26  
**触发词**: "CI/CD", "流水线", "持续集成", "持续部署", "CI/CD pipeline"

---

## 🎯 技能概述

为 DevOps 工程师智能体提供 CI/CD 流水线设计能力，包括流水线架构、质量门禁、部署策略、回滚机制。

---

## 📊 核心功能

### 流水线设计

```yaml
# 完整 CI/CD 流水线
stages:
  - build
  - test
  - security-scan
  - deploy-staging
  - e2e-test
  - deploy-prod

# 质量门禁
quality_gates:
  - lint: pass
  - unit_test: coverage≥80%
  - security_scan: no critical
  - e2e: 100% pass

# 部署策略
deploy_strategy:
  type: canary
  canary_percentage: 10
  auto_rollback: true
```

### 部署策略对比

| 策略 | 风险 | 回滚速度 | 适用场景 |
|------|------|---------|---------|
| **滚动更新** | 低 | 快 | 常规发布 |
| **蓝绿部署** | 低 | 即时 | 重要发布 |
| **金丝雀** | 最低 | 快 | 高风险发布 |

---

**最后更新**: 2026-03-26  
**维护者**: DevOpsEngineer
