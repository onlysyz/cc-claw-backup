# CC-Claw Discord Bot Setup & Automation

## Recommended Bots

| Bot | Purpose | Invite Link |
|-----|---------|-------------|
| MEE6 | Auto roles, moderation, leveling | mee6.xyz |
| Carl-bot | Welcome messages, logging, reaction roles | carl.gg |
| StatBot | Server analytics | statbot.net |
| Circle | Role management | circleci.com |

---

## MEE6 Configuration

### Auto-Roles
```
Level 0 (New member): @newcomer
Level 5: @member
Level 10: @helper
Level 25: @contributor
Level 50: @power-user
```

### Welcome Message
```
👋 Welcome to CC-Claw, {user}!

You're member #{member_count}!

To get started:
1. Read the rules in #rules
2. Introduce yourself in #introductions
3. Check out #getting-started

Questions? Ask in #qa!

We're glad you're here! 💜
```

### Level-Up Messages
```
🎉 {user} just reached Level {level}!

Keep being active to unlock more perks!
```

### XP Settings
```
Base XP per message: 10
Cooldown: 30 seconds
Bonus for helpful answers: +15 XP
Bonus in #showoff: +20 XP
```

---

## Carl-bot Configuration

### Welcome DM
```
👋 Welcome to CC-Claw Community!

Thanks for joining {server}! 🎉

I'm excited you're here. CC-Claw makes Claude Code work 24/7 — autonomous, persistent, and always learning.

**Quick Links:**
- 📖 Docs: docs.cc-claw.dev
- 🐙 GitHub: github.com/onlysyz/cc-claw
- 📦 PyPI: pypi.org/project/cc-claw

**Get Started:**
1. pip install cc-claw
2. cc-claw install
3. cc-claw start

**Have questions?**
- #qa — Questions & answers
- #troubleshooting — Debug help
- #feature-requests — Ideas

Can't wait to see what you build! 🚀
```

### Reaction Roles

| Emoji | Role | Channel |
|-------|------|---------|
| 💻 | Developer | #role-selection |
| 🤖 | AI Enthusiast | #role-selection |
| 📚 | Learning | #role-selection |
| 💡 | Ideas | #role-selection |
| 🔧 | Beta Tester | #role-selection |
| 📢 | Announcements | #role-selection |

### Role Selection Message
```
👋 Pick your roles!

💻 Developer — Get access to #dev channels
🤖 AI Enthusiast — AI/LLM discussion
📚 Learning — Learning resources
💡 Ideas — Feature discussions
🔧 Beta Tester — Early access to new features
📢 Announcements — Get notified of releases

React below to assign yourself roles!
```

---

## StatBot Configuration

### Dashboard Settings
```
Server ID: [YOUR SERVER ID]
Update frequency: Hourly
Public stats: Enabled
Channel: #📊stats
```

### Stats Channel Message
```
📊 CC-Claw Community Stats

👥 Members: {member_count}
🟢 Online: {online_count}
📅 Joined this week: {weekly_joins}

Last updated: {timestamp}
```

---

## Auto-Moderation Rules

### Spam Protection
```
Max messages per 10 seconds: 5
Action on exceed: Warn
Max warns before mute: 3
Mute duration: 10 minutes
```

### Link Filter
```
Allow links in: #chat, #showoff, #random
Block links in: #qa (except pypi.org, github.com, docs.cc-claw.dev)
Auto-delete invite links: Yes
```

### Mention Spam
```
Max mentions per message: 5
Max @everyone: 0
Max role mentions: 3
```

### Word Filter
```
Block: [explicit words]
Block: [spam phrases]
Warn first, then mute for: [repeated violations]
```

---

## Channel Auto-Purger

### #random (Activity Threshold)
```
Archive messages older than: 7 days
Keep pinned: Yes
Notify: No
```

### #showoff (Keep Active)
```
Archive messages older than: 30 days
Keep featured: 60 days
Auto-pin winners: Yes
```

### #qa (Keep Organized)
```
If answered and older than: 3 days
Action: React with ✅
Archive after: 7 days
```

---

## Scheduled Messages

### Daily (9 AM UTC)
```
🌅 Good morning! 

What are you building with CC-Claw today?

Drop a ⬇️ emoji to share!
```

### Daily (6 PM UTC)
```
🌙 End of day check-in!

How did CC-Claw do for you today?

✅ Completed goal
⏳ Still working
🔄 Need help

What's next? 👇
```

### Weekly (Monday 9 AM UTC)
```
📅 New week, new goals!

What should CC-Claw work on this week?

Reply with your goal and I'll track it!
```

### Weekly (Friday 5 PM UTC)
```
🏆 Showcase Friday is LIVE!

Show off what you built this week!

Format:
**Project:** [NAME]
**Screenshot:** [LINK]
**Description:** [TEXT]

Best project gets featured! 🎉
```

---

## Ticket System (For Support)

### Ticket Creation Message
```
Need help? Create a ticket!

Click the button below to open a support ticket.

A team member will respond within 24 hours.

📋 Common issues:
- Installation problems → #troubleshooting
- Feature questions → #qa
- Bugs → github.com/onlysyz/cc-claw/issues
```

### Ticket Response Template
```
Hey {user}! 👋

Thanks for creating a ticket. 

I'm looking into this now and will get back to you within 24 hours.

In the meantime:
- Can you share error logs?
- What have you tried so far?

💜
```

---

## Verification Flow

### Verification Channel (#verify)
```
🔐 Member Verification

To access the full server:

1. React with ✅ below
2. Answer: "What will you use CC-Claw for?"
3. Wait for @moderator approval

Why verify?
- Reduces spam
- Creates a trusted community
- Unlocks all channels
```

### Post-Verification DM
```
✅ Verification Complete!

You're now a verified member of CC-Claw Community.

Full access granted! 🎉

Next steps:
1. Introduce yourself in #introductions
2. Check out #getting-started
3. Ask questions in #qa

Welcome aboard! 💜
```

---

## Moderation Tools

### Mod Mail Configuration
```
Enable mod mail: Yes
Notify channel: #mod-logs
Response time target: 4 hours
Auto-close after: 7 days of inactivity
```

### Audit Log Settings
```
Track: All moderation actions
Channel: #mod-logs
Keep logs for: 90 days
```

### Moderator Commands
```
/kick @user [reason] — Remove user
/ban @user [reason] — Ban user
/mute @user [duration] — Temporarily mute
/warn @user [reason] — Issue warning
/timeout @user [duration] — Timeout user
/note @user [text] — Add moderator note
```

---

## Dashboard Configuration

### Community Insights
```
Track weekly:
- Member growth
- Message activity
- Channel popularity
- Role distribution
- Response times

Weekly report: #📊stats
Monthly report: #announcements
```

### Health Metrics
```
Active users: 70%+ of members
Help response: <2 hours
Issue resolution: 80%+
Member retention: 60%+
Net promoter score: 8+
```

---

## Integration Setup

### GitHub Integration
```
Webhook events:
- New issue → #github
- PR merged → #github
- New star → Thank reaction
- New fork → #github

Auto-post:
- Releases → #announcements
- PRs → Notify relevant contributors
```

### Twitter Integration (if available)
```
Auto-post:
- New followers → #social
- Engagement milestones → #social
- Mentions → Track for response
```

### YouTube Integration
```
New video → #announcements
New subscriber milestone → Celebrate
```

---

## Backup & Safety

### Daily Backup
```
Export:
- Member list
- Channel permissions
- Role hierarchy
- Message archives (critical channels)

Storage: Google Drive / Dropbox
Retention: 30 days
```

### Emergency Contacts
```
Owner: @onlysyz
Admin: @[name]
Moderators: @[names]
```

### Disaster Recovery
```
If server compromised:
1. Transfer ownership to backup account
2. Re-verify all members
3. Reset permissions
4. Restore from backup
```
