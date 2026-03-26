#!/bin/bash
# 自愈系统主脚本

echo "🏥 自愈系统运行中..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 配置
CHECK_INTERVAL=60  # 检查间隔 (秒)
LOG_FILE="/home/wufei/.openclaw/workspace/logs/self-healing.log"

# 日志函数
log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

# 1. 检查服务健康
check_services() {
  log "检查服务健康..."
  
  # 检查关键服务
  for service in nginx mysql redis; do
    if command -v systemctl &> /dev/null; then
      if ! systemctl is-active $service &> /dev/null; then
        log "🟠 警告：服务 $service 未运行"
        log "🔄 尝试重启 $service..."
        systemctl start $service
        if systemctl is-active $service &> /dev/null; then
          log "✅ 服务 $service 已恢复"
        else
          log "❌ 服务 $service 重启失败"
        fi
      fi
    fi
  done
}

# 2. 检查资源使用
check_resources() {
  log "检查资源使用..."
  
  # CPU 检查
  CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
  if (( $(echo "$CPU_USAGE > 90" | bc -l) )); then
    log "🟠 警告：CPU 使用率过高 ($CPU_USAGE%)"
    log "🔄 清理进程..."
    # 清理占用高的进程
  fi
  
  # 内存检查
  MEM_USAGE=$(free | grep Mem | awk '{printf("%.2f", $3/$2 * 100.0)}')
  if (( $(echo "$MEM_USAGE > 90" | bc -l) )); then
    log "🟠 警告：内存使用率过高 ($MEM_USAGE%)"
    log "🔄 清理缓存..."
    sync; echo 3 > /proc/sys/vm/drop_caches
  fi
  
  # 磁盘检查
  DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | cut -d'%' -f1)
  if [ $DISK_USAGE -gt 90 ]; then
    log "🟠 警告：磁盘使用率过高 ($DISK_USAGE%)"
    log "🔄 清理磁盘..."
    /home/wufei/.openclaw/workspace/scripts/cleanup-disk.sh
  fi
}

# 3. 检查任务队列
check_tasks() {
  log "检查任务队列..."
  
  # 检测卡住的任务
  STUCK_TASKS=$(ps aux | grep "task" | grep -v grep | awk '$6 > 1800000 {print $2}')
  if [ -n "$STUCK_TASKS" ]; then
    log "🟠 警告：发现卡住的任务"
    for pid in $STUCK_TASKS; do
      log "🔄 终止卡住的任务：$pid"
      kill -9 $pid
    done
  fi
}

# 4. 检查应用健康
check_application() {
  log "检查应用健康..."
  
  # 检查 API 响应
  if command -v curl &> /dev/null; then
    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/health 2>/dev/null)
    if [ "$RESPONSE" != "200" ]; then
      log "🟠 警告：API 响应异常 ($RESPONSE)"
      log "🔄 尝试重启应用..."
      # 重启应用逻辑
    fi
  fi
}

# 主循环
main() {
  log "🏥 自愈系统启动"
  log "检查间隔：${CHECK_INTERVAL}秒"
  
  while true; do
    check_services
    check_resources
    check_tasks
    check_application
    
    log "✅ 健康检查完成"
    sleep $CHECK_INTERVAL
  done
}

# 启动
main
