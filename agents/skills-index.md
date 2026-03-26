# 产研智能体技能总索引

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 统一技能查找和使用

---

## 📊 技能统计

| 智能体 | 技能数 | 共享技能 | 使用率 |
|-------|-------|---------|-------|
| **ProductManager** | 13 | 5 | 高 |
| **Architect** | 16 | 8 | 高 |
| **DevEngineer** | 21 | 10 | 高 |
| **QAEngineer** | 13 | 6 | 高 |
| **DevOpsEngineer** | 13 | 5 | 中 |
| **UI/UX Designer** | 10 | 4 | 中 |
| **ProjectManager** | 10 | 4 | 中 |
| **TechLeader** | 10 | 5 | 高 |

**总计**: 106 个技能，47 个共享技能

---

## 🔍 技能分类索引

### 需求与产品
- **business-analysis** - 商业分析 (PM)
- **user-research** - 用户研究 (PM)
- **data-driven-decision** - 数据驱动决策 (PM)
- **stakeholder-management** - 干系人管理 (PM)
- **product-strategy** - 产品战略 (PM)

### 架构与设计
- **advanced-architecture** - 高级架构 (Arch)
- **security-architecture** - 安全架构 (Arch/Tech)
- **disaster-recovery** - 灾备架构 (Arch)
- **observability-design** - 可观测性设计 (Arch)
- **tech-strategy** - 技术战略 (Arch)
- **system-design** - 系统设计 (Dev)

### 开发与实现
- **code-quality** - 代码质量 (Dev)
- **debugging-diagnosis** - 调试诊断 (Dev)
- **performance-optimization** - 性能优化 (Dev)
- **security-coding** - 安全编码 (Dev)
- **technical-writing** - 技术文档 (Dev)
- **api-governance** - API 治理 (Dev)

### 测试与质量
- **test-automation** - 测试自动化 (QA)
- **performance-testing** - 性能测试 (QA)
- **security-testing** - 安全测试 (QA)
- **quality-metrics** - 质量度量 (QA)
- **shift-left-testing** - 左移测试 (QA)

### 运维与部署
- **iac-terraform** - IaC Terraform (Ops)
- **kubernetes-ops** - K8s 运维 (Ops)
- **ci-cd-pipeline** - CI/CD 流水线 (Ops)
- **monitoring-sre** - 监控 SRE (Ops)
- **cloud-security** - 云安全 (Ops)
- **cost-optimization** - 成本优化 (Ops)

### 设计与体验
- **design-system** - 设计系统 (UI/UX)
- **user-centered-design** - 以用户为中心 (UI/UX)
- **interaction-design** - 交互设计 (UI/UX)
- **design-validation** - 设计验证 (UI/UX)
- **design-handoff** - 设计交付 (UI/UX)

### 项目管理
- **agile-management** - 敏捷管理 (PM)
- **risk-management** - 风险管理 (PM)
- **stakeholder-engagement** - 干系人参与 (PM)
- **cost-budget-management** - 成本预算 (PM)
- **team-leadership** - 团队领导 (PM)

### 技术领导
- **technical-decision** - 技术决策 (Tech)
- **code-quality-system** - 代码质量体系 (Tech)
- **tech-leadership** - 技术领导力 (Tech)
- **tech-debt-management** - 技术债务 (Tech)
- **innovation-research** - 创新研究 (Tech)

---

## 🚀 使用指南

### 查找技能
```bash
# 搜索技能
grep -r "技能名称" agents/*/skills/

# 列出所有技能
find agents/*/skills/ -name "SKILL.md"
```

### 使用技能
```bash
# 复制技能到工作区
cp agents/dev-engineer/skills/code-quality/SKILL.md ./

# 查看技能说明
cat agents/dev-engineer/skills/code-quality/SKILL.md
```

### 贡献技能
```bash
# 创建新技能
mkdir -p agents/my-agent/skills/new-skill
cat > agents/my-agent/skills/new-skill/SKILL.md << 'EOF'
# 技能名称
...
EOF

# 复制到共享目录
cp -r agents/my-agent/skills/new-skill shared-skills/
```

---

## 📈 技能热度

| 技能 | 使用次数 | 贡献者 | 共享状态 |
|------|---------|-------|---------|
| code-quality | 高 | DevEngineer | ✅ 共享 |
| test-automation | 高 | QAEngineer | ✅ 共享 |
| advanced-architecture | 高 | Architect | ✅ 共享 |
| security-architecture | 高 | Architect | ✅ 共享 |
| agile-management | 中 | ProjectManager | ✅ 共享 |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
