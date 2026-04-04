# 项目启动检查清单

**适用范围:** 所有新项目 **执行时机:** 项目创建后 24 小时内 **责任人:** ai-orchestrator + tech-lead

---

## ✅ 基础设施检查

### 1. 版本控制

- [ ] Git 仓库初始化
- [ ] .gitignore 配置 (Python/Node/IDE)
- [ ] 分支策略定义 (main/develop/feature)
- [ ] 提交规范定义 (Conventional Commits)

### 2. 项目结构

- [ ] 标准目录结构创建
- [ ] README.md 初始化
- [ ] LICENSE 选择
- [ ] CHANGELOG.md 创建

### 3. 依赖管理

- [ ] requirements.txt / package.json
- [ ] 依赖版本锁定
- [ ] 虚拟环境配置
- [ ] 依赖安全扫描配置

---

## ✅ 代码质量配置

### 4. 代码规范

- [ ] Python: flake8 / pylint 配置
- [ ] JavaScript: ESLint 配置
- [ ] 格式化：Black / Prettier
- [ ] 导入排序：isort

### 5. Pre-commit Hooks

- [ ] .pre-commit-config.yaml
- [ ] 语法检查
- [ ] 格式化
- [ ] 敏感信息检测

### 6. 编辑器配置

- [ ] .editorconfig
- [ ] VS Code settings.json
- [ ] 推荐插件列表

---

## ✅ 测试配置

### 7. 测试框架

- [ ] 单元测试：pytest / jest
- [ ] 集成测试配置
- [ ] 测试覆盖率：coverage
- [ ] 测试数据管理

### 8. CI/CD

- [ ] GitHub Actions / GitLab CI
- [ ] 自动测试流程
- [ ] 自动部署流程
- [ ] 质量门禁配置

---

## ✅ 文档规范

### 9. 技术文档

- [ ] API 文档：Swagger/OpenAPI
- [ ] 架构设计文档
- [ ] 数据库设计文档
- [ ] 部署文档

### 10. 开发文档

- [ ] 开发环境搭建指南
- [ ] 代码规范文档
- [ ] 提交流程文档
- [ ] 审查清单文档

---

## ✅ 智能体职责分配

| 智能体              | 职责       | 交付物                |
| ------------------- | ---------- | --------------------- |
| **ai-orchestrator** | 总体协调   | 项目治理计划          |
| **architect**       | 架构设计   | 架构文档 + 目录结构   |
| **tech-lead**       | 技术规范   | 代码规范 + Pre-commit |
| **dev-engineer**    | 项目初始化 | 依赖配置 + 环境搭建   |
| **qa-engineer**     | 测试配置   | 测试框架 + CI 配置    |
| **devops-engineer** | 部署配置   | CI/CD + 监控配置      |
| **product-manager** | 需求文档   | PRD + 验收标准        |
| **ui-ux-designer**  | UI 规范    | 设计系统 + 组件库     |
| **project-manager** | 项目计划   | 里程碑 + 资源分配     |

---

## 📊 验收标准

### 必须项 (P0)

- [ ] Git 仓库正常
- [ ] 项目可运行
- [ ] 基础测试通过
- [ ] 代码规范配置

### 重要项 (P1)

- [ ] CI/CD 配置
- [ ] 文档完整
- [ ] Pre-commit 生效
- [ ] 质量门禁配置

### 可选项 (P2)

- [ ] 监控告警
- [ ] 性能基准
- [ ] 安全扫描
- [ ] 自动化文档

---

## 🎯 执行流程

```
项目创建
    ↓
ai-orchestrator 召集智能体
    ↓
各智能体完成职责清单
    ↓
tech-lead 验收
    ↓
ai-orchestrator 最终审查
    ↓
✅ 项目治理完成
```

---

**版本:** v1.0 **生效日期:** 2026-03-20 **适用范围:** 所有新项目 **审查周期:** 每周更新
