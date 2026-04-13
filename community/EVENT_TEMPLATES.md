# CC-Claw Weekly Event Templates

## Event Calendar

| Day | Event | Time (UTC) | Duration | Channel | Purpose |
|-----|-------|------------|---------|---------|---------|
| Mon | Weekly Kickoff | 14:00 | 15 min | #events | Set intentions |
| Tue | Tip Tuesday | 17:00 | 10 min | #tips | Share knowledge |
| Wed | Contributor Wednesday | 18:00 | 30 min | #dev | Code review |
| Thu | Feedback Thursday | 16:00 | 20 min | #feedback | Product input |
| Fri | Showcase Friday | 17:00 | 45 min | #showoff | Feature projects |
| Sat | Open Office | 15:00 | 60 min | Voice | Casual chat |

---

## Monday: Weekly Kickoff

**Duration:** 15 minutes
**Purpose:** Set weekly goals and intentions

### Template
```
📅 Weekly Kickoff — [DATE]

Happy Monday! Let's start the week right! 🎯

Reply with:
1. 🎯 What goal are you setting for CC-Claw this week?
2. 🔧 What will it be working on?
3. 🚧 Any blockers you're anticipating?

I'll start 👇

[HOST'S GOAL POST]
```

### Host Post Example
```
🎯 This week I'm setting CC-Claw to:
- Complete the REST API authentication module
- Write 3 unit tests
- Document the retry configuration

What about you all? 👇
```

### Closing Template (After 15 min)
```
Thanks everyone for sharing! 🙌

Tips for the week:
- Use /progress to check CC-Claw status anytime
- Check #announcements for updates
- Need help? Post in #qa

Have a great week! 🚀
```

---

## Tuesday: Tip Tuesday

**Duration:** 10 minutes
**Purpose:** Share one useful tip or trick

### Template
```
💡 Tip Tuesday #[NUMBER]

Theme: [WEEKLY THEME]

Drop your BEST CC-Claw tip in one sentence!

Format:
- Windows: `your tip`
- macOS: `your tip`
- Linux: `your tip`

I'll start 👇

Pro tip: Use `cc-claw status --verbose` to see detailed token usage!
```

### Theme Suggestions

| Week | Theme |
|------|-------|
| 1 | Memory features |
| 2 | Goal setting |
| 3 | Error handling |
| 4 | Multi-agent tips |
| 5 | Token optimization |
| 6 | Custom tools |
| 7 | Integration tricks |
| 8 | Debugging tips |

### Tip Examples
```
💡 Setting multiple goals: cc-claw goal "build API" --priority high

💡 Check memory: cc-claw memory search "auth error"

💡 Skip retry for known errors: cc-claw config retry.skip="timeout"

💡 Use @mentions to notify specific users: cc-claw notify @user "done"
```

### Closing Template
```
Great tips everyone! 🎉

Most creative tip this week: [TIP]

Most useful tip this week: [TIP]

See you next Tuesday! 👋
```

---

## Wednesday: Contributor Wednesday

**Duration:** 30 minutes
**Purpose:** Code review, PR discussion, contribute together

### Pre-Event Message (Day Before)
```
🔧 Contributor Wednesday is tomorrow!

This week: [PR/TOPIC TO REVIEW]

If you have open PRs, bring them!
If you want to contribute, come learn!

discord.gg/cc-claw
```

### Template
```
🔧 Contributor Wednesday #X

Today we're reviewing:
[PR LINK] — [TITLE]
[ISSUE LINK] — [TITLE]

Format:
- 🐛 Bug reports: What's broken?
- 💡 Suggestions: How to fix?
- ✅ LGTM: Looks good to merge!

Let's help each other contribute! 🙌
```

### Code Review Format
```
PR: [TITLE]
Author: @username
Status: [Ready/Needs Work]

Review:
- [ ] Tests added?
- [ ] Docs updated?
- [ ] Code style OK?
- [ ] Security concerns?

Overall: [Approve/Request Changes/Needs Discussion]
```

### Closing Template
```
🔧 Contributor Wednesday Complete!

This week's merged PRs: [LIST]
New contributors: @username

Thanks for contributing! 💜

Next week: [TOPIC]
```

---

## Thursday: Feedback Thursday

**Duration:** 20 minutes
**Purpose:** Product feedback, feature requests, opinions

### Template
```
📝 Feedback Thursday #X

Theme: [SPECIFIC FEATURE/AREA]

We want to hear your honest opinions!

Questions for today:
1. [QUESTION 1]
2. [QUESTION 2]
3. [QUESTION 3]

Format:
**Q1:** [YOUR ANSWER]
**Q2:** [YOUR ANSWER]
**Q3:** [YOUR ANSWER]

No wrong answers! 💜
```

### Theme Examples

| Week | Theme |
|------|-------|
| 1 | Memory system |
| 2 | Multi-agent features |
| 3 | CLI experience |
| 4 | Documentation |
| 5 | Error messages |
| 6 | Token tracking |
| 7 | New features you want |
| 8 | Pricing (when applicable) |

### Closing Template
```
📝 Feedback Thursday Complete!

Key feedback themes:
- [THEME 1]
- [THEME 2]

This feedback goes directly to the team! 🙌

Top request: [FEATURE] — we'll track this!

Thanks for being honest! 💜
```

---

## Friday: Showcase Friday

**Duration:** 45 minutes
**Purpose:** Show off projects, get feedback, celebrate work

### Pre-Event (Morning)
```
🏆 Showcase Friday is TODAY at 5 PM UTC!

This week's theme: [THEME]

Start gathering:
📸 Screenshots
📝 Brief description
💻 Code snippets (optional)
🔗 Live demo links

Who’s showing off? 👇
```

### Event Template
```
🏆 Showcase Friday #X!

This week's theme: [THEME]

SHOW US WHAT YOU BUILT! 🚀

Format:
**Project Name:** [NAME]
**What it does:** [DESCRIPTION]
**Screenshot/Demo:** [LINK]
**CC-Claw features used:** [LIST]

Reactions:
- 🔥 = Amazing!
- 💡 = Great idea!
- 👏 = Nice work!

Let's celebrate each other's work! 🎉
```

### Submission Example
```
**Project Name:** Todo API
**What it does:** REST API for my todo app with auth
**Screenshot:** [LINK]
**CC-Claw features used:**
- Goal: "Build REST API"
- Memory: remembered auth requirements
- Multi-agent: coder + tester agents

Built overnight while I slept! 😴
```

### Winner Template
```
🏆 SHOWCASE WINNER! 🏆

This week's best project:

@username — [PROJECT NAME]

Why: [REASON]

Prize: Featured in #announcements + @power-user role!

Amazing work everyone! 🎉
```

### Closing Template
```
🏆 Showcase Friday Complete!

Thanks to everyone who shared! 🙌

Full showcase: [LINK TO MESSAGE]

Next week's theme: [THEME]

Have an amazing weekend! 👋
```

---

## Saturday: Open Office Hours

**Duration:** 60 minutes (optional voice chat)
**Purpose:** Casual conversation, troubleshooting, networking

### Template
```
🗣️ Open Office Hours — Saturday

Voice chat session for:
- Troubleshooting CC-Claw issues
- Chatting about AI/coding
- Meeting the community
- Just hanging out

No agenda — come as you are! ☕

Voice channel: #voice-general
Text backup: #random

See you at 3 PM UTC! 👋
```

### During Voice Session
```
☕ Open Office Hours is LIVE!

Currently in voice:
- @user1
- @user2

Topic: [CURRENT TOPIC or "Chilling!"]

Join us! 👋
```

### Post-Session
```
☕ Open Office Hours Complete!

Great conversations everyone!

Key topics discussed:
- [TOPIC 1]
- [TOPIC 2]

Next Saturday: Same time! 👋
```

---

## Special Events

### AMA (Ask Me Anything)

**Duration:** 60 minutes
**Host:** Founder/maintainer

```
🎙️ AMA with @username — CC-Claw Founder

Ask anything about:
- The vision behind CC-Claw
- Technical architecture
- Future plans
- Building open source
- [OTHER TOPICS]

Drop your questions below! 👇

Starting NOW — going for 1 hour!
```

### Launch Celebration

```
🎉 CC-Claw v[X.X] Launch Celebration!

What’s new:
[FEATURE 1]
[FEATURE 2]
[FEATURE 3]

Live demo in the next 30 minutes!
Join: [VOICE LINK]

Questions? Drop them below! 👇
```

### Community Hackathon

**Duration:** 48-72 hours

```
🏆 CC-Claw Community Hackathon!

Theme: [THEME]

Duration: 48 hours
Prizes:
🥇 $100 + feature spotlight
🥈 $50 + power-user role
🥉 Swag pack

Register: [FORM LINK]
Discord: discord.gg/cc-claw

Let's build something amazing! 🚀
```

---

## Event Best Practices

### Before Event
- [ ] Prepare all materials
- [ ] Test any demos
- [ ] Send reminder 1 day before
- [ ] Send reminder 1 hour before

### During Event
- [ ] Start on time
- [ ] Welcome everyone
- [ ] Guide the conversation
- [ ] Thank contributors
- [ ] Keep it focused

### After Event
- [ ] Post summary
- [ ] Share resources
- [ ] Thank participants
- [ ] Schedule next event
- [ ] Collect feedback
