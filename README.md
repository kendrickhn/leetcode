Welcome to my personal LeetCode journey repository – where I track every problem I solve, whether it’s done independently or with AI help. This repo isn't just about green ticks – it’s a growing database to reflect, analyze, and visualize my progress.

---

## 📁 Repository Structure

```
leetcode-journal/
├── problems/         # Code files grouped by difficulty
│   ├── easy/
│   ├── medium/
│   └── hard/
├── solutions/        # Markdown writeups for explanation & reflection
├── progress/
│   └── log.csv       # Central progress log with problem metadata
├── visualize/
│   └── analyze_progress.ipynb  # (Coming soon) Data analysis notebook
├── log_helper.py     # Python script for quick logging of solved problems
└── README.md         # You're here!
```

---

## How I Use This Repo

### When I solve a problem:
1. Save the code to `problems/<level>/<id>_<kebab-title>_<ai/self>.py`
2. Log the problem in `progress/log.csv`
3. (Optional) Write insights in `solutions/<id>.md`

### Logging Template:
Use this Python shortcut:

```python
from log_helper import log_problem

log_problem(
    id=1234,
    title="Some Problem",
    level="Medium",
    solved_by="Self",
    date="2025-04-14",
    tags="hashmap, sliding window"
)
```

---

## Why This Journal?

- Track problem-solving consistency over time
- Reflect on what topics I struggle with most
- Balance self-solved and AI-supported learning
- Build a data source for future visualizations

---

## Goals

- 365-day LeetCode streak tracker
- 100+ hard problems solved (at least 50 self-solved)
- Progress dashboard with topics breakdown

---

Thanks for checking out my journey! Let’s grow together 💪
