#!/bin/bash
# 性能监控脚本

echo "📊 性能监控报告"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 缓存统计
echo "缓存统计:"
if [ -d "/home/wufei/.openclaw/workspace/cache" ]; then
  CACHE_SIZE=$(du -sh /home/wufei/.openclaw/workspace/cache 2>/dev/null | cut -f1)
  echo "  缓存大小：${CACHE_SIZE:-0}"
  
  MEMORY_CACHE=$(ls -la /home/wufei/.openclaw/workspace/cache/memory 2>/dev/null | wc -l)
  SKILLS_CACHE=$(ls -la /home/wufei/.openclaw/workspace/cache/skills 2>/dev/null | wc -l)
  CONTEXT_CACHE=$(ls -la /home/wufei/.openclaw/workspace/cache/context 2>/dev/null | wc -l)
  
  echo "  - 记忆缓存：$((MEMORY_CACHE - 3)) 项"
  echo "  - 技能缓存：$((SKILLS_CACHE - 3)) 项"
  echo "  - 上下文缓存：$((CONTEXT_CACHE - 3)) 项"
else
  echo "  缓存未启用"
fi
echo ""

# 并行处理状态
echo "并行处理:"
WORKERS=$(ps aux | grep -E "(worker|parallel)" | grep -v grep | wc -l)
echo "  当前工作线程：$WORKERS"
echo "  最大工作线程：8"
echo ""

# 模型使用统计
echo "模型使用:"
echo "  默认模型：qwen-plus"
echo "  回退模型：qwen-turbo"
echo "  高级模型：qwen-max"
echo ""

# 性能指标
echo "性能指标:"
echo "  目标响应时间：<500ms"
echo "  目标缓存命中率：>80%"
echo "  目标并行度：8"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 性能监控完成"
