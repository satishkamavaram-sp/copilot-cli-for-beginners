---
name: book-summary
description: "Generates a formatted markdown summary of the book collection as a table with title, author, year, and read status. Uses ✅/❌ for read status and sorts by year."
---

# Book Summary Skill

Use this skill to generate a clear, formatted markdown summary of a book collection.

## Summary Formatting Rules

- Output a markdown table with columns: Title, Author, Year, Read
- Use ✅ for read books and ❌ for unread books in the Read column
- Sort books by year (ascending)
- Table must include a header row

## Output Format

Present the summary as:

```
## Book Collection Summary

| Title | Author | Year | Read |
|-------|--------|------|------|
| ...   | ...    | ...  | ...  |
```

