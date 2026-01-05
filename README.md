# LeetCode Solutions (Auto-Synced)

This repository automatically syncs my **Accepted** LeetCode submissions into GitHub using a scheduled GitHub Actions workflow.

CPS688 - ADVANCED Algorithms:  One of the great courses I took from TMU (Toronto Metropolitan University) formerly RyersonU taught by **Dr. [Claude Gravel](https://www.torontomu.ca/cs/our-people/claude-gravel/)**

## Structure

Solutions are organized by difficulty:

- `leetcode/Easy/` - Contains README.md with stats and problem list
- `leetcode/Medium/` - Contains README.md with stats and problem list
- `leetcode/Hard/` - Contains README.md with stats and problem list

Each problem folder follows the format:

`{question_id}-{title_slug}`

Each problem folder contains:
- `README.md` - The problem statement and description
- Solution file(s) - My accepted submissions

## Language Usage Analysis

Language distribution reports are automatically generated as README.md files:

- `leetcode/README.md` - Combined statistics for all problems
- `leetcode/Easy/README.md` - Statistics and problem list for Easy problems
- `leetcode/Medium/README.md` - Statistics and problem list for Medium problems
- `leetcode/Hard/README.md` - Statistics and problem list for Hard problems


<p align="center">
  <img src="https://leetcard.jacoblin.cool/ArshiaRx?theme=dark&font=Fira%20Sans%20Extra%20Condensed&border=0&colors=0d1117,30363d,2ea043,d29922,f85149,c9d1d9,58a6ff,39d353" width="60%" />
</p>


- Only **Accepted** submissions are synced.
- Each problem folder includes the problem statement as `README.md`.
- Sync runs on a schedule (every 30 minutes) and can also be triggered manually in the Actions tab.
- The workflow automatically organizes problems by difficulty and generates statistics.

-> Occasionally update secretKey manually
