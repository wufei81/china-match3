# API 设计与注册规范

**适用范围:** 所有 API 开发 **执行时机:** API 创建前 **责任人:** architect + tech-lead

---

## 📋 API 设计原则

### RESTful 规范

1. **资源命名**
   - 使用名词复数：`/api/v1/users`
   - 小写字母：`/api/v1/data-sources`
   - 连字符分隔：`/api/v1/temp-tables`

2. **HTTP 方法**
   - `GET`: 获取资源
   - `POST`: 创建资源
   - `PUT`: 更新资源
   - `PATCH`: 部分更新
   - `DELETE`: 删除资源

3. **状态码**
   - `200`: 成功
   - `201`: 创建成功
   - `400`: 请求错误
   - `401`: 未授权
   - `403`: 禁止访问
   - `404`: 不存在
   - `500`: 服务器错误

---

## 🔧 API 实现模板

### 标准 API 文件结构

```python
"""
模块说明 API

功能描述
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# 路由器配置
router = APIRouter(prefix="/api/v1/模块名", tags=["模块标签"])


# ========== 数据模型 ==========

class ResourceCreate(BaseModel):
    """创建资源请求"""
    name: str = Field(..., description="资源名称")
    # ... 其他字段


class ResourceResponse(BaseModel):
    """资源响应"""
    id: str
    name: str
    # ... 其他字段


# ========== API 端点 ==========

@router.get("", response_model=List[ResourceResponse])
async def list_resources():
    """
    获取资源列表

    Returns:
        资源列表
    """
    pass


@router.post("", response_model=Dict[str, Any])
async def create_resource(request: ResourceCreate):
    """
    创建资源

    Args:
        request: 创建请求

    Returns:
        创建结果
    """
    pass
```

---

## 📝 API 注册流程

### 步骤 1: 创建 API 文件

```bash
# 在 app/api/ 目录下创建
touch app/api/new_module.py
```

### 步骤 2: 定义路由器

```python
# app/api/new_module.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/new-module", tags=["新模块"])
```

### 步骤 3: 更新主应用

```python
# app/main.py

# 1. 导入路由器 (按字母顺序)
from app.api.new_module import router as new_module_router

# 2. 注册路由器 (按字母顺序)
app.include_router(new_module_router)
```

### 步骤 4: 验证注册

```bash
# 检查 API 文档
curl http://localhost:8000/docs

# 检查路由列表
curl http://localhost:8000/openapi.json
```

---

## ✅ API 注册检查清单

### 创建 API 时

- [ ] 创建 API 文件 (`app/api/模块名.py`)
- [ ] 定义路由器 (`APIRouter`)
- [ ] 实现数据模型 (`Pydantic`)
- [ ] 实现端点函数
- [ ] 添加文档字符串
- [ ] 添加类型注解

### 注册 API 时

- [ ] 导入路由器 (`from app.api.模块 import router as 模块_router`)
- [ ] 注册路由器 (`app.include_router(模块_router)`)
- [ ] 按字母顺序排列导入
- [ ] 按字母顺序排列注册
- [ ] 添加注释说明

### 验证 API 时

- [ ] 启动服务无错误
- [ ] API 文档可访问 (`/docs`)
- [ ] OpenAPI schema 正确 (`/openapi.json`)
- [ ] 端点测试通过
- [ ] 错误处理正常

---

## 🚨 常见错误与避免

### 错误 1: 导入缺失

```python
# ❌ 错误
app.include_router(new_module_router)  # NameError!

# ✅ 正确
from app.api.new_module import router as new_module_router
app.include_router(new_module_router)
```

### 错误 2: 命名冲突

```python
# ❌ 错误
from app.api.charts import router as charts_router
from app.api.charts import router as charts_router  # 重复！

# ✅ 正确
from app.api.charts import router as charts_router
```

### 错误 3: 路由冲突

```python
# ❌ 错误
router = APIRouter(prefix="/api/v1/users")
router = APIRouter(prefix="/api/v1/users")  # 重复！

# ✅ 正确
router = APIRouter(prefix="/api/v1/users")
```

---

## 📊 API 注册追踪表

| API 模块     | 文件            | 路由器变量          | 前缀                 | 状态 | 创建者       | 日期       |
| ------------ | --------------- | ------------------- | -------------------- | ---- | ------------ | ---------- |
| query        | query.py        | query_router        | /api/v1/query        | ✅   | dev-engineer | 2026-03-19 |
| data-sources | data_sources.py | data_sources_router | /api/v1/data-sources | ✅   | dev-engineer | 2026-03-20 |
| alert-db     | alert_db.py     | alert_db_router     | /api/v1/alerts       | ✅   | dev-engineer | 2026-03-20 |
| charts-db    | charts_db.py    | charts_db_router    | /api/v1/charts       | ✅   | dev-engineer | 2026-03-20 |
| temp-tables  | temp_tables.py  | temp_tables_router  | /api/v1/temp-tables  | ✅   | dev-engineer | 2026-03-20 |

---

## 🎯 自动化检查脚本

### API 注册验证脚本

```python
#!/usr/bin/env python3
"""
验证所有 API 路由器已正确注册
"""

import ast
import sys
from pathlib import Path

def check_api_registration():
    """检查 API 注册"""
    main_file = Path("app/main.py")
    api_dir = Path("app/api")

    # 获取所有 API 文件
    api_files = list(api_dir.glob("*.py"))

    # 解析 main.py
    with open(main_file) as f:
        content = f.read()

    # 检查导入
    missing_imports = []
    for api_file in api_files:
        module_name = api_file.stem
        if f"from app.api.{module_name} import router" not in content:
            missing_imports.append(module_name)

    # 检查注册
    missing_registrations = []
    for api_file in api_files:
        module_name = api_file.stem
        router_var = f"{module_name}_router"
        if f"app.include_router({router_var})" not in content:
            missing_registrations.append(module_name)

    # 输出结果
    if missing_imports:
        print("❌ 缺失导入:")
        for module in missing_imports:
            print(f"  - from app.api.{module} import router as {module}_router")

    if missing_registrations:
        print("❌ 缺失注册:")
        for module in missing_registrations:
            print(f"  - app.include_router({module}_router)")

    if not missing_imports and not missing_registrations:
        print("✅ 所有 API 已正确注册")
        return 0

    return 1

if __name__ == "__main__":
    sys.exit(check_api_registration())
```

---

## 📈 API 质量指标

| 指标           | 目标值  | 测量方式                |
| -------------- | ------- | ----------------------- |
| API 文档覆盖率 | 100%    | 有 docstring 的端点比例 |
| 类型注解覆盖率 | 100%    | 有类型注解的函数比例    |
| 测试覆盖率     | > 80%   | 单元测试覆盖的端点比例  |
| 响应时间 P99   | < 500ms | 性能测试                |
| 错误率         | < 1%    | 监控统计                |

---

**版本:** v1.0 **生效日期:** 2026-03-20 **适用范围:** 所有 API 开发 **审查周期:** 每周更新
