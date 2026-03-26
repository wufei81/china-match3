# DevEngineer 使用 Everything Claude Code 方案

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 充分利用 everything-claude-code 的 13 个代理、43 个技能和 31 个命令

---

## 🎯 核心能力映射

### everything-claude-code 核心资源

| 类型 | 数量 | 用途 |
|------|------|------|
| **代理 (Agents)** | 13 个 | 专业子代理，处理特定任务 |
| **技能 (Skills)** | 127+ 个 | 工作流定义和领域知识 |
| **命令 (Commands)** | 31 个 | 快速执行的斜杠命令 |
| **规则 (Rules)** | 31+ 个 | 始终遵循的指南 |
| **钩子 (Hooks)** | 自动触发 | 基于事件的自动化 |

---

## 🤖 13 个核心代理使用指南

### 1️⃣ planner - 功能实现规划
**用途**: 将需求拆解为可实现的任务

**使用场景**:
```bash
# 接到新需求时
/planner "添加用户认证功能"

# 输出:
# - 需求分析
# - 任务拆解
# - 优先级排序
# - 时间估算
```

**DevEngineer 集成**:
```markdown
## 开发前使用 planner

1. 收到任务后，先调用 /planner
2. 审查规划是否合理
3. 调整任务优先级
4. 开始实现
```

---

### 2️⃣ architect - 系统设计决策
**用途**: 设计系统架构和技术方案

**使用场景**:
```bash
# 需要设计架构时
/architect "设计 IM 系统架构"

# 输出:
# - 系统架构图
# - 技术选型
# - 数据模型
# - API 设计
```

**DevEngineer 集成**:
```markdown
## 架构设计流程

1. 复杂功能调用 /architect
2. 审查架构设计
3. 与现有架构对齐
4. 记录到 CODEBASE_INDEX.md
```

---

### 3️⃣ tdd-guide - 测试驱动开发
**用途**: 指导 TDD 流程

**使用场景**:
```bash
# TDD 开发时
/tdd "实现用户登录 API"

# 输出:
# - RED: 编写失败测试
# - GREEN: 实现最少代码
# - IMPROVE: 重构优化
```

**DevEngineer 集成**:
```markdown
## TDD 工作流 (强制)

1. 调用 /tdd 开始
2. 遵循 RED-GREEN-IMPROVE 循环
3. 确保覆盖率≥80%
4. 记录到 VALIDATION_LOG.md
```

---

### 4️⃣ code-reviewer - 质量和安全审查
**用途**: 代码质量审查

**使用场景**:
```bash
# 代码完成后
/code-review "审查登录模块代码"

# 输出:
# - 代码质量问题
# - 安全隐患
# - 改进建议
# - 最佳实践对齐
```

**DevEngineer 集成**:
```markdown
## 代码审查流程

1. 代码完成后调用 /code-review
2. 修复所有 P0/P1 问题
3. 再次审查直到通过
4. 填写 CODE_REVIEW_CHECKLIST.md
```

---

### 5️⃣ security-reviewer - 漏洞分析
**用途**: 安全漏洞审查

**使用场景**:
```bash
# 安全敏感功能
/security-reviewer "审查认证模块安全性"

# 输出:
# - OWASP Top 10 检查
# - 潜在漏洞
# - 修复建议
```

**DevEngineer 集成**:
```markdown
## 安全检查 (强制)

1. 安全相关功能必须调用 /security-reviewer
2. 修复所有 P0 安全漏洞
3. 填写 SECURITY_CHECKLIST.md
4. TechLeader 签字确认
```

---

### 6️⃣ build-error-resolver - 构建错误解决
**用途**: 自动修复构建错误

**使用场景**:
```bash
# 构建失败时
/build-fix "修复 TypeScript 编译错误"

# 输出:
# - 错误分析
# - 修复方案
# - 自动修复
```

**DevEngineer 集成**:
```markdown
## 构建错误处理

1. 遇到构建错误调用 /build-fix
2. 审查修复方案
3. 应用修复
4. 验证构建通过
```

---

### 7️⃣ e2e-runner - E2E 测试生成
**用途**: Playwright E2E 测试

**使用场景**:
```bash
# E2E 测试
/e2e "生成登录流程 E2E 测试"

# 输出:
# - E2E 测试脚本
# - 测试数据
# - 执行报告
```

**DevEngineer 集成**:
```markdown
## E2E 测试流程

1. 功能完成后调用 /e2e
2. 审查测试用例
3. 执行测试
4. 修复失败测试
5. 记录到 VALIDATION_LOG.md
```

---

### 8️⃣ refactor-cleaner - 死代码清理
**用途**: 代码重构和清理

**使用场景**:
```bash
# 重构时
/refactor-clean "清理认证模块死代码"

# 输出:
# - 未使用代码识别
# - 重复代码检测
# - 重构建议
```

**DevEngineer 集成**:
```markdown
## 重构流程

1. 定期调用 /refactor-clean
2. 审查重构建议
3. 小步重构
4. 确保测试通过
```

---

### 9️⃣ doc-updater - 文档同步
**用途**: 自动更新文档

**使用场景**:
```bash
# 代码变更后
/doc-updater "更新 API 文档"

# 输出:
# - 文档差异
# - 更新建议
# - 自动更新
```

**DevEngineer 集成**:
```markdown
## 文档同步

1. 代码变更后调用 /doc-updater
2. 审查文档更新
3. 更新 CODEBASE_INDEX.md
4. 提交文档
```

---

### 🔟 go-reviewer - Go 代码审查
**用途**: Go 代码专业审查

**使用场景**:
```bash
# Go 代码审查
/go-review "审查 Go 后端代码"

# 输出:
# - Go 惯用语检查
# - 性能问题
# - 并发安全
```

---

### 1️⃣1️⃣ go-build-resolver - Go 构建错误解决
**用途**: Go 构建错误修复

**使用场景**:
```bash
# Go 构建失败
/go-build "修复 Go 编译错误"

# 输出:
# - 错误分析
# - 修复方案
# - 自动修复
```

---

### 1️⃣2️⃣ 其他专业代理

| 代理 | 用途 | 使用频率 |
|------|------|---------|
| **cpp-reviewer** | C++ 代码审查 | 按需 |
| **python-reviewer** | Python 代码审查 | 按需 |
| **perl-reviewer** | Perl 代码审查 | 按需 |

---

## 🛠️ 31 个核心命令使用指南

### 开发类命令

| 命令 | 用途 | 使用频率 |
|------|------|---------|
| **/tdd** | 测试驱动开发 | 每次开发 |
| **/plan** | 实现规划 | 新任务开始 |
| **/e2e** | E2E 测试生成 | 功能完成 |
| **/code-review** | 代码审查 | 代码完成 |
| **/build-fix** | 修复构建错误 | 构建失败时 |
| **/refactor-clean** | 死代码清理 | 定期 |
| **/go-review** | Go 代码审查 | Go 开发 |
| **/go-test** | Go TDD 工作流 | Go 开发 |
| **/go-build** | Go 构建修复 | Go 构建失败 |

### 学习类命令

| 命令 | 用途 | 使用频率 |
|------|------|---------|
| **/learn** | 会话中提取模式 | 每次会话结束 |
| **/checkpoint** | 保存验证状态 | 关键节点 |
| **/verify** | 运行验证循环 | 功能完成 |
| **/skill-create** | 从 git 历史生成技能 | 项目里程碑 |

### 直觉类命令 (持续学习 v2)

| 命令 | 用途 | 使用频率 |
|------|------|---------|
| **/instinct-status** | 查看学习的直觉 | 每周 |
| **/instinct-import** | 导入直觉 | 需要时 |
| **/instinct-export** | 导出直觉 | 分享时 |
| **/evolve** | 将直觉聚类到技能 | 每月 |
| **/promote** | 提升项目级直觉 | 需要时 |
| **/projects** | 查看已识别项目 | 每月 |

### 配置类命令

| 命令 | 用途 | 使用频率 |
|------|------|---------|
| **/setup-pm** | 配置包管理器 | 项目开始 |

---

## 📚 127+ 技能使用指南

### 核心技能分类

#### 1. 编码标准 (coding-standards/)
- TypeScript 最佳实践
- Python 最佳实践
- Go 最佳实践
- Perl 最佳实践

#### 2. 后端模式 (backend-patterns/)
- API 设计模式
- 数据库模式
- 缓存模式
- 消息队列模式

#### 3. 前端模式 (frontend-patterns/)
- React 模式
- Next.js 模式
- 状态管理
- 性能优化

#### 4. 持续学习 (continuous-learning/)
- 从会话中自动提取模式
- 基于直觉的学习
- 渐进式上下文细化

#### 5. 测试工作流 (tdd-workflow/)
- TDD 方法论
- 测试覆盖率
- 测试最佳实践

#### 6. 安全审查 (security-review/)
- OWASP Top 10
- 安全检查清单
- 漏洞修复

#### 7. 验证循环 (verification-loop/)
- 持续验证
- 检查点机制
- pass@k 指标

---

## 🎯 DevEngineer 完整开发流程

### Phase 0: 任务接收
```bash
# 1. 使用 planner 拆解任务
/planner "实现用户登录功能"

# 2. 审查任务拆解
# 3. 确认优先级
```

### Phase 1: 架构设计 (复杂任务)
```bash
# 1. 使用 architect 设计
/architect "设计登录模块架构"

# 2. 审查架构设计
# 3. 对齐现有架构
# 4. 更新 CODEBASE_INDEX.md
```

### Phase 2: TDD 开发
```bash
# 1. 使用 tdd-guide 开始
/tdd "实现登录 API"

# 2. 遵循 RED-GREEN-IMPROVE 循环
# 3. 确保覆盖率≥80%
```

### Phase 3: 代码审查
```bash
# 1. 代码完成后调用
/code-review "审查登录模块"
/security-reviewer "审查安全性"

# 2. 修复所有 P0/P1 问题
# 3. 填写检查清单
```

### Phase 4: 构建验证
```bash
# 1. 运行构建
npm run build

# 2. 如有错误，调用
/build-fix "修复构建错误"

# 3. 验证构建通过
```

### Phase 5: E2E 测试
```bash
# 1. 生成 E2E 测试
/e2e "生成登录流程 E2E 测试"

# 2. 执行测试
# 3. 修复失败测试
```

### Phase 6: 重构清理
```bash
# 1. 调用重构
/refactor-clean "清理登录模块"

# 2. 审查重构建议
# 3. 小步重构
```

### Phase 7: 文档同步
```bash
# 1. 更新文档
/doc-updater "更新 API 文档"

# 2. 更新 CODEBASE_INDEX.md
# 3. 提交文档
```

### Phase 8: 学习提取
```bash
# 1. 提取模式
/learn "从登录模块开发中提取模式"

# 2. 保存到技能库
# 3. 更新直觉
```

### Phase 9: 验证交付
```bash
# 1. 运行验证
/verify "验证登录模块"

# 2. 保存检查点
/checkpoint "登录模块完成"

# 3. 填写 VALIDATION_LOG.md
# 4. 交付 QA
```

---

## 🔧 钩子 (Hooks) 自动化

### 自动触发钩子

| 钩子 | 触发时机 | 作用 |
|------|---------|------|
| **session-start** | 会话开始 | 加载上下文 |
| **session-end** | 会话结束 | 保存状态 |
| **pre-compact** | 压缩前 | 保存状态 |
| **suggest-compact** | 定期 | 压缩建议 |
| **evaluate-session** | 会话结束 | 提取模式 |

### DevEngineer 钩子配置

```json
{
  "hooks": [
    {
      "name": "warn-console-log",
      "matcher": "tool == \"Edit\" && file matches \\.(ts|tsx|js|jsx)$",
      "command": "grep -n 'console.log' && echo '[Hook] 移除 console.log'"
    },
    {
      "name": "auto-save-context",
      "matcher": "session-end",
      "command": "node scripts/hooks/session-end.js"
    }
  ]
}
```

---

## 📊 规则 (Rules) 遵循

### 通用规则 (必须遵循)

| 规则 | 内容 | 重要性 |
|------|------|-------|
| **coding-style.md** | 不可变性、文件组织 | 🔴 高 |
| **git-workflow.md** | 提交格式、PR 流程 | 🔴 高 |
| **testing.md** | TDD、80% 覆盖率要求 | 🔴 高 |
| **performance.md** | 模型选择、上下文管理 | 🔴 高 |
| **security.md** | 强制性安全检查 | 🔴 高 |

### 语言特定规则

| 规则 | 用途 |
|------|------|
| **typescript/** | TypeScript/JavaScript 模式 |
| **python/** | Python 模式 |
| **golang/** | Go 模式 |
| **perl/** | Perl 模式 |

---

## 🎯 使用检查清单

### 每次开发任务

- [ ] 使用 `/planner` 拆解任务
- [ ] 复杂任务使用 `/architect` 设计
- [ ] 使用 `/tdd` 遵循 TDD 流程
- [ ] 使用 `/code-review` 审查代码
- [ ] 使用 `/security-reviewer` 安全检查
- [ ] 使用 `/build-fix` 修复构建错误
- [ ] 使用 `/e2e` 生成 E2E 测试
- [ ] 使用 `/refactor-clean` 清理死代码
- [ ] 使用 `/doc-updater` 同步文档
- [ ] 使用 `/learn` 提取模式
- [ ] 使用 `/verify` 运行验证
- [ ] 使用 `/checkpoint` 保存状态
- [ ] 填写 `VALIDATION_LOG.md`
- [ ] 更新 `CODEBASE_INDEX.md`

### 每周任务

- [ ] 使用 `/instinct-status` 查看直觉
- [ ] 使用 `/projects` 查看项目统计
- [ ] 审查技能库更新
- [ ] 导出有价值直觉

### 每月任务

- [ ] 使用 `/evolve` 聚类直觉到技能
- [ ] 审查技能有效性
- [ ] 更新规则配置
- [ ] 清理未使用代理

---

## 📈 效果评估

### 预期提升

| 指标 | 当前 | 使用后 | 提升 |
|------|------|-------|------|
| **开发效率** | 基准 | +50% | 代理辅助 |
| **代码质量** | 基准 | +60% | 自动审查 |
| **测试覆盖率** | 80% | 90%+ | TDD 强制 |
| **安全问题** | 基准 | -80% | 安全审查 |
| **返工率** | 25% | 10% | 规划前置 |
| **文档同步** | 手动 | 自动 | doc-updater |

---

## 🚀 快速开始

### 1. 安装插件
```bash
# 添加市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install everything-claude-code@everything-claude-code
```

### 2. 安装规则
```bash
# 复制规则
cp -r /home/wufei/.claude/backups/everything-claude-code/rules/common/* ~/.claude/rules/
cp -r /home/wufei/.claude/backups/everything-claude-code/rules/typescript/* ~/.claude/rules/
```

### 3. 开始使用
```bash
# 尝试第一个命令
/plan "实现用户登录功能"

# 查看可用命令
/plugin list everything-claude-code@everything-claude-code
```

---

## 🔗 相关资源

- **源文件**: `/home/wufei/.claude/backups/everything-claude-code/`
- **精简指南**: https://x.com/affaanmustafa/status/2012378465664745795
- **详细指南**: https://x.com/affaanmustafa/status/2014040193557471352
- **GitHub**: https://github.com/affaan-m/everything-claude-code

---

**维护者**: DevEngineer  
**最后更新**: 2026-03-26  
**版本**: 1.0
