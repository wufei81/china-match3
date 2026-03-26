# 脚本工具集

**版本**: 1.0  
**创建日期**: 2026-03-26  
**目标**: 自动化日常任务

---

## 📁 脚本清单

### 质量检查
- **quality-gate.sh** - 自动质量门禁检查
  - Gate 3: 开发质量 (lint/test/build)
  - Gate 5: 安全检查 (密钥/健康检查/SQL 注入)
  - 使用：`./scripts/quality-gate.sh`

---

## 🚀 使用方式

### 质量检查
```bash
# 运行质量门禁
./scripts/quality-gate.sh

# 输出示例
🔍 运行质量门禁检查...

Gate 3: 开发质量检查
✅ Lint 通过
✅ 测试通过
✅ 覆盖率通过：85%
✅ 构建通过

Gate 5: 安全检查
✅ 无硬编码密钥
✅ 健康检查端点配置
✅ 无 SQL 注入风险

✅ 所有质量门禁通过
准备交付！🚀
```

---

## 📊 检查项

### Gate 3: 开发质量
| 检查项 | 工具 | 标准 |
|-------|------|------|
| Lint | ESLint | 0 errors |
| 测试 | Jest/Pytest | 100% pass |
| 覆盖率 | Coverage | ≥80% |
| 构建 | TypeScript | 0 errors |

### Gate 5: 安全
| 检查项 | 方法 | 标准 |
|-------|------|------|
| 硬编码密钥 | grep | 0 发现 |
| 健康检查 | grep | 已配置 |
| SQL 注入 | grep | 0 发现 |

---

## 🔧 维护

### 添加新检查
1. 编辑 `quality-gate.sh`
2. 添加检查逻辑
3. 测试脚本
4. 更新文档

### 自定义阈值
```bash
# 编辑 quality-gate.sh
# 修改覆盖率阈值
if (( $(echo "$COVERAGE < 85" | bc -l) )); then
  # 85% 改为 80%
fi
```

---

**维护者**: AI Orchestrator  
**最后更新**: 2026-03-26
