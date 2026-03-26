# Everything Claude Code 多智能体配置方案

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 让 8 个产研智能体共享 everything-claude-code 的 13 代理、43 技能、31 命令

---

## 🎯 智能体能力映射

### 核心原则
| 智能体 | 核心职责 | 优先使用的代理/命令 |
|-------|---------|-------------------|
| **ProductManager** | 需求定义、PRD | planner, learn |
| **Architect** | 架构设计 | architect, code-reviewer |
| **UI/UX Designer** | UI/UX 设计 | doc-updater, learn |
| **TechLeader** | 技术决策、评审 | code-reviewer, security-reviewer, go-reviewer |
| **DevEngineer** | 开发实现 | tdd, e2e, build-fix, refactor-clean |
| **QAEngineer** | 测试验证 | e2e-runner, verify, checkpoint |
| **DevOpsEngineer** | 部署运维 | build-fix, verify |
| **ProjectManager** | 项目管理 | planner, checkpoint, verify |

---

## 🤖 各智能体详细配置

### 1️⃣ ProductManager (产品经理)

**核心职责**: 需求定义、PRD 撰写、任务规划

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **planner** | `/planner` | 功能实现规划、任务拆解 | 每次新需求 |
| **learn** | `/learn` | 从需求讨论中提取模式 | 每次会话结束 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `strategic-compact` | 需求精简、PRD 压缩 |
| `continuous-learning` | 从需求讨论中学习模式 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/plan` | 功能实现规划 |
| `/learn` | 会话中提取模式 |
| `/checkpoint` | 保存需求状态 |

#### 配置示例
```markdown
## ProductManager 使用 Everything Claude Code

### 新需求处理流程
1. `/planner "实现用户认证功能"` → 任务拆解
2. 审查规划结果
3. 调整优先级
4. 创建 PRD

### 会话结束
1. `/learn "从需求讨论中提取模式"` → 提取需求模式
2. 保存到技能库

### 配置位置
~/.claude/agents/product-manager.md
```

---

### 2️⃣ Architect (架构师)

**核心职责**: 系统设计、技术选型、架构评审

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **architect** | `/architect` | 系统设计决策 | 每个模块 |
| **code-reviewer** | `/code-review` | 架构审查 | 设计完成后 |
| **security-reviewer** | `/security-reviewer` | 安全架构审查 | 安全敏感设计 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `backend-patterns` | API、数据库、缓存模式 |
| `security-review` | 安全检查清单 |
| `eval-harness` | 架构验证 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/plan` | 架构实现规划 |
| `/code-review` | 架构审查 |
| `/security-reviewer` | 安全审查 |
| `/checkpoint` | 保存架构状态 |

#### 配置示例
```markdown
## Architect 使用 Everything Claude Code

### 架构设计流程
1. `/architect "设计 IM 系统架构"` → 系统设计
2. 审查架构输出
3. `/security-reviewer "审查架构安全性"` → 安全审查
4. `/code-review "审查架构设计"` → 质量审查
5. 更新架构文档

### 配置位置
~/.claude/agents/architect.md
```

---

### 3️⃣ UI/UX Designer (设计师)

**核心职责**: UI 设计、UX 优化、设计系统

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **doc-updater** | `/doc-updater` | 设计文档同步 | 设计变更后 |
| **refactor-cleaner** | `/refactor-clean` | 设计系统清理 | 定期 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `frontend-patterns` | React、Next.js 模式 |
| `coding-standards/typescript` | TypeScript 规范 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/doc-updater` | 设计文档同步 |
| `/refactor-clean` | 清理设计系统 |
| `/learn` | 提取设计模式 |

#### 配置示例
```markdown
## UI/UX Designer 使用 Everything Claude Code

### 设计变更流程
1. 完成设计稿
2. `/doc-updater "更新设计文档"` → 同步文档
3. `/refactor-clean "清理设计系统"` → 清理重复组件
4. `/learn "从设计变更中提取模式"` → 提取模式

### 配置位置
~/.claude/agents/ui-ux-designer.md
```

---

### 4️⃣ TechLeader (技术负责人)

**核心职责**: 技术决策、代码审查、安全评审

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **code-reviewer** | `/code-review` | 代码质量审查 | 每次审查 |
| **security-reviewer** | `/security-reviewer` | 安全漏洞审查 | 每次审查 |
| **go-reviewer** | `/go-review` | Go 代码审查 | Go 项目 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `security-review` | 安全检查清单 |
| `coding-standards` | 编码标准 |
| `verification-loop` | 持续验证 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/code-review` | 代码审查 |
| `/security-reviewer` | 安全审查 |
| `/go-review` | Go 审查 |
| `/verify` | 验证循环 |
| `/checkpoint` | 保存审查状态 |

#### 配置示例
```markdown
## TechLeader 使用 Everything Claude Code

### 代码审查流程
1. `/code-review "审查登录模块代码"` → 质量审查
2. `/security-reviewer "审查登录模块安全性"` → 安全审查
3. 审查结果
4. `/checkpoint "审查完成"` → 保存状态
5. 签字确认

### Go 项目审查
1. `/go-review "审查 Go 后端代码"` → Go 专项审查
2. 审查结果
3. 签字确认

### 配置位置
~/.claude/agents/tech-leader.md
```

---

### 5️⃣ DevEngineer (开发工程师) ⭐ 核心用户

**核心职责**: 功能实现、代码编写、自验证

#### 推荐代理 (全部 13 个)
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **planner** | `/planner` | 任务规划 | 每次新任务 |
| **architect** | `/architect` | 复杂设计 | 复杂任务 |
| **tdd-guide** | `/tdd` | TDD 开发 | 每次开发 |
| **code-reviewer** | `/code-review` | 自审查 | 代码完成 |
| **security-reviewer** | `/security-reviewer` | 自检查 | 安全敏感 |
| **build-error-resolver** | `/build-fix` | 构建修复 | 构建失败 |
| **e2e-runner** | `/e2e` | E2E 测试 | 功能完成 |
| **refactor-cleaner** | `/refactor-clean` | 重构清理 | 定期 |
| **doc-updater** | `/doc-updater` | 文档同步 | 代码变更 |
| **go-reviewer** | `/go-review` | Go 审查 | Go 开发 |
| **go-build-resolver** | `/go-build` | Go 构建修复 | Go 构建失败 |
| **learn** | `/learn` | 模式提取 | 会话结束 |
| **verify** | `/verify` | 验证交付 | 交付前 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `tdd-workflow` | TDD 方法论 |
| `backend-patterns` | 后端模式 |
| `frontend-patterns` | 前端模式 |
| `security-review` | 安全检查 |
| `verification-loop` | 持续验证 |
| `continuous-learning` | 持续学习 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/tdd` | TDD 开发 |
| `/code-review` | 代码审查 |
| `/build-fix` | 构建修复 |
| `/e2e` | E2E 测试 |
| `/refactor-clean` | 重构清理 |
| `/doc-updater` | 文档同步 |
| `/learn` | 模式提取 |
| `/verify` | 验证交付 |

#### 完整开发流程
```markdown
## DevEngineer 使用 Everything Claude Code

### 9 Phase 开发流程

Phase 0: 任务规划
`/planner "实现用户登录功能"`

Phase 1: 架构设计 (复杂任务)
`/architect "设计登录模块架构"`

Phase 2: TDD 开发
`/tdd "实现登录 API"`
→ RED: 编写失败测试
→ GREEN: 实现最少代码
→ IMPROVE: 重构优化

Phase 3: 代码审查
`/code-review "审查登录模块"`
`/security-reviewer "审查安全性"`

Phase 4: 构建验证
`npm run build`
如失败 → `/build-fix "修复构建错误"`

Phase 5: E2E 测试
`/e2e "生成登录流程 E2E 测试"`

Phase 6: 重构清理
`/refactor-clean "清理登录模块死代码"`

Phase 7: 文档同步
`/doc-updater "更新 API 文档"`

Phase 8: 学习提取
`/learn "从登录模块开发中提取模式"`

Phase 9: 验证交付
`/verify "验证登录模块"`
`/checkpoint "登录模块完成"`

### 配置位置
~/.claude/agents/dev-engineer.md (已配置)
```

---

### 6️⃣ QAEngineer (测试工程师)

**核心职责**: 测试验证、E2E 测试、质量门禁

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **e2e-runner** | `/e2e` | E2E 测试生成 | 每次测试 |
| **verify** | `/verify` | 验证循环 | 测试完成 |
| **code-reviewer** | `/code-review` | 测试代码审查 | 测试代码完成 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `eval-harness` | 验证循环评估 |
| `verification-loop` | 持续验证 |
| `tdd-workflow` | TDD 测试 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/e2e` | E2E 测试生成 |
| `/verify` | 验证循环 |
| `/checkpoint` | 保存测试状态 |
| `/code-review` | 测试代码审查 |

#### 配置示例
```markdown
## QAEngineer 使用 Everything Claude Code

### E2E 测试流程
1. `/e2e "生成登录流程 E2E 测试"` → 生成测试
2. 审查测试用例
3. 执行测试
4. 修复失败测试
5. `/verify "验证登录模块"` → 验证循环
6. `/checkpoint "测试完成"` → 保存状态

### 配置位置
~/.claude/agents/qa-engineer.md
```

---

### 7️⃣ DevOpsEngineer (运维工程师)

**核心职责**: 部署、CI/CD、监控、运维

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **build-error-resolver** | `/build-fix` | 构建修复 | 构建失败 |
| **verify** | `/verify` | 部署验证 | 部署前 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `verification-loop` | 部署验证 |
| `backend-patterns` | 部署模式 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/build-fix` | 构建修复 |
| `/verify` | 部署验证 |
| `/checkpoint` | 保存部署状态 |

#### 配置示例
```markdown
## DevOpsEngineer 使用 Everything Claude Code

### 部署流程
1. 准备部署环境
2. 运行构建
3. 如失败 → `/build-fix "修复构建错误"`
4. `/verify "验证部署就绪"` → 部署验证
5. `/checkpoint "部署完成"` → 保存状态

### 配置位置
~/.claude/agents/devops-engineer.md
```

---

### 8️⃣ ProjectManager (项目经理)

**核心职责**: 项目规划、进度追踪、风险管理

#### 推荐代理
| 代理 | 命令 | 使用场景 | 频率 |
|------|------|---------|------|
| **planner** | `/planner` | 项目规划 | 项目启动 |
| **verify** | `/verify` | 项目验证 | 里程碑 |
| **checkpoint** | `/checkpoint` | 保存状态 | 关键节点 |

#### 推荐技能
| 技能 | 用途 |
|------|------|
| `strategic-compact` | 项目精简 |
| `continuous-learning` | 项目模式学习 |

#### 推荐命令
| 命令 | 用途 |
|------|------|
| `/plan` | 项目规划 |
| `/checkpoint` | 保存项目状态 |
| `/verify` | 项目验证 |
| `/learn` | 提取项目管理模式 |

#### 配置示例
```markdown
## ProjectManager 使用 Everything Claude Code

### 项目规划流程
1. `/planner "3 个月 IM 系统开发项目"` → 项目规划
2. 审查任务拆解
3. 调整优先级
4. 创建项目计划

### 里程碑验证
1. `/verify "验证 Phase 1 完成"` → 里程碑验证
2. `/checkpoint "Phase 1 完成"` → 保存状态

### 配置位置
~/.claude/agents/project-manager.md
```

---

## 🔧 统一配置步骤

### Step 1: 安装插件 (所有智能体)
```bash
# 添加市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install everything-claude-code@everything-claude-code
```

### Step 2: 安装规则 (所有智能体)
```bash
# 克隆仓库 (如未克隆)
git clone https://github.com/affaan-m/everything-claude-code.git

# 复制通用规则
cp -r everything-claude-code/rules/common/* ~/.claude/rules/

# 复制语言特定规则 (根据技术栈选择)
cp -r everything-claude-code/rules/typescript/* ~/.claude/rules/
# 或
cp -r everything-claude-code/rules/python/* ~/.claude/rules/
cp -r everything-claude-code/rules/golang/* ~/.claude/rules/
```

### Step 3: 配置智能体 (每个智能体)

#### 更新 AGENTS.md
```markdown
## 4. Toolchains

**核心工具**:
- **everything-claude-code**: ⭐ 核心开发框架 (13 代理、43 技能、31 命令)

**推荐代理**:
- `/planner` - 功能实现规划
- `/tdd` - 测试驱动开发
- `/code-review` - 质量审查
- ... (根据智能体角色选择)

详见：`@workspace/EVERYTHING_CLAUDE_CODE_MULTI_AGENT.md`
```

### Step 4: 配置钩子 (可选)
```json
// ~/.claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "tool == \"Edit\"",
        "hooks": [{
          "type": "command",
          "command": "#!/bin/bash\n# 警告 console.log\n"
        }]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [{
          "type": "command",
          "command": "/learn"
        }]
      }
    ]
  }
}
```

---

## 📊 预期效果

| 智能体 | 效率提升 | 质量提升 | 自动化程度 |
|-------|---------|---------|-----------|
| **ProductManager** | +30% | +40% | 中 |
| **Architect** | +40% | +50% | 高 |
| **UI/UX Designer** | +30% | +40% | 中 |
| **TechLeader** | +50% | +70% | 高 |
| **DevEngineer** | +50% | +60% | 高 |
| **QAEngineer** | +60% | +70% | 高 |
| **DevOpsEngineer** | +40% | +50% | 高 |
| **ProjectManager** | +30% | +40% | 中 |

---

## 🎯 快速开始

### 立即开始 (5 分钟)
```bash
# 1. 安装插件
/plugin marketplace add affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code

# 2. 安装规则
cp -r /home/wufei/.claude/backups/everything-claude-code/rules/common/* ~/.claude/rules/

# 3. 开始使用
/plan "实现功能"
```

### 各智能体开始使用
| 智能体 | 第一个命令 |
|-------|----------|
| ProductManager | `/planner "新需求"` |
| Architect | `/architect "设计架构"` |
| UI/UX Designer | `/doc-updater "更新文档"` |
| TechLeader | `/code-review "审查代码"` |
| DevEngineer | `/tdd "开发功能"` |
| QAEngineer | `/e2e "生成测试"` |
| DevOpsEngineer | `/verify "验证部署"` |
| ProjectManager | `/plan "项目规划"` |

---

## 📋 配置检查清单

### 通用配置
- [ ] 插件已安装
- [ ] 规则已复制
- [ ] 钩子已配置 (可选)

### 各智能体配置
- [ ] ProductManager AGENTS.md 已更新
- [ ] Architect AGENTS.md 已更新
- [ ] UI/UX Designer AGENTS.md 已更新
- [ ] TechLeader AGENTS.md 已更新
- [ ] DevEngineer AGENTS.md 已更新 (✅ 已完成)
- [ ] QAEngineer AGENTS.md 已更新
- [ ] DevOpsEngineer AGENTS.md 已更新
- [ ] ProjectManager AGENTS.md 已更新

### 验证配置
- [ ] 每个智能体可以调用推荐代理
- [ ] 每个智能体可以使用推荐命令
- [ ] 规则生效

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26  
**版本**: 1.0
