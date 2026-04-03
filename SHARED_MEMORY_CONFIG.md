# 🧠 产研团队共享记忆配置方案 (v2.0)

> **版本**: 2.0 | **生效日期**: 2026-04-03 | **适用范围**: 17 个产研智能体

---

## 一、当前记忆架构状态

### ✅ 已运行的 Qdrant 向量记忆 (9 个集合)

```
Qdrant: localhost:6333
状态：✅ 运行中
集合数：9 个
```

| 集合名 | 记录数 | 用途 | 访问权限 |
|--------|--------|------|----------|
| `project_memory` | 25 条 | 项目基本信息、目标、里程碑 | 全团队读写 |
| `decision_log` | 6 条 | 技术/产品/设计决策日志 | 全团队读写 |
| `codebase_knowledge` | 9 条 | 代码结构、API 契约、数据模型 | 全团队读写 |
| `collaboration_context` | 0 条 | 智能体间交接记录、依赖、阻塞 | 全团队读写 |
| `meeting_minutes` | 0 条 | 设计评审、代码审查会议记录 | 全团队读写 |
| `pm_shared_decisions` | 4 条 | PM 内部决策记录 | 仅 3 个 PM |
| `pm_shared_research` | 4 条 | 用户研究、竞品分析 | 仅 3 个 PM |
| `pm_shared_prd_templates` | 2 条 | PRD 模板、案例库 | 仅 3 个 PM |
| `claw-team-memos` | - | 商业分析团队备忘录 | Scout/Analyst/Strategist |

### ✅ 文件系统共享记忆

**位置**: `/home/wufei/.openclaw/workspace/agents/claw-team/shared/`

```
shared/
├── memos/               # 团队备忘录
├── project_briefs/      # 项目背景文档 (待创建)
├── market_intel/        # Scout 情报 (待创建)
├── data_analysis/       # Analyst 数据报告 (待创建)
├── strategy_reports/    # Strategist 战略报告 (待创建)
├── templates/           # 报告模板 (待创建)
└── archives/            # 归档项目 (待创建)
```

---

## 二、17 智能体共享记忆配置

### 2.1 记忆分层架构

```
┌─────────────────────────────────────────────────────────────┐
│                    L1: 全员共享记忆 (Qdrant)                 │
│  所有 17 个智能体都可读写的向量记忆                            │
│  - project_memory (项目信息)                                │
│  - decision_log (决策日志)                                  │
│  - codebase_knowledge (代码知识)                            │
│  - collaboration_context (协作上下文)                        │
│  - meeting_minutes (会议纪要)                               │
└─────────────────────────────────────────────────────────────┘
                            ↑↓
┌─────────────────────────────────────────────────────────────┐
│                    L2: 角色专属记忆 (Qdrant)                 │
│  特定角色智能体专属的向量记忆                                │
│  - pm_shared_* (3 个 PM 专属)                                │
│  - claw-team-memos (Strategist/Scout/Analyst 专属)          │
└─────────────────────────────────────────────────────────────┘
                            ↑↓
┌─────────────────────────────────────────────────────────────┐
│                    L3: 文件系统共享 (Git 版本控制)            │
│  所有智能体可读写的文件共享空间                              │
│  - /workspace/docs/ (文档归档)                              │
│  - /workspace/templates/ (模板库)                           │
│  - /agents/claw-team/shared/ (团队共享)                     │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 智能体记忆权限矩阵

| 智能体 | L1 全员共享 | L2 角色专属 | L3 文件系统 |
|--------|-------------|-------------|-------------|
| `main-agent` | ✅ 读写 | ❌ | ✅ 读写 |
| `ai-orchestrator` | ✅ 读写 | ❌ | ✅ 读写 |
| `product-manager-qwen` | ✅ 读写 | ✅ PM 专属 | ✅ 读写 |
| `product-manager-glm` | ✅ 读写 | ✅ PM 专属 | ✅ 读写 |
| `product-manager-kimi` | ✅ 读写 | ✅ PM 专属 | ✅ 读写 |
| `architect` | ✅ 读写 | ❌ | ✅ 读写 |
| `tech-leader` | ✅ 读写 | ❌ | ✅ 读写 |
| `dev-engineer-qwen` | ✅ 读写 | ❌ | ✅ 读写 |
| `dev-engineer-glm` | ✅ 读写 | ❌ | ✅ 读写 |
| `ui-ux-designer-qwen` | ✅ 读写 | ❌ | ✅ 读写 |
| `ui-ux-designer-kimi` | ✅ 读写 | ❌ | ✅ 读写 |
| `qa-engineer` | ✅ 读写 | ❌ | ✅ 读写 |
| `devops-engineer` | ✅ 读写 | ❌ | ✅ 读写 |
| `project-manager` | ✅ 读写 | ❌ | ✅ 读写 |
| `strategist` | ✅ 读写 | ✅ 商业团队专属 | ✅ 读写 |
| `analyst` | ✅ 读写 | ✅ 商业团队专属 | ✅ 读写 |
| `scout` | ✅ 读写 | ✅ 商业团队专属 | ✅ 读写 |

---

## 三、各智能体记忆使用规范

### 3.1 产品系 (3 PM)

**写入内容**:
- `project_memory`: 项目目标、里程碑、AC
- `decision_log`: 产品决策、优先级变更
- `pm_shared_decisions`: PM 内部辩论记录
- `pm_shared_research`: 用户研究、竞品分析
- `pm_shared_prd_templates`: PRD 模板、案例

**查询场景**:
- 新项目启动 → 查询 `project_memory` 了解历史
- PRD 评审 → 查询 `pm_shared_decisions` 参考过往决策
- 需求变更 → 查询 `decision_log` 追溯决策原因

**示例代码**:
```python
# PM 写入产品决策
client.upsert(
    collection_name="pm_shared_decisions",
    points=[{
        "id": "pm-decision-001",
        "vector": [...],
        "payload": {
            "project_id": "proj-im-2026",
            "decision_type": "feature_priority",
            "pm_agent": "product-manager-qwen",
            "content": "登录功能优先级高于消息已读",
            "consensus_level": "unanimous",
            "created_at": "2026-04-03T12:00:00Z"
        }
    }]
)
```

### 3.2 研发系 (2 Dev)

**写入内容**:
- `codebase_knowledge`: API 实现细节、数据模型变更
- `collaboration_context`: 模块间接口约定、依赖关系
- `decision_log`: 技术选型决策

**查询场景**:
- 开发前 → 查询 `codebase_knowledge` 了解现有 API
- 接口对齐 → 查询 `collaboration_context` 确认依赖
- 技术决策 → 查询 `decision_log` 参考历史选型

**示例代码**:
```python
# Dev 写入代码知识
client.upsert(
    collection_name="codebase_knowledge",
    points=[{
        "id": "code-api-login",
        "vector": [...],
        "payload": {
            "project_id": "proj-im-2026",
            "knowledge_type": "api_spec",
            "created_by": "dev-engineer-qwen",
            "api_path": "POST /api/auth/login",
            "content": "登录 API 实现细节...",
            "tags": ["auth", "login", "jwt"]
        }
    }]
)
```

### 3.3 设计系 (2 UI)

**写入内容**:
- `project_memory`: 用户旅程、交互流程
- `decision_log`: 设计决策、风格选择
- `meeting_minutes`: 设计评审记录

**查询场景**:
- 新设计启动 → 查询 `project_memory` 了解用户需求
- 设计规范 → 查询 `decision_log` 参考历史决策
- 设计评审 → 写入 `meeting_minutes` 记录反馈

### 3.4 架构师 (Architect)

**写入内容**:
- `codebase_knowledge`: 架构决策、技术选型、API 契约
- `decision_log`: 架构评审结论

**查询场景**:
- 架构设计 → 查询 `codebase_knowledge` 了解现有架构
- 技术选型 → 查询 `decision_log` 参考历史选型理由

### 3.5 技术负责人 (Tech-Leader)

**写入内容**:
- `decision_log`: 技术评审结论、代码审查意见
- `meeting_minutes`: 技术评审会议记录

**查询场景**:
- 架构评审 → 查询 `decision_log` 了解历史决策
- 代码审查 → 查询 `codebase_knowledge` 确认规范

### 3.6 测试系 (QA)

**写入内容**:
- `meeting_minutes`: 测试评审、Bug 评审记录
- `collaboration_context`: 测试阻塞、依赖开发修复

**查询场景**:
- 测试计划 → 查询 `project_memory` 了解 AC
- Bug 跟踪 → 查询 `collaboration_context` 确认修复状态

### 3.7 运维系 (DevOps)

**写入内容**:
- `codebase_knowledge`: 部署配置、CI/CD 流程
- `collaboration_context`: 发布阻塞、环境问题

**查询场景**:
- 发布准备 → 查询 `meeting_minutes` 确认评审通过
- 问题排查 → 查询 `collaboration_context` 了解变更历史

### 3.8 项目经理 (PM)

**写入内容**:
- `project_memory`: 里程碑更新、风险记录
- `meeting_minutes`: 项目例会记录
- `collaboration_context`: 依赖跟踪、阻塞解除

**查询场景**:
- 进度跟踪 → 查询 `project_memory` 了解里程碑
- 风险管理 → 查询 `collaboration_context` 确认阻塞状态

### 3.9 协调者 (AI-Orchestrator)

**写入内容**:
- `collaboration_context`: 智能体调度记录、任务交接
- `meeting_minutes`: 跨智能体协调会议

**查询场景**:
- 任务调度 → 查询 `collaboration_context` 了解依赖
- 进度汇总 → 查询所有集合生成状态报告

### 3.10 商业团队 (Strategist/Scout/Analyst)

**写入内容**:
- `claw-team-memos`: 情报简报、数据报告、战略报告
- `project_memory`: 商业目标、市场分析
- `decision_log`: 商业决策

**查询场景**:
- 情报搜集 → 查询 `claw-team-memos` 获取历史情报
- 数据分析 → 查询 `project_memory` 了解业务目标

---

## 四、记忆写入与查询流程

### 4.1 写入流程

```
1. 智能体完成任务
       ↓
2. 提取关键信息 (决策/知识/上下文)
       ↓
3. 生成向量 (使用嵌入模型)
       ↓
4. 写入对应集合 (根据权限)
       ↓
5. 记录日志 (memory.log)
```

### 4.2 查询流程

```
1. 智能体启动任务
       ↓
2. 生成查询向量 (任务描述→向量)
       ↓
3. 查询相关集合 (带权限过滤)
       ↓
4. 返回 Top-N 结果 (相似度排序)
       ↓
5. 智能体使用结果辅助决策
```

---

## 五、文件系统共享规范

### 5.1 文档归档路径

| 文档类型 | 存储路径 | 命名规范 |
|----------|----------|----------|
| PRD | `/workspace/docs/prd/` | `PRD-[项目]-[版本].md` |
| FSD | `/workspace/docs/fsd/` | `FSD-[项目]-[版本].md` |
| 架构文档 | `/workspace/docs/arch/` | `ARCH-[项目]-[版本].md` |
| API 契约 | `/workspace/docs/api/` | `API-[服务]-[版本].md` |
| 测试计划 | `/workspace/docs/qa/` | `TEST-[项目]-[版本].md` |
| UI 规范 | `/workspace/docs/ui/` | `UI-[项目]-[版本].md` |

### 5.2 模板库路径

| 模板类型 | 存储路径 |
|----------|----------|
| PRD 模板 | `/workspace/templates/PRD.template.md` |
| FSD 模板 | `/workspace/templates/FSD.template.md` |
| 架构模板 | `/workspace/templates/ARCHITECTURE.template.md` |
| API 模板 | `/workspace/templates/API_SPEC.template.md` |
| 测试计划模板 | `/workspace/templates/TEST_PLAN.template.md` |

### 5.3 团队共享路径

| 内容类型 | 存储路径 |
|----------|----------|
| 项目背景 | `/agents/claw-team/shared/project_briefs/` |
| 市场情报 | `/agents/claw-team/shared/market_intel/` |
| 数据报告 | `/agents/claw-team/shared/data_analysis/` |
| 战略报告 | `/agents/claw-team/shared/strategy_reports/` |
| 模板 | `/agents/claw-team/shared/templates/` |
| 归档 | `/agents/claw-team/shared/archives/` |

---

## 六、记忆维护与清理

### 6.1 定期清理策略

| 记忆类型 | 保留期限 | 清理方式 |
|----------|----------|----------|
| `project_memory` | 项目结束后 1 年 | 归档到冷存储 |
| `decision_log` | 永久保留 | 不清理 |
| `codebase_knowledge` | 代码删除后 6 个月 | 标记过期 |
| `collaboration_context` | 30 天 | 自动清理 |
| `meeting_minutes` | 1 年 | 归档 |
| `pm_shared_*` | 永久保留 | 不清理 |

### 6.2 备份策略

| 备份类型 | 频率 | 存储位置 |
|----------|------|----------|
| Qdrant 快照 | 每日 | `~/.openclaw/backups/qdrant/` |
| 文件系统 | 每次 commit | Git 版本控制 |
| 完整备份 | 每周 | 外部存储 |

---

## 七、监控与告警

### 7.1 健康检查

```bash
# Qdrant 健康检查
curl http://localhost:6333/health

# 集合统计
curl http://localhost:6333/collections | python3 -m json.tool

# 记忆日志
tail -f /var/log/openclaw/memory.log
```

### 7.2 告警规则

| 指标 | 阈值 | 告警方式 |
|------|------|----------|
| Qdrant 不可用 | 连续 3 次失败 | 通知 devops-engineer |
| 集合记录数异常 | 日增长>1000 条 | 通知 ai-orchestrator |
| 查询延迟 | P95>500ms | 通知 architect |
| 磁盘使用 | >80% | 通知 devops-engineer |

---

## 八、快速参考卡片

### 智能体记忆速查

| 智能体 | 主要写入集合 | 主要查询集合 |
|--------|-------------|-------------|
| PM-* | project_memory, pm_shared_* | project_memory, pm_shared_* |
| Dev-* | codebase_knowledge, collaboration_context | codebase_knowledge |
| UI-* | project_memory, meeting_minutes | project_memory |
| Architect | codebase_knowledge, decision_log | decision_log |
| Tech-Leader | decision_log, meeting_minutes | decision_log |
| QA | meeting_minutes, collaboration_context | project_memory |
| DevOps | codebase_knowledge, collaboration_context | meeting_minutes |
| Project-Mgr | project_memory, collaboration_context | 全部 |
| Orchestrator | collaboration_context | 全部 |
| Strategist | claw-team-memos, project_memory | claw-team-memos |
| Scout | claw-team-memos | claw-team-memos |
| Analyst | claw-team-memos, data_analysis | claw-team-memos |

### 集合用途速查

| 集合名 | 用途 | 保留期 |
|--------|------|--------|
| `project_memory` | 项目信息、里程碑、AC | 项目后 1 年 |
| `decision_log` | 技术/产品/设计决策 | 永久 |
| `codebase_knowledge` | 代码/架构/API 知识 | 代码后 6 月 |
| `collaboration_context` | 交接/依赖/阻塞 | 30 天 |
| `meeting_minutes` | 会议记录 | 1 年 |
| `pm_shared_*` | PM 专属记忆 | 永久 |
| `claw-team-memos` | 商业团队记忆 | 永久 |

---

## 九、实施检查清单

### 已完成 ✅

- [x] Qdrant 运行中 (9 个集合)
- [x] 文件系统共享目录创建
- [x] 智能体权限矩阵定义
- [x] 记忆写入/查询流程定义
- [x] 文档归档路径规划

### 待完成 📋

- [ ] 各智能体 AGENTS.md 注入记忆使用规范
- [ ] 记忆写入/查询 SDK 封装
- [ ] 记忆质量监控仪表板
- [ ] 记忆清理自动化脚本
- [ ] 记忆备份自动化

---

> 📌 **本方案为产研智能体共享记忆配置标准，所有智能体必须严格遵守**
> 
> **版本**: 2.0 | **最后更新**: 2026-04-03 | **维护者**: ai-orchestrator + devops-engineer
