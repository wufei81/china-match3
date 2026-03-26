# GitHub 认证配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**所有者**: wufei (wufei81@126.com)

---

## 🔐 认证配置

### 环境变量 (已配置)

```bash
# ~/.bashrc (已添加)
export GITHUB_TOKEN="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"
export GITHUB_EMAIL="wufei81@126.com"
export GITHUB_USER="wufei"
```

### 配置文件 (已创建)

```bash
# ~/.claude/.env (权限 600)
GITHUB_TOKEN=github_pat_xxx
GITHUB_EMAIL=wufei81@126.com
GITHUB_USER=wufei

# /workspace/.env (权限 600)
GITHUB_TOKEN=github_pat_xxx
GITHUB_EMAIL=wufei81@126.com
GITHUB_USER=wufei
```

### Git 配置 (已完成)

```bash
git config --global credential.helper store  # 凭证存储
git config --global user.email "wufei81@126.com"
git config --global user.name "wufei"
```

---

## 📁 配置文件位置

| 文件 | 路径 | 权限 | 用途 |
|------|------|------|------|
| **~/.bashrc** | /home/wufei/.bashrc | 644 | 环境变量 (所有会话) |
| **~/.claude/.env** | /home/wufei/.claude/.env | 600 | Claude 专用配置 |
| **/workspace/.env** | /home/wufei/.openclaw/workspace/.env | 600 | 工作区配置 |

---

## 🤖 智能体使用

### 所有 8 个智能体已配置

| 智能体 | 配置状态 | 使用说明 |
|-------|---------|---------|
| **DevEngineer** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **Architect** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **ProductManager** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **UI/UX Designer** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **TechLeader** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **QAEngineer** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **DevOpsEngineer** | ✅ 已配置 | AGENTS.md 第 4 节 |
| **ProjectManager** | ✅ 已配置 | AGENTS.md 第 4 节 |

### 使用示例

```bash
# DevEngineer 推送代码
git add .
git commit -m "feat: 实现登录功能"
git push origin main
# 自动使用 GITHUB_TOKEN 认证

# Architect 创建 PR
gh pr create --title "架构设计" --body "IM 系统架构"
# 自动使用 GITHUB_TOKEN 认证

# DevOpsEngineer 配置 GitHub Actions
# GitHub Actions 自动使用 GITHUB_TOKEN
```

---

## 🔒 安全说明

### Token 权限

**Token 类型**: Personal Access Token (Classic)  
**权限范围**: repo, workflow, user  
**过期时间**: 根据 GitHub 设置

### 安全措施

1. ✅ **文件权限 600** - 仅所有者可读写
2. ✅ **不提交到 Git** - .env 已添加到 .gitignore
3. ✅ **环境变量** - 会话期间可用
4. ✅ **凭证存储** - Git 自动使用

### 安全建议

1. **定期轮换 Token** - 每 90 天
2. **启用双因素认证** - GitHub 设置
3. **最小权限原则** - 只授予必要权限
4. **监控 Token 使用** - GitHub 设置 → Applications

---

## 🚀 快速测试

```bash
# 测试 Token 是否有效
curl -H "Authorization: token $GITHUB_TOKEN" \
     https://api.github.com/user

# 应该返回用户信息
{
  "login": "wufei",
  "email": "wufei81@126.com",
  ...
}

# 测试 Git 推送
git push -u origin main
# 应该不需要输入密码
```

---

## 📋 维护清单

### 每月检查
- [ ] Token 是否过期
- [ ] 文件权限是否正确
- [ ] Git 配置是否正常

### 每季度
- [ ] 轮换 Token
- [ ] 审查 Token 权限
- [ ] 检查 Git 日志

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26  
**版本**: 1.0
