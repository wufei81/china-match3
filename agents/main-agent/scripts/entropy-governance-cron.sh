#!/bin/bash
# 🧬 熵治理系统 - Cron 定时任务脚本
# 用法：将此脚本添加到 crontab 或通过 OpenClaw cron 管理

set -e

# 配置
WORKSPACE="/home/wufei/.openclaw/workspace/agents/main-agent"
SCRIPT_DIR="${WORKSPACE}/scripts"
GOVERNANCE_DIR="${WORKSPACE}/governance"
LOG_FILE="${GOVERNANCE_DIR}/entropy-cron.log"
REPORT_DATE=$(date +%Y%m%d)
REPORT_PATH="${GOVERNANCE_DIR}/entropy-report-${REPORT_DATE}.json"

# 确保目录存在
mkdir -p "${GOVERNANCE_DIR}"

# 记录开始时间
echo "========================================" >> "${LOG_FILE}"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 熵治理任务启动" >> "${LOG_FILE}"

# 切换到脚本目录
cd "${SCRIPT_DIR}"

# 执行治理（非交互模式）
python3 entropy-governance.py full \
  --workspace "${WORKSPACE}" \
  --auto \
  --output "${REPORT_PATH}" \
  >> "${LOG_FILE}" 2>&1

# 检查结果
if [ $? -eq 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 治理完成" >> "${LOG_FILE}"
    
    # 读取报告摘要
    if command -v jq &> /dev/null; then
        SUMMARY=$(jq -r '.summary' "${REPORT_PATH}")
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] 📊 ${SUMMARY}" >> "${LOG_FILE}"
    fi
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 治理失败" >> "${LOG_FILE}"
fi

# 清理旧报告（保留 30 天）
find "${GOVERNANCE_DIR}" -name "entropy-report-*.json" -mtime +30 -delete 2>/dev/null || true

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 任务结束" >> "${LOG_FILE}"
