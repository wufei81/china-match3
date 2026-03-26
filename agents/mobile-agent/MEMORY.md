# MEMORY.md — 长期记忆

## 关于用户
- 用户名：待补充
- 时区：Asia/Shanghai
- 语言：中文
- 偏好：简洁表达，注重结果

## 活跃项目

### 1. 语音识别服务 (ASR)
- **状态**: 模型已下载完成
- **模型**: SenseVoiceSmall (1.8GB)
- **路径**: `/home/wufei/funasr-nano/`
- **支持语言**: 普通话、粤语、英语、日语、韩语
- **待办**: 测试方言识别（四川话、贵州话、湖南话）

### 2. 智能体记忆系统
- **状态**: 已配置
- **插件**: memory-qdrant + memory-setup
- **存储**: 本地 Qdrant (无需 API 密钥)
- **特性**: 语义搜索、自动回忆

## 已安装技能
- ✅ memory-qdrant - 本地向量记忆
- ✅ memory-setup - 记忆配置管理

## 决策与经验

### 模型下载
- 优先使用清华镜像源
- 大文件下载设置 1 小时超时
- 支持断点续传 (git lfs)

### 智能体超时配置
- 下载任务：60 分钟
- 代码实现：15 分钟
- 测试套件：20 分钟
- 复杂架构：15-20 分钟

## 偏好设置
- 下载完成/失败立即通知
- 每 2-3 分钟主动汇报进度
- 核心信息在前 3 行
- 使用 emoji 增强可读性

## 工具配置
- FunASR v1.3.1 已安装
- Git LFS 已安装
- 阿里云 DashScope API 已配置
- **Firecrawl API 已配置** - 所有智能体首选搜索技能
  - API Key: `fc-350fdbdce4bb445a94744c3ce69be452`
  - 已配置智能体：mobile-agent, ai-orchestrator, architect, dev-engineer, devops-engineer, product-manager, project-manager, qa-engineer, tech-leader, ui-ux-designer
