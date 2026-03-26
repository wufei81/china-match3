# 共享技能库

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 所有产研智能体共享技能和模式

---

## 📁 目录结构

```
shared-skills/
├── code-patterns/        # DevEngineer 贡献 (已填充 ✅)
├── test-patterns/        # QAEngineer 贡献 (已填充 ✅)
├── arch-patterns/        # Architect 贡献 (已填充 ✅)
├── security-patterns/    # TechLeader 贡献 (已填充 ✅)
├── design-patterns/      # UI/UX Designer 贡献 (已填充 ✅)
└── project-patterns/     # ProjectManager 贡献 (已填充 ✅)
```

---

## 🎯 使用方式

### 贡献技能
1. 在自己的智能体目录中创建技能
2. 验证技能有效
3. 复制到 shared-skills/ 对应目录
4. 更新技能说明

### 使用技能
1. 浏览 shared-skills/ 目录
2. 找到需要的技能
3. 复制到个人技能目录或直接使用

---

## 📊 技能清单

### code-patterns/ (来自 DevEngineer)
- ✅ code-quality/ - 代码质量技能
- ✅ debugging-diagnosis/ - 调试诊断技能
- ✅ performance-optimization/ - 性能优化技能
- ✅ security-coding/ - 安全编码技能

### test-patterns/ (来自 QAEngineer)
- ✅ test-automation/ - 测试自动化技能
- ✅ performance-testing/ - 性能测试技能
- ✅ security-testing/ - 安全测试技能

### arch-patterns/ (来自 Architect)
- ✅ advanced-architecture/ - 高级架构技能
- ✅ security-architecture/ - 安全架构技能
- ✅ disaster-recovery/ - 灾备架构技能

### security-patterns/ (来自 TechLeader)
- ✅ security-architecture/ - 安全架构技能
- ✅ code-quality-system/ - 代码质量体系技能

### design-patterns/ (来自 UI/UX Designer)
- ✅ design-system/ - 设计系统技能
- ✅ user-centered-design/ - 以用户为中心的设计技能
- ✅ interaction-design/ - 交互设计技能

### project-patterns/ (来自 ProjectManager)
- ✅ agile-management/ - 敏捷管理技能
- ✅ risk-management/ - 风险管理技能
- ✅ stakeholder-engagement/ - 干系人参与技能

---

## 🔄 同步机制

### 自动同步 (推荐)
```bash
# 每天自动同步
0 2 * * * rsync -av agents/*/skills/* shared-skills/
```

### 手动同步
```bash
# 复制所有技能到共享目录
cp -r agents/*/skills/* shared-skills/
```

---

## 📈 使用统计

| 技能目录 | 技能数 | 使用次数 | 贡献者 |
|---------|-------|---------|-------|
| code-patterns | 4 | - | DevEngineer |
| test-patterns | 3 | - | QAEngineer |
| arch-patterns | 3 | - | Architect |
| security-patterns | 2 | - | TechLeader |
| design-patterns | 3 | - | UI/UX Designer |
| project-patterns | 3 | - | ProjectManager |

**总计**: 18 个共享技能

---

**维护者**: 所有产研智能体  
**最后更新**: 2026-03-26
