# PinchTab 安装配置指南

## ✅ 安装完成

**版本**: pinchtab 0.8.6  
**安装时间**: 2026-03-29  
**状态**: 已安装并运行

## 📦 安装步骤

### 1. 安装 PinchTab
```bash
curl -fsSL https://pinchtab.com/install.sh | bash
```

### 2. 安装 Daemon 服务
```bash
pinchtab daemon install
```

### 3. 配置安全设置
编辑配置文件 `/home/wufei/.pinchtab/config.json`，修改 IDPI 白名单：

```json
"idpi": {
  "enabled": true,
  "allowedDomains": [
    "127.0.0.1",
    "localhost",
    "::1",
    "httpbin.org",
    "pinchtab.com",
    "example.com",
    "github.com",
    "zhihu.com",
    "bilibili.com",
    "weibo.com",
    "xiaohongshu.com",
    "douyin.com",
    "36kr.com",
    "sina.com.cn",
    "jd.com",
    "youtube.com",
    "google.com",
    "wikipedia.org"
  ],
  "strictMode": false
}
```

### 4. 启动服务
```bash
pinchtab daemon restart
```

## 🎯 常用命令

### 基础操作
```bash
# 导航到网页
pinchtab nav https://example.com

# 获取页面结构（快照）
pinchtab snap -c

# 提取页面文本
pinchtab text

# 截图
pinchtab screenshot -o output.png

# 点击元素
pinchtab click e5

# 填写表单
pinchtab fill e3 "文本内容"

# 按键操作
pinchtab press e7 Enter
```

### 快速操作
```bash
# 导航 + 分析一步完成
pinchtab quick https://example.com
```

### 查找元素
```bash
# 自然语言查找元素
pinchtab find "登录按钮"
pinchtab find "搜索框"
```

### 管理实例
```bash
# 查看实例
pinchtab instances

# 查看配置文件
pinchtab profiles

# 健康检查
pinchtab health
```

### Daemon 管理
```bash
# 查看状态
pinchtab daemon

# 重启
pinchtab daemon restart

# 停止
pinchtab daemon stop

# 卸载
pinchtab daemon uninstall
```

## 🔧 HTTP API 使用

### 认证 Token
从配置文件获取：`/home/wufei/.pinchtab/config.json`
```json
"server": {
  "token": "29f36bacb513e84930ba2fdb5decbc33ba1588207b2373fe"
}
```

### API 示例
```bash
# 健康检查
curl -H "Authorization: Bearer <token>" http://localhost:9867/health

# 导航
curl -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -X POST http://localhost:9867/nav \
  -d '{"url":"https://example.com"}'

# 获取快照
curl -H "Authorization: Bearer <token>" \
  http://localhost:9867/snapshot?filter=interactive
```

## 📊 Dashboard

访问：http://localhost:9867

需要 Token 认证（从配置文件获取）

## 🔐 安全配置

### 当前安全状态
```bash
pinchtab security
```

**默认安全设置**:
- ✅ 仅绑定 127.0.0.1（本地回环）
- ✅ API 需要认证
- ✅ 敏感端点已禁用
- ✅ IDPI 内容防护启用
- ⚠️  白名单域名已扩展（用于测试）

### 生产环境建议
1. 保持 `strictMode: true`
2. 仅允许必要的域名
3. 不要暴露到公网
4. 使用反向代理 + TLS

## 🤖 与 AI 智能体集成

### MCP (SMCP) 插件
PinchTab 提供 MCP 插件，支持 15 个工具：
- `pinchtab__navigate`
- `pinchtab__snapshot`
- `pinchtab__action`
- `pinchtab__click`
- `pinchtab__fill`
- `pinchtab__type`
- `pinchtab__press`
- `pinchtab__screenshot`
- 等等...

配置参考：`plugins/README.md`（在 PinchTab 源码中）

### 与 opencli 配合使用
```bash
# opencli 用于内容抓取
opencli zhihu hot

# pinchtab 用于交互操作
pinchtab nav https://zhihu.com
pinchtab snap -c
pinchtab click e5
```

## 📝 使用示例

### 示例 1：抓取知乎热榜
```bash
# 导航
pinchtab nav https://www.zhihu.com/hot

# 等待加载
pinchtab wait 3000

# 获取结构
pinchtab snap -c

# 提取文本
pinchtab text
```

### 示例 2：自动登录
```bash
# 导航到登录页
pinchtab nav https://example.com/login

# 查找用户名输入框
pinchtab find "用户名"

# 填写表单
pinchtab fill e1 "username"
pinchtab fill e2 "password"

# 点击登录
pinchtab click e3
```

### 示例 3：截图保存
```bash
# 导航并截图
pinchtab nav https://example.com
pinchtab screenshot -o /tmp/page.png

# 或保存为 PDF
pinchtab pdf --tab <tabId> -o output.pdf
```

## 🐛 故障排查

### 问题：导航被阻止
```
Error 403: navigation blocked by IDPI
```
**解决**: 将域名添加到 `allowedDomains` 列表

### 问题：认证失败
```
{"code":"missing_token","error":"unauthorized"}
```
**解决**: 在 API 请求中添加 `Authorization: Bearer <token>`

### 问题：服务未运行
```bash
pinchtab daemon
# 如果未运行
pinchtab daemon start
```

### 查看日志
```bash
journalctl --user -u pinchtab -f
```

## 📚 相关资源

- **官方文档**: https://pinchtab.com/docs
- **GitHub**: https://github.com/pinchtab/pinchtab
- **配置文件**: `/home/wufei/.pinchtab/config.json`
- **数据目录**: `/home/wufei/.pinchtab/`

## ⚡ 快速参考卡

```bash
# 启动/停止
pinchtab daemon start|stop|restart

# 导航
pinchtab nav <url>

# 查看
pinchtab snap          # 结构
pinchtab text          # 文本
pinchtab screenshot    # 截图

# 交互
pinchtab click <ref>   # 点击
pinchtab fill <ref> <text>  # 填写
pinchtab press <ref> <key>  # 按键

# 管理
pinchtab instances     # 实例
pinchtab profiles      # 配置
pinchtab health        # 健康
```

---

**最后更新**: 2026-03-29  
**状态**: ✅ 运行正常
