# IaC Terraform Skill - 基础设施即代码技能

**版本**: 1.0  
**创建日期**: 2026-03-26  
**触发词**: "Terraform", "IaC", "基础设施代码", "terraform", "infrastructure as code"

---

## 🎯 技能概述

为 DevOps 工程师智能体提供 Terraform 基础设施即代码能力，包括 Terraform 最佳实践、模块化设计、状态管理、CI/CD 集成。

---

## 📊 核心功能

### Terraform 最佳实践

```hcl
# 模块化结构
modules/
├── vpc/
├── eks/
├── rds/
└── s3/

environments/
├── dev/
├── staging/
└── prod/

# 最佳实践
- 使用模块复用
- 状态文件远程存储
- 启用状态锁定
- 使用 workspace 隔离环境
```

### CI/CD 集成

```yaml
# GitHub Actions
name: Terraform
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: hashicorp/setup-terraform@v2
      
      - name: Terraform Init
        run: terraform init
      
      - name: Terraform Format
        run: terraform fmt -check
      
      - name: Terraform Validate
        run: terraform validate
      
      - name: Terraform Plan
        run: terraform plan -out=tfplan
      
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve tfplan
```

---

**最后更新**: 2026-03-26  
**维护者**: DevOpsEngineer
