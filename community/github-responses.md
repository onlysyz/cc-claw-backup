# GitHub Community Response Templates

## Star Thank You Template

```
Hey @{{user}}! ⭐

Thanks for starring cc-claw! This really means a lot.

As a starred user, you'll get:
- Early access to new features
- Your issue reports prioritized
- Direct influence on roadmap

Want to get more involved?
- Read the docs: https://docs.cc-claw.dev
- Join Discord: https://discord.gg/cc-claw
- Check out good first issues: https://github.com/onlysyz/cc-claw/labels/good%20first%20issue

Keep an eye on your GitHub notifications - I'll DM you when we launch new features!

Happy coding! 🚀
```

## Issue Response Templates

### Bug Report Acknowledgment

```
👋 Hi @{{user}}!

Thanks for reporting this bug! I'm taking a look now.

**What I'll need:**
- CC-Claw version: `cc-claw --version`
- Python version: `python --version`
- OS: [macOS/Linux/Windows]
- Claude Code version (if known)

**Can you provide:**
1. Steps to reproduce
2. Expected vs actual behavior
3. Relevant logs (run with `cc-claw daemon --debug`)

I'll update here as I learn more. This helps us fix it faster! 🔧
```

### Bug Confirmed + Fix In Progress

```
🐛 Confirmed! I reproduced this issue on [version/OS].

Root cause: [brief explanation]

Working on a fix now. ETA: [timeframe]

Track progress: [link to PR/branch]
```

### Bug Fixed

```
✅ Fixed in #{{pr_number}}!

This was caused by [brief explanation]. The fix [what it does].

Can you test with:
```bash
pip install --upgrade cc-claw
```

Let me know if you hit any other issues!
```

### Feature Request - Considering

```
💡 Great idea! I can see how this would be useful for [use case].

I'm considering this for v{{version}}. Here's my initial thoughts:

**Pros:**
- [benefit 1]
- [benefit 2]

**Challenges:**
- [consideration 1]

**Would you be interested in:**
1. Helping test early versions?
2. Contributing code?

I'll update here as the plan develops. Thanks for the suggestion! 🙏
```

### Feature Request - Approved

```
🎉 Approved! This aligns perfectly with our roadmap.

I've labeled this as `enhancement` and added it to the [milestone/roadmap].

**Implementation plan:**
1. [step 1]
2. [step 2]

**Want to collaborate?**
PRs welcome! Check `CONTRIBUTING.md` for guidelines.
```

### Question Answered

```
@{{user}} Great question! 

[Clear answer with code example if applicable]

**Additional context:**
[Related info that might help]

Let me know if anything's still unclear! 💬
```

### Good First Issue - Welcome

```
👋 Welcome! Thanks for picking up this issue.

Here's what you need to know:

**The codebase:**
- Main entry: `client/daemon.py`
- Tests: `tests/`
- Docs: `docs/`

**Getting started:**
```bash
pip install -e ".[dev]"
pytest tests/  # Run tests first
```

**Need help?**
- Discord: https://discord.gg/cc-claw
- I'm happy to pair on this!

Feel free to ask questions here - no such thing as a dumb question for your first contribution! 🎉
```

## Pull Request Response Templates

### PR Submitted

```
🎉 Thanks for contributing, @{{user}}!

I'll review this within [timeframe]. Here's what I'm looking for:

**Review checklist:**
- [ ] Tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated if needed
- [ ] No breaking changes without good reason

**Questions I might ask:**
- Why this approach vs alternatives?
- How did you test this?
- Any edge cases to consider?

Looking forward to the review! 🚀
```

### PR Approved + Merged

```
✅ Merged! Thanks @{{user}}!

Your contribution: [brief description]

It's live in #{{commit_sha}} and will be in the next release.

Added you to `CONTRIBUTORS.md` 🎉

Thanks for making cc-claw better!
```

### PR Changes Requested

```
💬 Hey @{{user}}, thanks for this PR!

I've left some comments requesting changes:

**Main points:**
1. [comment 1]
2. [comment 2]

**How to address:**
[Specific guidance on each point]

Don't worry if you're unsure how to proceed - just ask! Happy to discuss. 💪
```

## Outage/Hotfix Response

```
🚨 Working on a hotfix for [issue] right now.

**Status:** Investigating → Fixing → Testing → Deploying

**ETA:** [timeframe]

**Workaround:**
[If available]

I'll update this thread every [frequency] until resolved.

Sorry for the inconvenience! 💜
```

## Cross-Promotion Response

```
Hey @{{user}}! Saw you mentioned cc-claw at [platform/event] - thanks for spreading the word! 🐦

If you write about it publicly, I'd love to read it! Feel free to drop the link here.

Also, want a swag pack? Just DM me with your address. 🎁
```