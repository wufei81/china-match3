# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and
share skills without leaking your infrastructure.

---

## 🤖 AI Model Configuration (阿里云 DashScope)

### API Key

```bash
export DASHSCOPE_API_KEY="sk-cb651f6e342e4a80b4eb9a2185b045ab"
export OPENAI_API_KEY="$DASHSCOPE_API_KEY"
export OPENAI_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
```

### Available Models

- `qwen-plus` - 通义千问 Plus（推荐，平衡性能和成本）
- `qwen-turbo` - 通义千问 Turbo（快速，低成本）
- `qwen-max` - 通义千问 Max（最强性能）
- `qwen-long` - 长文本处理

### Usage Examples

```bash
# summarize 技能使用
summarize "https://example.com" --model openai/qwen-plus

# 或直接指定
summarize "/path/to/file.pdf" --model openai/qwen-turbo
```

---

Add whatever helps you do your job. This is your cheat sheet.
