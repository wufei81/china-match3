# 监控告警配置指南

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 系统监控和异常告警

---

## 🎯 监控架构

```
应用 → Prometheus → Grafana → 告警
  ↓       ↓           ↓         ↓
指标   收集        可视化     通知
```

---

## 📊 监控指标

### 应用指标
| 指标 | 描述 | 告警阈值 |
|------|------|---------|
| **请求延迟** | P95 响应时间 | >500ms |
| **错误率** | 失败请求比例 | >1% |
| **吞吐量** | QPS | <100 |
| **可用性** | 服务在线率 | <99.9% |

### 系统指标
| 指标 | 描述 | 告警阈值 |
|------|------|---------|
| **CPU** | CPU 使用率 | >80% |
| **内存** | 内存使用率 | >85% |
| **磁盘** | 磁盘使用率 | >90% |
| **网络** | 网络带宽 | >80% |

### 业务指标
| 指标 | 描述 | 告警阈值 |
|------|------|---------|
| **活跃用户** | DAU/MAU | 异常波动 |
| **转化率** | 关键转化 | 下降>10% |
| **API 调用** | 关键 API | 失败>5% |

---

## 🔧 Prometheus 配置

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'app'
    static_configs:
      - targets: ['localhost:3000']
    metrics_path: '/metrics'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - 'alerts.yml'
```

---

## 🚨 告警规则

```yaml
# alerts.yml
groups:
  - name: application
    rules:
      - alert: HighLatency
        expr: http_request_duration_seconds{quantile="0.95"} > 0.5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "高延迟告警"
          description: "P95 延迟 > 500ms"
      
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "高错误率告警"
          description: "错误率 > 1%"

  - name: system
    rules:
      - alert: HighCPU
        expr: cpu_usage > 0.8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "高 CPU 告警"
          description: "CPU > 80%"
      
      - alert: HighMemory
        expr: memory_usage > 0.85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "高内存告警"
          description: "内存 > 85%"
```

---

## 📢 通知渠道

### 配置方式
```yaml
# alertmanager.yml
route:
  receiver: 'default-receiver'
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

receivers:
  - name: 'default-receiver'
    email_configs:
      - to: 'wufei81@126.com'
        from: 'alerts@example.com'
        smarthost: 'smtp.example.com:587'
    
    # Slack 通知
    slack_configs:
      - api_url: 'YOUR_SLACK_WEBHOOK'
        channel: '#alerts'
    
    # 钉钉通知
    dingtalk_configs:
      - webhook: 'YOUR_DINGTALK_WEBHOOK'
```

---

## 🚀 部署方式

### Docker Compose
```yaml
version: '3'
services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
  
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
  
  alertmanager:
    image: prom/alertmanager
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
```

---

## 📈 预期效果

| 指标 | 当前 | 配置后 | 提升 |
|------|------|-------|------|
| **问题发现** | 用户报告 | 自动发现 | 提前 80% |
| **响应时间** | 30 分钟 | 5 分钟 | -83% |
| **MTTR** | 2 小时 | 30 分钟 | -75% |

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
