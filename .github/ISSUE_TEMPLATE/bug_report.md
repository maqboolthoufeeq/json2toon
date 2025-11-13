---
name: Bug report
about: Create a report to help us improve json2toon
title: '[BUG] '
labels: bug
assignees: ''
---

## Describe the Bug

A clear and concise description of what the bug is.

## To Reproduce

Steps to reproduce the behavior:

```python
from json2toon import json_to_toon, toon_to_json

# Minimal code example that reproduces the issue
data = {
    "example": "your data here"
}

result = json_to_toon(data)
print(result)

# What happens here?
```

## Expected Behavior

A clear and concise description of what you expected to happen.

## Actual Behavior

A clear and concise description of what actually happened.

**Error message (if any):**
```
Paste any error messages here
```

**Output:**
```
Paste the actual output here
```

## Environment

- **json2toon version**: [e.g., 0.1.1] (run `pip show json2toon`)
- **Python version**: [e.g., 3.12.1] (run `python --version`)
- **Operating System**: [e.g., macOS 14.0, Ubuntu 22.04, Windows 11]
- **Installation method**: [e.g., pip, uv]

## Additional Context

Add any other context about the problem here:
- Does this happen with specific data types?
- Is this a regression (worked in previous version)?
- Any relevant configuration options used?

## Possible Solution (Optional)

If you have an idea of what might be causing the issue or how to fix it, please share.

## Related Issues

Are there any related issues or PRs? Please link them here.

---

**Checklist before submitting:**
- [ ] I have searched existing issues to make sure this isn't a duplicate
- [ ] I have included a minimal reproducible example
- [ ] I have specified my environment details
- [ ] I have checked the [documentation](https://github.com/maqboolthoufeeq/json2toon#readme)
