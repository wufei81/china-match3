# Cost Optimization Skill - 成本优化技能

**版本**: 1.0  
**创建日期**: 2026-03-26  
**触发词**: "成本优化", "云成本", "FinOps", "cost optimization", "FinOps"

---

## 🎯 技能概述

为 DevOps 工程师智能体提供成本优化能力，包括云成本分析、优化策略、预算管控、成本分摊。

---

## 📊 核心功能

### 成本优化策略

| 领域 | 优化措施 | 节省潜力 |
|------|---------|---------|
| **计算** | 预留实例、自动伸缩 | 30-50% |
| **存储** | 存储分层、生命周期 | 40-60% |
| **网络** | CDN 优化、流量整形 | 20-30% |
| **数据库** | 实例优化、读写分离 | 20-40% |

### 成本管控

```yaml
# 预算告警
budgets:
  - name: monthly-budget
    amount: 10000
    alerts:
      - threshold: 50%
        action: notify
      - threshold: 80%
        action: notify
      - threshold: 100%
        action: block
```

### 成本分摊

| 维度 | 分摊方式 |
|------|---------|
| **按部门** | 部门资源使用 |
| **按项目** | 项目标签 |
| **按环境** | dev/staging/prod |

---

**最后更新**: 2026-03-26  
**维护者**: DevOpsEngineer
