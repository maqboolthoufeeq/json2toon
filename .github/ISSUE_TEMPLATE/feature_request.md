---
name: Feature request
about: Suggest an idea for json2toon
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Feature Description

A clear and concise description of the feature you'd like to see in json2toon.

## Motivation / Use Case

Explain the problem you're trying to solve or the use case this feature would enable.

**Example scenario:**
```
I want to be able to [do something] so that [achieve some goal].
```

## Proposed Solution

Describe how you envision this feature working.

**Example API (if applicable):**
```python
from json2toon import json_to_toon, ToonConfig

# How would you use this feature?
config = ToonConfig(
    new_option="value"  # Your proposed feature
)

result = json_to_toon(data, config=config)
```

## Alternatives Considered

Have you considered any alternative solutions or workarounds?

- **Alternative 1**: Description
- **Alternative 2**: Description

## Implementation Details (Optional)

If you have ideas on how to implement this:

- Which files would need to be modified?
- Are there any edge cases to consider?
- Would this be a breaking change?

## Examples

Provide examples of how this feature would work:

### Example 1
**Input:**
```json
{
  "example": "data"
}
```

**Current behavior:**
```
example: data
```

**Desired behavior with new feature:**
```
# Your expected output here
```

### Example 2
<!-- Add more examples if needed -->

## Benefits

What benefits would this feature provide?

- [ ] Improves performance
- [ ] Adds new functionality
- [ ] Improves developer experience
- [ ] Increases compatibility
- [ ] Better error handling
- [ ] Other: [describe]

## Breaking Changes

Would this feature introduce any breaking changes?

- [ ] Yes - Describe the breaking changes
- [ ] No - Fully backward compatible

## Related Features

Are there any related features or issues?

- Related to #[issue number]
- Builds upon #[issue number]
- Depends on #[issue number]

## Additional Context

Add any other context, screenshots, links, or resources about the feature request here.

**References:**
- TOON spec section: [if applicable]
- Similar implementations: [links to other projects]
- Discussion: [link to discussion thread]

## Willingness to Contribute

Would you be willing to contribute this feature?

- [ ] Yes, I can submit a PR with guidance
- [ ] Yes, I can submit a complete PR
- [ ] No, but I can help with testing
- [ ] No, just suggesting the idea

---

**Checklist before submitting:**
- [ ] I have searched existing issues to avoid duplicates
- [ ] I have clearly described the use case
- [ ] I have considered alternatives
- [ ] I have provided examples
- [ ] I have checked the [TOON specification](https://github.com/toon-format/spec) for alignment
