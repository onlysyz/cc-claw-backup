# CC-Claw Community Engagement Workflows

## Daily Tasks (5-10 min)

### Morning (9:00 AM)
1. Check Discord for new members → Send welcome DM
2. Scan #qa for unanswered questions → Reply or assign
3. Check GitHub for new issues → Acknowledge within 1 hour

### Afternoon (2:00 PM)
1. Review GitHub PRs → Provide feedback
2. Check Discord for resolved issues → Mark as solved
3. Post engaging question in #general

### Evening (6:00 PM)
1. Review daily stats
2. Thank top contributors
3. Preview tomorrow's work

## Weekly Tasks (30 min)

### Monday: Community Pulse
- Post weekly check-in in #general
- "What did you build this weekend? Share in #showoff!"
- Review feature request votes

### Tuesday: Tutorial Tuesday
- Share a tip/trick in #general
- "Pro tip: Did you know cc-claw can..."
- Highlight useful docs

### Wednesday: Contribution Wednesday
- Review open PRs
- Reach out to contributors
- Post "good first issue" reminder

### Thursday: Feedback Thursday
- Collect feedback on recent changes
- "How's vX.X working for you?"
- Identify pain points

### Friday: Showcase Friday
- Feature best community project
- Thank weekly contributors
- Post release preview if applicable

### Weekend: Light Touch
- Check urgent issues only
- No scheduled content
- Respond to mentions

## GitHub Issue Workflow

### New Issue Received
```
Within 1 hour:
1. Acknowledge with 👋 reaction
2. Add appropriate label (bug/enhancement/question)
3. Assign milestone if applicable
4. Reply with acknowledgment template

Within 24 hours:
1. Triage (confirm/reproduce)
2. Add priority label (P0-P3)
3. Request missing info if needed
```

### Issue States
| State | Label | Action |
|-------|-------|--------|
| New | `new` | Acknowledge |
| Confirmed | `confirmed` | Working on fix |
| In Progress | `in progress` | Active development |
| Needs Info | `needs-info` | Waiting on user |
| Won't Fix | `wont-fix` | Close with reason |
| Fixed | `fixed` | Close & verify |

## Star Response Workflow

### Auto-Response (GitHub Actions)
```yaml
name: Thank Stargazers
on:
  watch:
    types: [started]

jobs:
  thank:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thanks for the ⭐! Check the README for how to get started.'
            })
```

### Manual Follow-Up (Daily)
```
For users who star (check weekly):
1. Check their profile for relevant work
2. DM them on Discord if they're a member
3. Add to stars notification list
```

## Discord Growth Campaign

### Week 1-4: Foundation
- Post server invite in README
- Post server invite in docs
- Post server invite in each article
- Post server invite on Twitter

### Week 5-8: Engagement
- Host first community event
- AMAs with maintainers
- Developer office hours

### Week 9-12: Retention
- Feature projects weekly
- Contributor recognition
- Swag for top contributors

## Content Calendar

| Day | Platform | Content |
|-----|----------|---------|
| Mon | GitHub | Release notes |
| Tue | Discord | Tutorial tip |
| Wed | GitHub | PR reviews |
| Thu | Twitter | Feature preview |
| Fri | Discord | Showcase |
| Sat | - | Rest |
| Sun | Twitter | Week recap |

## Response Time Targets

| Channel | First Response | Resolution |
|---------|---------------|------------|
| GitHub Issues | < 1 hour | < 48 hours |
| GitHub PRs | < 4 hours | < 7 days |
| Discord #qa | < 2 hours | < 24 hours |
| Discord DM | < 4 hours | < 48 hours |
| Twitter | < 8 hours | < 72 hours |

## Escalation Path

```
Community Issue
    ↓
Tier 1: Community support (answered in 2h)
    ↓
Tier 2: Core team (if no solution in 24h)
    ↓
Tier 3: Critical bug (P0 → immediate attention)
    ↓
Tier 4: Security issue (private disclosure)
```

## Metrics Dashboard

Track weekly:
- New Discord members
- Active Discord users
- GitHub stars (net change)
- GitHub issues opened/closed
- PRs merged
- Response time averages

Tools:
- Discord Insights
- GitHub API (graphql)
- Custom bot for stats
