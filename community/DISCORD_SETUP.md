# CC-Claw Discord Community Setup

## Server Structure

```
CC-Claw Community
├── #welcome              # Welcome messages, rules
├── #announcements        # Official announcements only
├── #releases            # Release notes feed
│
├── 📚docs/              # Documentation links
│   ├── getting-started
│   ├── api-reference
│   └── tutorials
│
├── 💬general/            # General discussion
│   ├── chat
│   ├── showoff          # Show what you built
│   └── help-others      # Community support
│
├── 🤖support/            # Getting help
│   ├── qa               # Questions & Answers
│   ├── troubleshooting
│   └── feature-requests
│
├── 🔧dev/                # Development
│   ├── internals         # Architecture discussion
│   ├── prs               # PR reviews
│   └── plugins           # Plugin development
│
├── 🏆showcase/           # Featured projects
│   ├── projects          # Community projects
│   └── blog-posts        # Articles about cc-claw
│
└── 🎉social/             # Social
    ├── twitter           # Twitter feed
    └── meetups           # Virtual meetups
```

## Role Structure

| Role | Color | Permissions | Purpose |
|------|-------|-------------|---------|
| @everyone | Gray | Basic | Default role |
| @user | Blue | Talk in chat | Verified user |
| @contributor | Purple | PR review | Contributed code |
| @beta-tester | Orange | Early access | Tested betas |
| @translator | Yellow | Translate docs | Language contributors |
| @moderator | Red | Manage | Community mods |
| @maintainer | Black | Full access | Core team |

## Welcome DM Template

```
👋 Welcome to CC-Claw Community!

Thanks for joining! Here's how to get started:

**🎯 What is CC-Claw?**
CC-Claw makes Claude Code autonomous - it works while you sleep.

**📚 Quick Start:**
1. Install: `pip install cc-claw`
2. Docs: https://docs.cc-claw.dev
3. GitHub: https://github.com/onlysyz/cc-claw

**💬 Get Involved:**
- #chat - General discussion
- #qa - Questions & answers
- #showoff - Share what you build!

**📋 Rules:**
1. Be respectful
2. No spam/self-promotion without asking
3. Use #qa for questions (not #chat)
4. Help others when you can

See you around! 🚀
```

## Verification Flow (/verify command)

```
Bot DM:
Welcome! To verify you're human:

1. What will you mainly use CC-Claw for?
   - Personal projects
   - Work projects
   - Contributing code
   - Just curious

2. (Optional) What's your GitHub handle?

[React with ✅ to confirm]
```

## Feature Request Flow

```
User posts in #feature-requests
    ↓
Bot reacts with 📋 and creates tracking issue
    ↓
Community votes with 👍/👎
    ↓
Maintainer reviews weekly
    ↓
Approved → Added to roadmap
Rejected → Explained with reasoning
```

## Announcement Template

```
📢 **CC-Claw v{{version}} Released!**

**What's New:**
{{changes}}

**Upgrade:**
pip install --upgrade cc-claw

**Migration Guide:**
{{link}}

**Known Issues:**
{{issues}}

**Thanks:**
{{contributors}}

---
Report bugs: https://github.com/onlysyz/cc-claw/issues
```

## Moderation Settings

### Anti-Spam
- Max 3 messages in 5 seconds → Warn
- Max 5 messages in 5 seconds → Mute 10min
- Max 10 messages in 5 seconds → Kick

### Auto-Moderation
- No links in #qa (except docs links)
- No @everyone/@here mentions
- No political/religious content

## Success Metrics

| Metric | Target | Weekly Check |
|--------|--------|--------------|
| Active users | 100+ | ✅ |
| Messages/week | 500+ | ✅ |
| Support response time | <2 hours | ✅ |
| Issue resolution | 80% | ✅ |
| User satisfaction | 4.5/5 | ✅ |

## Discord Bot Commands

| Command | Description | Channel |
|---------|-------------|---------|
| /verify | Verify membership | DM only |
| /stats | Your usage stats | Any |
| /invite | Get invite link | Any |
| /docs <topic> | Quick doc link | Any |
| /issue <title> | Create GitHub issue | Any |
| /feedback <text> | Submit feedback | DM only |
| /notify <version> | Get notified for release | #releases |
