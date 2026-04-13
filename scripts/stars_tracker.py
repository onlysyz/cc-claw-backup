#!/usr/bin/env python3
"""CC-Claw Stars Tracker

Usage:
    python stars_tracker.py              # Show current stars
    python stars_tracker.py --update      # Update README badge
    python stars_tracker.py --log        # Log to history
    python stars_tracker.py --notify     # Send notification on milestone
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = "onlysyz/cc-claw"
README_FILE = Path(__file__).parent.parent / "README.md"
STARS_FILE = Path(__file__).parent.parent / "stars_history.json"
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK", "")


def get_stars() -> int:
    """Fetch current star count from GitHub API"""
    url = f"https://api.github.com/repos/{REPO}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CC-Claw-Stars-Tracker"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
            return data.get("stargazers_count", 0)
    except Exception as e:
        print(f"Error fetching stars: {e}")
        return 0


def load_history() -> dict:
    """Load star history from JSON file"""
    if STARS_FILE.exists():
        with open(STARS_FILE) as f:
            return json.load(f)
    return {"history": [], "milestones": []}


def save_history(history: dict):
    """Save star history to JSON file"""
    with open(STARS_FILE, "w") as f:
        json.dump(history, f, indent=2)


def log_stars(stars: int) -> dict:
    """Log current stars and check for milestones"""
    history = load_history()

    today = datetime.utcnow().strftime("%Y-%m-%d")
    entry = {
        "date": today,
        "stars": stars,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Check if already logged today
    if history["history"] and history["history"][-1]["date"] == today:
        history["history"][-1] = entry
    else:
        history["history"].append(entry)

    # Calculate daily gain
    if len(history["history"]) >= 2:
        prev_stars = history["history"][-2]["stars"]
        entry["daily_gain"] = stars - prev_stars
    else:
        entry["daily_gain"] = 0

    # Check milestones
    MILESTONES = [100, 500, 1000, 5000, 10000]
    achieved = []
    for milestone in MILESTONES:
        milestone_key = f"milestone_{milestone}"
        if stars >= milestone and not history["milestones"].get(milestone_key):
            history["milestones"][milestone_key] = {
                "date": today,
                "stars": stars
            }
            achieved.append(milestone)

    save_history(history)
    return entry, achieved


def update_readme(stars: int):
    """Update README with current star count"""
    if not README_FILE.exists():
        print("README.md not found")
        return

    with open(README_FILE) as f:
        content = f.read()

    # Update badge URL
    new_badge = f"https://img.shields.io/github/stars/{REPO}?style=for-the-badge&cacheSeconds=3600"
    old_badge_pattern = f"https://img.shields.io/github/stars/{REPO}?style=for-the-badge"

    if old_badge_pattern in content:
        content = content.replace(old_badge_pattern, new_badge)

        with open(README_FILE, "w") as f:
            f.write(content)

        print(f"Updated README badge to {stars} stars")
    else:
        print("Badge pattern not found in README")


def get_stars_badge_url(stars: int) -> str:
    """Generate Shields.io badge URL with star count"""
    return f"https://img.shields.io/github/stars/{REPO}?style=for-the-badge&label={stars}%20stars"


def notify_milestone(milestone: int):
    """Send Discord notification for milestone"""
    if not DISCORD_WEBHOOK:
        print(f"🎉 Milestone reached: {milestone} stars!")
        return

    import urllib.request
    import json

    data = {
        "content": f"🎉 **CC-Claw reached {milestone} GitHub stars!**\n\ngithub.com/{REPO}"
    }

    req = urllib.request.Request(
        DISCORD_WEBHOOK,
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=10):
            print(f"Discord notification sent for {milestone} stars")
    except Exception as e:
        print(f"Failed to send Discord notification: {e}")


def print_status(stars: int):
    """Print current status"""
    print(f"\n📊 CC-Claw Stars Tracker")
    print(f"{'='*40}")
    print(f"Repository: {REPO}")
    print(f"Current Stars: ⭐ {stars}")
    print()

    history = load_history()
    if history["history"]:
        print("Recent History:")
        for entry in history["history"][-7:]:
            date = entry["date"]
            stars_count = entry["stars"]
            gain = entry.get("daily_gain", 0)
            gain_str = f"(+{gain})" if gain > 0 else ""
            print(f"  {date}: {stars_count} stars {gain_str}")
        print()

    milestones = history.get("milestones", {})
    if milestones:
        print("Achieved Milestones:")
        for m, data in milestones.items():
            print(f"  🎯 {data['stars']} stars on {data['date']}")
        print()

    # Calculate projection
    if len(history["history"]) >= 7:
        week_ago = history["history"][-7]["stars"]
        week_gain = stars - week_ago
        daily_avg = week_gain / 7
        days_to_100 = (100 - stars) / daily_avg if daily_avg > 0 else float('inf')
        days_to_1000 = (1000 - stars) / daily_avg if daily_avg > 0 else float('inf')

        print("Projections:")
        if days_to_100 < 30:
            print(f"  📅 ~{int(days_to_100)} days to 100 stars")
        if days_to_1000 < 90:
            print(f"  📅 ~{int(days_to_1000)} days to 1,000 stars")
    print()


def main():
    parser = argparse.ArgumentParser(description="CC-Claw GitHub Stars Tracker")
    parser.add_argument("--update", action="store_true", help="Update README with current stars")
    parser.add_argument("--log", action="store_true", help="Log current stars to history")
    parser.add_argument("--notify", type=int, metavar="MILESTONE", help="Notify milestone achieved")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    stars = get_stars()

    if args.json:
        print(json.dumps({"stars": stars, "repo": REPO}))
        return

    print_status(stars)

    if args.notify:
        notify_milestone(args.notify)

    if args.update:
        update_readme(stars)

    if args.log:
        entry, achieved = log_stars(stars)
        print(f"Logged: {entry['date']} - {entry['stars']} stars (+{entry['daily_gain']})")
        for m in achieved:
            print(f"🎉 Milestone achieved: {m} stars!")
            notify_milestone(m)

    if not any([args.update, args.log, args.notify]):
        print("Use --help for options")


if __name__ == "__main__":
    main()
