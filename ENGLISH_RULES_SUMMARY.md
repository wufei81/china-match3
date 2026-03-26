# 📋 6-Phase Development Process (English Rules Summary)

**版本**: 1.0 **生效日期**: 2026-03-20 **适用范围**: All 9 R&D agents

---

## 🎯 Overview

Complete 6-phase development process rules have been added to all 9 agents' `AGENTS.md` in **English**.

**Rules Source**: User-provided development best practices (translated to English)

---

## 📁 Where Rules Are Stored

### Primary Location (Memory System)

- `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md` - Core rules summary

### Agent-Specific Rules (Each Agent's AGENTS.md)

| Agent               | Phase Focus                                        | Location                           |
| ------------------- | -------------------------------------------------- | ---------------------------------- |
| **product-manager** | Phase 0: Requirements Clarification                | `agents/product-manager/AGENTS.md` |
| **architect**       | Phase 1: Context + Phase 3: Design                 | `agents/architect/AGENTS.md`       |
| **tech-leader**     | Phase 0/1/3/5/6: Review & Oversight                | `agents/tech-leader/AGENTS.md`     |
| **dev-engineer**    | Phase 1/3/4/5/6: Full Implementation               | `agents/dev-engineer/AGENTS.md`    |
| **qa-engineer**     | Phase 0: Testability + Phase 5: Validation         | `agents/qa-engineer/AGENTS.md`     |
| **devops-engineer** | Phase 1: Infrastructure + Phase 5: Deployment      | `agents/devops-engineer/AGENTS.md` |
| **ai-orchestrator** | Phase 0-6: Process Tracking                        | `agents/ai-orchestrator/AGENTS.md` |
| **project-manager** | Phase 0: Scope + Phase 6: Closure                  | `agents/project-manager/AGENTS.md` |
| **ui-ux-designer**  | Phase 0: Design Goals + Phase 5: Design Validation | `agents/ui-ux-designer/AGENTS.md`  |

---

## 🎯 Phase Summary (English)

### Phase 0: Requirements Clarification

**Goal**: Transform "what to do" into "verifiable specifications"

**Key Activities**:

- Confirm goal type (feature/bug/refactor/performance/security/API change)
- Define acceptance criteria (input/output/behavior/compatibility)
- Identify risks (consistency/reliability/security/observability)

**Stop Condition**: If information insufficient → STOP and confirm with user

---

### Phase 1: Build Context

**Goal**: Understand system layers, don't blindly change

**Key Activities**:

- Identify layer boundaries (Interface/Application/Domain/Infrastructure/Cross-cutting)
- Find existing conventions (error types, logging, transactions, config)
- Determine minimal change entry point

**Output**: Know which modules to change, which parts must remain unchanged

---

### Phase 2: Solution Design

**Goal**: Classify change type, propose options with trade-offs

**Change Types**:

- **Small**: Direct implementation, minimal changes
- **Medium**: Confirm with user before implementing
- **Large**: Design document first, get approval

**Options to Consider**:

- "New module" vs "Extend existing"
- "Config-driven" vs "Hardcoded"
- "Synchronous failure" vs "Graceful degradation"

---

### Phase 3: Micro-Design

**Goal**: Break into subtasks with verifiable results

**Standard Subtasks (A-E)**:

- **A**: Contract Alignment (parameters/return/error semantics)
- **B**: Main Logic Implementation
- **C**: Boundary Conditions & Error Handling
- **D**: Observability (logging, metrics, trace)
- **E**: Test & Validation Strategy

---

### Phase 4: Code Implementation

**Goal**: Minimal runnable increments

**Implementation Rhythm**:

1. **Complete compilation/run path** - Make it callable
2. **Implement main path** - Cover common inputs
3. **Add boundary & failure branches** - Edge cases
4. **Ensure consistency & security** - Unified error handling, prevent injection
5. **Add observability** - Logs with key info, traceable errors
6. **Minor cleanup** (last!) - No large refactoring unless required

---

### Phase 5: Test & Validation

**Goal**: Prove it doesn't break (layered verification)

**Verification Layers**: | Layer | What to Verify | |-------|----------------| | **Unit Tests** | Main logic,
boundaries, error semantics | | **Integration Tests** | Real DB/services, transactions, idempotency | | **Regression
Tests** | Old usage still works, comparison cases | | **Static Checks** | Type check, lint, formatting | | **Runtime
Verification** | Critical E2E flow passes |

**Output**: "How to verify" checklist with concrete commands

---

### Phase 6: Delivery & Communication

**Goal**: Enable fast review/merge

**Documentation**:

- Change points (which modules, why)
- Compatibility impact (old callers, error semantics)
- Verification commands/steps
- Remaining risks/uncovered cases (honestly labeled)

**Coding Style Options**:

- **Test-First** (more stable): Tests/contract → implementation → integration
- **Implementation-First** (faster): Main path → tests for key branches

---

## 🚨 Enforcement Mechanism

### Each Agent's Responsibility

**Every Session Start** (MANDATORY):

1. Read `@workspace/memory/CORE_RULES.md` (core rules)
2. Read `@workspace/agents/<agent>/AGENTS.md` (this file)
3. Read `TASK_TRACKER.md` (project status)
4. Check `PROJECT_STARTUP_CHECKLIST.md` (initialization status)
5. Review phase-specific documents

### ai-orchestrator Oversight

**Track Phase Progress** (update every 2-3 min):

```markdown
## Phase Progress

| Agent           | Current Phase | Started | Status         | Blockers |
| --------------- | ------------- | ------- | -------------- | -------- |
| product-manager | Phase 0       | 14:00   | ✅ Complete    | None     |
| architect       | Phase 1       | 14:10   | 🟡 In Progress | -        |
```

**Escalation Triggers**:

- Phase 0-3 not completed after 30 min → Remind agent
- Phase 4 started before Phase 0-3 → STOP and notify tech-leader
- Any phase blocked >30 min → Notify user

---

## 📊 Agent Responsibility Matrix

| Phase       | Primary Owner              | Reviewers          | Key Deliverables              |
| ----------- | -------------------------- | ------------------ | ----------------------------- |
| **Phase 0** | product-manager            | tech-leader        | Requirements memo, AC         |
| **Phase 1** | All agents                 | tech-leader        | Context memo                  |
| **Phase 2** | Architect                  | tech-leader + user | Solution classification       |
| **Phase 3** | All agents                 | tech-leader        | Subtasks A-E                  |
| **Phase 4** | dev-engineer               | tech-leader        | Incremental commits           |
| **Phase 5** | dev-engineer + qa-engineer | tech-leader        | Validation logs, test results |
| **Phase 6** | All agents                 | tech-leader + qa   | Delivery documentation        |

---

## 🎯 Key Principles

### Universal Rules (All Agents)

1. **Stop if unclear** - Don't guess, ask user
2. **Document everything** - TASK_TRACKER.md for all phases
3. **Incremental progress** - Small commits, frequent validation
4. **Layered verification** - Prove it doesn't break
5. **Honest communication** - Disclose risks, uncovered cases

### Security Baseline (All Agents)

- ⛔ No hardcoded secrets
- ⛔ No SQL string concatenation
- ⛔ No CORS \* + credentials
- ⛔ No auth test backdoors
- ⛔ No default-disabled security

---

## 📚 Related Documents

- **Full Chinese Version**: `/home/wufei/.openclaw/workspace/DEVELOPMENT_PROCESS_CHECKLIST.md`
- **Core Rules**: `/home/wufei/.openclaw/workspace/memory/CORE_RULES.md`
- **Project Initialization**: `/home/wufei/.openclaw/workspace/PROJECT_INITIALIZATION_GUIDE.md`
- **Process Summary**: `/home/wufei/.openclaw/workspace/PROCESS_OPTIMIZATION_SUMMARY.md`

---

**版本**: 1.0 **最后更新**: 2026-03-20 **维护者**: ai-orchestrator + tech-leader
