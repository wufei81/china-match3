# 🎯 智能体自动读取机制 - 完整方案

> **问题**: 如何让智能体在启动时自动读取规则，无需手动执行初始化脚本？
>
> **答案**: 利用 OpenClaw 原生 BOOTSTRAP.md 机制 + memory 系统 + 自动检测脚本

---

## ✅ 已实现的三层自动读取

### 第 1 层：BOOTSTRAP.md (OpenClaw 原生)

**位置**: `/home/wufei/.openclaw/workspace/BOOTSTRAP.md`

**机制**: OpenClaw **每次新会话启动时自动读取**

**内容**:

- 核心规则摘要 (3 条红线 + 安全基线)
- 6 阶段开发流程
- 5 个质量门禁
- 必备模板清单
- 智能体职责矩阵

**优点**:

- ✅ OpenClaw 原生支持，无需配置
- ✅ 每次会话必读，不会遗漏
- ✅ 简洁版本，快速加载

---

### 第 2 层：memory/CORE_RULES.md (持久化记忆)

**位置**: `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`

**机制**: 所有智能体 AGENTS.md 第 2 节规定"每次会话开始必读"

**内容**:

- 完整 3 条红线 + 安全基线
- 完整 6 阶段开发流程 (英文)
- 完整 5 个质量门禁
- 模板文件清单
- 违规处理
- 智能体职责

**优点**:

- ✅ 持久化记忆系统
- ✅ 所有智能体共享
- ✅ 支持语义检索
- ✅ 版本控制

---

### 第 3 层：agents/\*/AGENTS.md (角色规范)

**位置**: `/home/wufei/.openclaw/workspace/agents/<agent>/AGENTS.md`

**机制**: 每个智能体的核心规范

**内容**:

- 角色特定职责
- 阶段特定流程
- 检查清单
- 工具链

**优点**:

- ✅ 针对性强
- ✅ 详细具体
- ✅ 包含英文规则

---

## 🤖 自动初始化流程

### 完整工作流

```
新会话启动
  ↓
OpenClaw 自动读取 BOOTSTRAP.md (原生机制)
  ↓
智能体读取 memory/CORE_RULES.md (按 AGENTS.md 要求)
  ↓
智能体读取各自 AGENTS.md (角色规范)
  ↓
ai-orchestrator 检测项目状态
  ↓
项目未初始化？
  ├─ 是 → 自动执行 auto-init-if-needed.sh
  │      ↓
  │     创建目录 + 复制模板 + 初始化 Git
  │      ↓
  │     验证完成
  │      ↓
  └─ 否 → 继续
  ↓
开始执行用户任务
```

---

## 📊 对比：之前 vs 现在

| 场景           | 之前                     | 现在                        |
| -------------- | ------------------------ | --------------------------- |
| **新会话启动** | 需要提醒读规则           | 自动读取 BOOTSTRAP.md       |
| **新项目创建** | 手动执行 init-project.sh | 自动检测 + 自动初始化       |
| **规则记忆**   | 散落在多个文件           | 集中在 memory/CORE_RULES.md |
| **智能体遵守** | 依赖自觉                 | AGENTS.md 强制规定          |

---

## 🎯 用户体验

### 之前的流程

```
用户：创建一个新项目
助手：请先运行以下命令
  cd /home/wufei/.openclaw/workspace
  ./init-project.sh my-project
用户：（手动执行）
用户：好了
助手：好的，现在开始任务
```

### 现在的流程

```
用户：创建一个新项目
助手：（自动检测 + 自动初始化）
助手：✅ 项目已自动初始化完成！
助手：所有规则已加载，6 阶段流程已激活。
助手：可以开始任务了，您的第一个需求是？
```

**改进**:

- ✅ 减少 2 步手动操作
- ✅ 无需记忆命令
- ✅ 更流畅的对话
- ✅ 规则自动加载

---

## 📋 验证方法

### 测试 1: 验证 BOOTSTRAP.md 自动读取

```bash
# 启动新会话
/new

# 问智能体
"What should you read on session start?"

# 期望回答
- BOOTSTRAP.md (auto-read by OpenClaw)
- memory/CORE_RULES.md (per AGENTS.md)
- AGENTS.md (role specification)
```

### 测试 2: 验证自动初始化

```bash
# 创建新目录
mkdir test-auto-init
cd test-auto-init

# 对智能体说
"Create a new project here"

# 期望行为
- 自动检测项目未初始化
- 自动执行 auto-init-if-needed.sh
- 回复：项目已自动初始化完成
```

### 测试 3: 验证规则遵守

```bash
# 对 dev-engineer 说
"Add a login API endpoint"

# 期望行为
- 不直接写代码
- 提出 Phase 0 的 5 个问题
- 说明需要需求澄清
```

---

## 🚀 核心文件清单

| 文件                     | 用途              | 自动程度                            |
| ------------------------ | ----------------- | ----------------------------------- |
| `BOOTSTRAP.md`           | 会话启动自动读取  | 🔴 100% 自动 (OpenClaw 原生)        |
| `memory/CORE_RULES.md`   | 持久化核心规则    | 🟡 依赖 AGENTS.md 要求              |
| `agents/*/AGENTS.md`     | 角色规范          | 🟡 依赖智能体自觉                   |
| `auto-init-if-needed.sh` | 自动检测 + 初始化 | 🔴 100% 自动 (ai-orchestrator 调用) |
| `init-project.sh`        | 基础初始化脚本    | 被 auto-init 调用                   |

---

## 🎯 最佳实践

### 推荐配置 (当前已实现)

**什么都不用做！** 已经全自动了：

1. ✅ BOOTSTRAP.md - OpenClaw 原生自动读
2. ✅ memory/CORE_RULES.md - 智能体必读
3. ✅ auto-init-if-needed.sh - 自动检测执行
4. ✅ agents/AGENTS.md - 明确规定流程

### 可选增强 (如需要)

**添加 Session Hook**:

```bash
# ~/.openclaw/session-init.sh
cat /home/wufei/.openclaw/workspace/memory/CORE_RULES.md
```

**配置 Gateway**:

```json
{
  "session": {
    "initScript": "~/.openclaw/session-init.sh"
  }
}
```

---

## 📊 自动化程度总结

| 环节           | 自动化程度     | 实现方式                          |
| -------------- | -------------- | --------------------------------- |
| **规则读取**   | 100% 自动      | BOOTSTRAP.md (原生)               |
| **项目检测**   | 100% 自动      | ai-orchestrator 自动检测          |
| **项目初始化** | 100% 自动      | auto-init-if-needed.sh            |
| **流程遵守**   | 依赖 AGENTS.md | 智能体自觉 + ai-orchestrator 监督 |

---

## ✅ 结论

**当前方案已经是最优解**：

1. ✅ 利用 OpenClaw 原生 BOOTSTRAP.md 机制
2. ✅ 持久化 memory 系统
3. ✅ 自动检测 + 自动初始化
4. ✅ 无需用户手动执行任何命令

**用户只需要**:

- 说"创建新项目"
- 然后开始任务

**其余全部自动！** 🤖

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator
