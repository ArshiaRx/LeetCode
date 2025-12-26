# LeetCode Solutions (Auto-Synced)

This repository automatically syncs my **Accepted** LeetCode submissions into GitHub using a scheduled GitHub Actions workflow.

## Structure

Solutions are organized by difficulty:

- `leetcode/Easy/` - Contains README.md with stats and problem list
- `leetcode/Medium/` - Contains README.md with stats and problem list
- `leetcode/Hard/` - Contains README.md with stats and problem list

Each problem folder follows the format:

`{question_id}-{title_slug}`

Each problem folder contains:
- `README.md` - The problem statement and description
- Solution file(s) - Your accepted submissions

## Language Usage Analysis

Language distribution reports are automatically generated as README.md files:

- `leetcode/README.md` - Combined statistics for all problems
- `leetcode/Easy/README.md` - Statistics and problem list for Easy problems
- `leetcode/Medium/README.md` - Statistics and problem list for Medium problems
- `leetcode/Hard/README.md` - Statistics and problem list for Hard problems

## Notes

- Only **Accepted** submissions are synced.
- Each problem folder includes the problem statement as `README.md`.
- Sync runs on a schedule (every 30 minutes) and can also be triggered manually in the Actions tab.
- The workflow automatically organizes problems by difficulty and generates statistics.

-> Occasionally update secretKey manually
