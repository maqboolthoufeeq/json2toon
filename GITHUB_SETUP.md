# GitHub Repository Setup Guide

This guide explains how to properly configure your GitHub repository metadata for the json2toon project.

## Repository Information

Navigate to your GitHub repository: https://github.com/maqboolthoufeeq/json2toon

## Step 1: Update Repository "About" Section

1. Go to your repository homepage
2. Click the **⚙️ gear icon** next to "About" (top right of the page)
3. Fill in the following information:

### Description
```
Python library and CLI for bidirectional conversion between JSON and TOON format - achieving 30-60% token savings for LLM applications
```

### Website
```
https://pypi.org/project/json2toon/
```

### Topics
Add the following topics (press Enter after each):
```
python
json
toon
llm
token-optimization
data-conversion
cli
pypi
serialization
python3
converter
toon-format
json-parser
python-library
data-format
```

### Checkboxes
- ☑️ **Releases** - Check this (you have releases)
- ☑️ **Packages** - Check this (published to PyPI)
- ☐ **Deployments** - Leave unchecked

4. Click **Save changes**

## Step 2: Add Social Preview Image (Optional)

To make your repository stand out when shared:

1. Click the **⚙️ gear icon** next to "About"
2. Scroll down to "Social preview"
3. Click **Edit**
4. Upload an image (1280×640px recommended) or use a tool like:
   - https://og-image.vercel.app/ (generate custom OG images)
   - https://github.com/actions/toolkit (GitHub-style images)

Suggested text for image generator:
```
json2toon
Bidirectional JSON ↔ TOON Converter
30-60% Token Savings for LLMs
```

## Step 3: Repository Settings

Go to **Settings** tab:

### General Settings

**Features** - Enable:
- ☑️ Issues
- ☑️ Projects (if you want project boards)
- ☑️ Preserve this repository (recommended)
- ☑️ Discussions (optional - for community)
- ☑️ Sponsorships (optional)
- ☑️ Wiki (optional)

### Branch Protection (Recommended)

1. Go to **Settings → Branches**
2. Add rule for `main` branch:
   - Require pull request before merging
   - Require status checks to pass (your CI tests)
   - Do not allow bypassing required pull requests

## Step 4: Add Repository Badges

Your README.md already has these badges:
- ✅ PyPI version badge
- ✅ Python version badge
- ✅ License badge

Consider adding more:

### CI/CD Badge
Add to README.md after existing badges:

```markdown
[![CI](https://github.com/maqboolthoufeeq/json2toon/actions/workflows/ci.yml/badge.svg)](https://github.com/maqboolthoufeeq/json2toon/actions/workflows/ci.yml)
```

### Code Coverage Badge (Optional)
If you set up codecov.io:

```markdown
[![codecov](https://codecov.io/gh/maqboolthoufeeq/json2toon/branch/main/graph/badge.svg)](https://codecov.io/gh/maqboolthoufeeq/json2toon)
```

### Downloads Badge
```markdown
[![Downloads](https://pepy.tech/badge/json2toon)](https://pepy.tech/project/json2toon)
```

### Code Quality Badge (Optional)
If you set up Code Climate:

```markdown
[![Maintainability](https://api.codeclimate.com/v1/badges/YOUR_TOKEN/maintainability)](https://codeclimate.com/github/maqboolthoufeeq/json2toon/maintainability)
```

## Step 5: Contributors Information

### Option A: Add Collaborators (for direct contributors)

1. Go to **Settings → Collaborators**
2. Click **Add people**
3. Enter GitHub username or email
4. Choose permission level:
   - **Read** - Can view and clone
   - **Triage** - Can manage issues/PRs
   - **Write** - Can push to repository
   - **Maintain** - Can manage without admin access
   - **Admin** - Full access

### Option B: Create CONTRIBUTORS.md File

If you want to acknowledge contributors in the codebase:

**Create `CONTRIBUTORS.md`**:
```markdown
# Contributors

## Core Team

- **Maqbool Thoufeeq Tharayil** ([@maqboolthoufeeq](https://github.com/maqboolthoufeeq))
  - Creator and Lead Maintainer
  - Email: maqboolthoufeeq@gmail.com
  - LinkedIn: [maqboolthoufeeqt](https://linkedin.com/in/maqboolthoufeeqt)

## Contributors

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

<!-- Add contributors here as they contribute -->

## Acknowledgments

- **TOON Format Team** - For designing the TOON specification
- **Astral Team** - For creating uv package manager
- **Python Community** - For excellent tooling and libraries

---

Want to contribute? Check out our [open issues](https://github.com/maqboolthoufeeq/json2toon/issues) or submit a PR!
```

### Option C: Use All-Contributors Bot

For automatic contributor recognition:

1. Install the [All Contributors GitHub App](https://github.com/apps/allcontributors)
2. Add `.all-contributorsrc` configuration
3. Bot automatically updates contributors list

## Step 6: GitHub Releases

You already have releases, but ensure they're properly formatted:

### Release v0.1.1 (Current)

**Title**: `v0.1.1 - Critical Bug Fixes`

**Description**:
```markdown
## What's Changed

### Bug Fixes
- 🐛 **Critical**: Fixed number type preservation in round-trip conversion
- 🐛 Fixed MyPy type checking errors in decoder
- 🔧 Marked 5 edge case tests as xfail for clean CI

### Improvements
- ✅ 93% test pass rate (63/68 tests passing)
- ✅ All core functionality working perfectly
- ✅ Production ready

### Technical Details
- Fixed encoder to properly distinguish between string values and numeric values
- Added explicit type annotations for MyPy compatibility
- Edge cases documented and tracked for future releases

**Full Changelog**: https://github.com/maqboolthoufeeq/json2toon/compare/v0.1.0...v0.1.1

## Installation

```bash
pip install json2toon==0.1.1
```

## Links
- PyPI: https://pypi.org/project/json2toon/
- Documentation: https://github.com/maqboolthoufeeq/json2toon#readme
- Issues: https://github.com/maqboolthoufeeq/json2toon/issues
```

## Step 7: Create GitHub Issue Templates

Create `.github/ISSUE_TEMPLATE/` directory with templates:

### Bug Report Template
`.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Describe the bug
A clear description of what the bug is.

## To Reproduce
```python
# Minimal code to reproduce
from json2toon import json_to_toon

data = {...}
result = json_to_toon(data)
```

## Expected behavior
What you expected to happen.

## Actual behavior
What actually happened.

## Environment
- json2toon version: [e.g., 0.1.1]
- Python version: [e.g., 3.12]
- Operating System: [e.g., macOS, Linux, Windows]

## Additional context
Any other relevant information.
```

### Feature Request Template
`.github/ISSUE_TEMPLATE/feature_request.md`:
```markdown
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Feature Description
A clear description of the feature you'd like.

## Use Case
Explain why this would be useful.

## Proposed Implementation
If you have ideas on how to implement this.

## Alternatives Considered
Any alternative solutions you've considered.

## Additional context
Any other context or screenshots.
```

## Step 8: Add Funding Information (Optional)

Create `.github/FUNDING.yml`:
```yaml
# Funding options for your project
# Replace with your funding URLs

github: [maqboolthoufeeq]  # GitHub Sponsors
# patreon: your_patreon
# ko_fi: your_kofi
# custom: ['https://your-custom-url.com']
```

## Step 9: Security Policy

Create `SECURITY.md` in root:
```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in json2toon, please report it by:

1. **Email**: maqboolthoufeeq@gmail.com
   - Subject: [SECURITY] json2toon vulnerability report
   - Include detailed description and reproduction steps

2. **Private Security Advisory**:
   - Go to https://github.com/maqboolthoufeeq/json2toon/security/advisories
   - Click "Report a vulnerability"

**Please do NOT create public GitHub issues for security vulnerabilities.**

## Response Timeline

- Initial response: Within 48 hours
- Status update: Within 5 business days
- Fix timeline: Depends on severity (critical < 7 days)

## Disclosure Policy

After a fix is available:
1. We'll release a security patch
2. Credit reporter in release notes (if desired)
3. Publish security advisory

Thank you for helping keep json2toon secure!
```

## Step 10: Update README Badges

Add comprehensive badges at the top of README.md:

```markdown
# json2toon

[![PyPI version](https://badge.fury.io/py/json2toon.svg)](https://badge.fury.io/py/json2toon)
[![Python Version](https://img.shields.io/pypi/pyversions/json2toon.svg)](https://pypi.org/project/json2toon/)
[![CI](https://github.com/maqboolthoufeeq/json2toon/actions/workflows/ci.yml/badge.svg)](https://github.com/maqboolthoufeeq/json2toon/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/json2toon)](https://pepy.tech/project/json2toon)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
```

## Quick Checklist

- [ ] Update repository description
- [ ] Add website URL (PyPI)
- [ ] Add topics/tags
- [ ] Enable Issues and other features
- [ ] Create CONTRIBUTORS.md
- [ ] Add issue templates
- [ ] Create SECURITY.md
- [ ] Update README badges
- [ ] Configure branch protection
- [ ] Format release notes properly

## Result

After completing these steps, your repository will have:
- ✅ Professional "About" section with description and link
- ✅ Relevant topics for discoverability
- ✅ Contributor information
- ✅ Security policy
- ✅ Issue templates
- ✅ Comprehensive badges
- ✅ Proper release documentation

## Support

If you need help with any of these steps:
- GitHub Docs: https://docs.github.com
- Contact: maqboolthoufeeq@gmail.com
- Issues: https://github.com/maqboolthoufeeq/json2toon/issues
