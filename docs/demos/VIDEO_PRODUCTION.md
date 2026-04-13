# CC-Claw Video Production Guide

## Quick Video Specs

| Demo | Duration | Platform | Style |
|------|----------|----------|--------|
| Demo 1 | 4-5 min | YouTube | Tutorial |
| Demo 2 | 2-3 min | YouTube Shorts | How-to |
| Demo 3 | 4-5 min | YouTube | Tutorial |
| Demo 4 | 10-15 min | YouTube | Full tutorial |
| Demo 5 | 5-8 min | YouTube Shorts | Feature showcase |

---

## Recording Setup

### Required Software

| Tool | Purpose | Cost | Link |
|------|---------|------|------|
| OBS Studio | Screen recording | Free | obsproject.com |
| DaVinci Resolve | Video editing | Free | blackmagicdesign.com |
| ScreenToGif | Terminal GIF | Free | screentogif.com |
| Carbon | Code screenshots | Free | carbon.now.sh |

### OBS Settings

#### Screen Recording
```
Settings → Video
├── Base Resolution: 1920x1080
├── Output Resolution: 1920x1080
├── FPS: 30 (or 60 for demos)
└── Downscale Filter: Lanczos

Settings → Output
├── Output Mode: Simple
├── Recording Quality: High Quality
├── Recording Format: MP4
└── Encoder: NVENC (NVIDIA) or QuickSync (Intel)
```

#### Terminal Recording
```
For terminal demos, use 1280x720 or smaller
Font: JetBrains Mono 16pt
Background: #0D1117 (GitHub dark)
Window border: None
```

---

## Terminal Animation Scripts

### Animated Terminal Python Script

```python
#!/usr/bin/env python3
"""
CC-Claw Terminal Animator
Creates animated terminal output for demo videos
"""

import time
import sys
import os

class TerminalAnimator:
    def __init__(self, delay=0.03):
        self.delay = delay
        self.lines = []

    def print(self, text, color=None):
        """Print with optional color (ANSI)"""
        if color:
            colors = {
                'green': '\033[92m',
                'yellow': '\033[93m',
                'red': '\033[91m',
                'blue': '\033[94m',
                'bold': '\033[1m',
                'reset': '\033[0m',
            }
            text = f"{colors.get(color, '')}{text}{colors['reset']}"

        sys.stdout.write(text + '\n')
        sys.stdout.flush()
        self.lines.append(text)
        time.sleep(self.delay)

    def clear(self):
        os.system('clear')

    def save(self, filename):
        """Save transcript to file"""
        with open(filename, 'w') as f:
            f.write('\n'.join(self.lines))


def demo_autonomous_execution():
    """Demo 1: Autonomous execution"""
    t = TerminalAnimator(delay=0.02)

    t.print("[CC-CLAW] 🎯 Starting autonomous runner...")
    time.sleep(0.5)
    t.print("[CC-CLAW] ✅ Connected to server")
    t.print("[CC-CLAW] 📋 Task queue: 5 pending tasks")
    time.sleep(0.3)

    t.print("\n[CC-CLAW] 🔧 Executing: Task 1/5")
    t.print("[CC-CLAW] 📝 Creating database schema...")
    time.sleep(1)

    t.print("[CC-CLAW] ✅ Completed (2m 34s)")
    t.print("[CC-CLAW] 📊 Tokens used: 2,340")

    t.print("\n[CC-CLAW] 🔧 Executing: Task 2/5")
    t.print("[CC-CLAW] 📝 Implementing user model...")
    time.sleep(0.8)

    t.print("[CC-CLAW] ⚠️ Rate limit detected (429)")
    t.print("[CC-CLAW] ⏳ Backing off for 60s...")
    time.sleep(0.5)

    t.print("[CC-CLAW] 🔄 Retrying...")
    time.sleep(0.8)

    t.print("[CC-CLAW] ✅ Completed (3m 12s)")

    return t

def demo_memory_system():
    """Demo 5: Memory system"""
    t = TerminalAnimator(delay=0.02)

    t.print("[CC-CLAW] 🧠 Memory System Active")
    time.sleep(0.3)
    t.print("\nRecent Memories:")

    memories = [
        ("Context", "Working on payment module"),
        ("Decision", "Using Stripe instead of PayPal"),
        ("Error", "Stripe timeout - RESOLVED"),
        ("Learned", "Need webhook retry mechanism"),
    ]

    for category, content in memories:
        t.print(f"├── {category}: {content}")

    t.print("\n[CC-CLAW] Last Session: 2024-01-15 22:30")
    t.print("[CC-CLAW] ✅ Ready to resume!")

    return t

def demo_multi_agent():
    """Demo 3: Multi-agent collaboration"""
    t = TerminalAnimator(delay=0.015)

    t.print("[CC-CLAW] 🤖 Multi-Agent Collaboration")
    t.print("[CC-CLAW] 📋 Registered agents: 3")
    time.sleep(0.3)

    agents = [
        ("BackendDev", "online", "Python, FastAPI, PostgreSQL"),
        ("FrontendDev", "online", "React, TypeScript"),
        ("QAEngineer", "online", "Testing, Security"),
    ]

    for name, status, caps in agents:
        color = 'green' if status == 'online' else 'red'
        t.print(f"├── {name} [{status}] - {caps}", color=color)

    t.print("\n[CC-CLAW] 🚀 Starting workflow: Blog System")
    t.print("[CC-CLAW] 📊 Task graph: 12 tasks across 4 phases")

    phases = [
        ("Phase 1", ["Research & Planning"]),
        ("Phase 2", ["Backend API", "Frontend UI", "Test Suite"]),
        ("Phase 3", ["Integration"]),
        ("Phase 4", ["Review & Deploy"]),
    ]

    for phase_name, tasks in phases:
        t.print(f"\n{phase_name}:")
        for task in tasks:
            t.print(f"├── {task} [PENDING]")

    return t


if __name__ == "__main__":
    print("Select demo:")
    print("1: Autonomous Execution")
    print("2: Memory System")
    print("3: Multi-Agent")
    choice = input("Choice: ").strip()

    if choice == "1":
        demo_autonomous_execution()
    elif choice == "2":
        demo_memory_system()
    elif choice == "3":
        demo_multi_agent()
```

---

## Thumbnail Templates

### Template 1: "Hero Shot"
```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│     😴 (sleeping)          vs          💻 (code flying)   │
│                                                              │
│                                                              │
│   ┌────────────────────────────────────────────────────┐      │
│   │  "让 Claude Code 通宵干活"                         │      │
│   │  CC-Claw 24/7 Autonomous AI Coding                │      │
│   └────────────────────────────────────────────────────┘      │
│                                                              │
│   ⭐ github.com/onlysyz/cc-claw                           │
└──────────────────────────────────────────────────────────────┘
```

### Template 2: "Memory Brain"
```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                         🧠                                   │
│                      💭   💭                                 │
│                    💭       💭                               │
│                                                              │
│        "Claude终于记得住上下文了"                             │
│                                                              │
│        CC-Claw 持久化记忆系统                                │
│                                                              │
│   ⭐ 10,000+ GitHub Stars                                  │
└──────────────────────────────────────────────────────────────┐
```

### Template 3: "Multi-Agent"
```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│     [BackendDev]  [FrontendDev]  [QAEngineer]               │
│         🤖            🤖            🤖                        │
│           \            |            /                         │
│            \           |           /                          │
│             v         v         v                           │
│                    [Blog System]                             │
│                                                              │
│     "3个AI Agent同时工作，效率翻倍"                          │
│                                                              │
│   ⭐ github.com/onlysyz/cc-claw                           │
└──────────────────────────────────────────────────────────────┘
```

---

## YouTube Chapter Markers

### Demo 1: Autonomous Coding
```
0:00 - Intro: The Problem (Claude Code sits idle)
0:30 - Solution: What is CC-Claw?
1:00 - Live Demo: Setting a Goal
2:30 - CC-Claw Working Overnight (time-lapse)
6:00 - Morning Progress Check
8:00 - Code Review
10:00 - Summary & Stats
12:00 - CTA
```

### Demo 4: REST API in One Hour
```
0:00 - Project Introduction
1:00 - Goal Decomposition
2:30 - Task Execution (selective highlights)
5:00 - Error Handling Demo
8:00 - Progress Check
9:30 - Code Quality Showoff
11:00 - Running Tests
12:00 - API Documentation
13:00 - Summary Stats
14:00 - Links & CTA
```

---

## B-Roll Shot List

| Demo | B-Roll Needed |
|------|---------------|
| Demo 1 | Sleeping developer, coffee cup, sunrise |
| Demo 2 | Brain visualization, lightbulb moment |
| Demo 3 | Team collaboration, multiple screens |
| Demo 4 | Fast-forward clock, code flying |
| Demo 5 | Memory bank, connecting wires |

### Free B-Roll Sources

1. **Pexels**: pexels.com/videos
2. **Pixabay**: pixabay.com/videos
3. **Coverr**: coverr.co
4. **Videvo**: videvo.net

### Search Terms
- "developer working late"
- "artificial intelligence brain"
- "code programming"
- "clock time lapse"
- "team collaboration"

---

## Audio Narration Guide

### Recording Tips

1. **Use a decent microphone** - Blue Yeti or Audio-Technica AT2020
2. **Quiet room** - Minimize background noise
3. **Speak clearly** - Not too fast, not too slow
4. **Enthusiasm** - Be excited about what you're showing!

### Voiceover Timing

For 10-minute video:
- Script should be ~1,500 words
- Reading pace: ~150 words/minute
- Practice reading script 2-3 times before recording

### Background Music

Royalty-free options:
- **Epidemic Sound**: epidemicsound.com
- **Artlist**: artlist.io
- **YouTube Audio Library**: Free, in YouTube Studio

Recommended style:
- Upbeat electronic for intros
- Calm ambient for explanations
- Triumphant for conclusions

---

## Post-Production Checklist

### Editing (DaVinci Resolve)
- [ ] Trim dead space at start/end
- [ ] Add B-roll cutaways
- [ ] Add text overlays for key points
- [ ] Add chapter markers
- [ ] Color correct (match terminal to branding)
- [ ] Add background music (duck under narration)
- [ ] Add sound effects (optional)

### Export Settings
```
YouTube 1080p:
├── Resolution: 1920x1080
├── Frame Rate: 30fps
├── Codec: H.264
├── Audio: AAC 320kbps
└── Bitrate: 8-12 Mbps
```

### Thumbnail
- [ ] 1280x720px
- [ ] Bold text (60pt minimum)
- [ ] Face or product shot
- [ ] Consistent branding

### YouTube Upload
- [ ] Title with keywords
- [ ] Description with timestamps
- [ ] Tags (15-20)
- [ ] Category: Science & Technology
- [ ] End screen + cards

---

## Quick Start Recording (5 minutes)

If short on time, record this simple demo:

```
Title: CC-Claw 5-Minute Quick Start

0:00 - Show terminal, type "cc-claw goal 'hello world'"
0:30 - Show CC-Claw decomposing
1:00 - Show first task executing
2:00 - Show progress command
3:00 - Show memory command
4:00 - Quick summary + GitHub link
```

---

## Recording Equipment

### Budget Option (<$100)
- USB Microphone: AntLion Bitmotion (~$50)
- Ring Light: Neewer 10" (~$30)
- Backdrop: Savage Seamless paper (~$20)

### Pro Option ($500+)
- Microphone: Shure SM7B (~$400)
- Audio Interface: Focusrite Scarlett 2i2 (~$150)
- Boom Arm: Rode PSA1 (~$100)
- Acoustic Treatment: Rockville acoustic foam (~$100)

### Minimum (Phone Only)
- Use phone camera
- Natural lighting near window
- Quiet room
- iMovie for editing (free)