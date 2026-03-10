---
name: quick-review
description: "Quickly review Python code for common quality issues: bare except clauses, missing type hints, and unclear variable names."
---

# Quick Review Skill

Use this skill to rapidly check Python code for the following issues:

## Quick Review Checklist

- [ ] No bare except clauses
- [ ] All functions and methods have type hints
- [ ] Variable names are clear and descriptive

## Output Format

Present findings as:

```
## Quick Review: [filename]

### Bare Except Clauses
- [PASS/FAIL] Description

### Type Hints
- [PASS/FAIL] Description

### Variable Names
- [PASS/FAIL] Description

### Summary
[X] items need attention before merge
```
