# Kubernetes Operations Skill - K8s 运维技能

**版本**: 1.0  
**创建日期**: 2026-03-26  
**触发词**: "Kubernetes", "K8s", "容器编排", "kubernetes", "k8s ops"

---

## 🎯 技能概述

为 DevOps 工程师智能体提供 Kubernetes 运维能力，包括 K8s 集群管理、故障排查、性能优化、安全加固。

---

## 📊 核心功能

### K8s 运维清单

| 任务 | 命令/工具 | 说明 |
|------|----------|------|
| **集群健康** | `kubectl get nodes` | 节点状态 |
| **Pod 排查** | `kubectl describe pod` | Pod 详情 |
| **日志查看** | `kubectl logs` | 容器日志 |
| **资源监控** | `kubectl top` | 资源使用 |
| **事件查看** | `kubectl get events` | 集群事件 |

### 常见故障排查

```bash
# Pod 无法启动
kubectl describe pod <pod-name>
kubectl logs <pod-name> --previous

# 服务无法访问
kubectl get endpoints
kubectl get svc
kubectl get ingress

# 资源不足
kubectl top nodes
kubectl top pods
kubectl describe node <node-name>
```

---

**最后更新**: 2026-03-26  
**维护者**: DevOpsEngineer
