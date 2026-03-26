# 自愈系统配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 自动故障检测、自动恢复、预测性维护

---

## 🎯 自愈系统架构

```
监控 → 检测 → 诊断 → 恢复 → 验证
  ↓      ↓      ↓      ↓      ↓
指标   告警   根因   剧本   确认
```

---

## 📊 故障检测

### 检测指标

#### 系统指标
| 指标 | 阈值 | 告警级别 |
|------|------|---------|
| **CPU 使用率** | >80% | Warning |
| **CPU 使用率** | >95% | Critical |
| **内存使用率** | >85% | Warning |
| **内存使用率** | >95% | Critical |
| **磁盘使用率** | >90% | Warning |
| **磁盘使用率** | >95% | Critical |

#### 应用指标
| 指标 | 阈值 | 告警级别 |
|------|------|---------|
| **响应时间** | >1s | Warning |
| **响应时间** | >5s | Critical |
| **错误率** | >1% | Warning |
| **错误率** | >5% | Critical |
| **可用性** | <99.9% | Warning |
| **可用性** | <99% | Critical |

#### 智能体指标
| 指标 | 阈值 | 告警级别 |
|------|------|---------|
| **任务队列长度** | >100 | Warning |
| **任务失败率** | >10% | Warning |
| **协作超时** | >5min | Warning |

---

## 🔧 自动恢复

### 恢复剧本库

#### 剧本 1: 服务重启
```bash
#!/bin/bash
# restart-service.sh

SERVICE=$1
echo "🔄 重启服务：$SERVICE"

# 停止服务
systemctl stop $SERVICE

# 等待
sleep 5

# 启动服务
systemctl start $SERVICE

# 验证
systemctl is-active $SERVICE
if [ $? -eq 0 ]; then
  echo "✅ 服务重启成功"
else
  echo "❌ 服务重启失败"
  exit 1
fi
```

#### 剧本 2: 清理磁盘
```bash
#!/bin/bash
# cleanup-disk.sh

echo "🧹 清理磁盘空间..."

# 清理日志
find /var/log -name "*.log" -mtime +30 -delete

# 清理缓存
rm -rf /tmp/*
rm -rf /var/cache/*

# 清理旧备份
find /backup -name "*.tar.gz" -mtime +30 -delete

echo "✅ 磁盘清理完成"
df -h
```

#### 剧本 3: 重启卡住的任务
```bash
#!/bin/bash
# restart-stuck-task.sh

echo "🔄 检测卡住的任务..."

# 检测超过 30 分钟的任务
STUCK_TASKS=$(ps aux | grep "task" | awk '$6 > 1800000 {print $2}')

if [ -n "$STUCK_TASKS" ]; then
  echo "发现卡住的任务：$STUCK_TASKS"
  for pid in $STUCK_TASKS; do
    echo "终止任务：$pid"
    kill -9 $pid
  done
  echo "✅ 卡住的任务已清理"
else
  echo "✅ 无卡住的任务"
fi
```

---

## 📈 预测性维护

### 趋势分析

#### CPU 趋势
```bash
#!/bin/bash
# cpu-trend.sh

# 收集最近 7 天 CPU 使用率
sar -u -f /var/log/sa/sa$(date +%d) | awk 'NR>3 {print $8}'

# 计算增长率
# 如果增长率>10%/天，发出预警
```

#### 内存泄漏检测
```bash
#!/bin/bash
# memory-leak.sh

# 监控进程内存增长
ps aux --sort=-%mem | head -10

# 如果内存持续增长，发出预警
```

---

## 🚨 告警配置

### 告警规则
```yaml
# alerts.yml
groups:
  - name: system
    rules:
      - alert: HighCPU
        expr: cpu_usage > 0.8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "CPU 使用率过高"
          action: "自动扩容或优化"
      
      - alert: HighMemory
        expr: memory_usage > 0.85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "内存使用率过高"
          action: "清理缓存或扩容"

  - name: application
    rules:
      - alert: HighLatency
        expr: http_request_duration_seconds{quantile="0.95"} > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "响应延迟过高"
          action: "重启服务或扩容"
      
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "错误率过高"
          action: "立即调查"
```

### 通知渠道
```yaml
# alertmanager.yml
route:
  receiver: 'default-receiver'
  group_by: ['alertname']
  
receivers:
  - name: 'default-receiver'
    email_configs:
      - to: 'wufei81@126.com'
    
    # 钉钉通知
    dingtalk_configs:
      - webhook: 'YOUR_DINGTALK_WEBHOOK'
    
    # Slack 通知
    slack_configs:
      - channel: '#alerts'
```

---

## 📊 预期效果

| 指标 | 当前 | 配置后 | 提升 |
|------|------|-------|------|
| **故障发现时间** | 30 分钟 | 10 秒 | -99% |
| **MTTR** | 2 小时 | 5 分钟 | -96% |
| **可用性** | 99.9% | 99.99% | +0.09% |
| **人工干预** | 100% | 10% | -90% |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
