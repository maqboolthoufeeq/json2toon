# Publishing Guide for json2toon

This guide explains how to build and publish the `json2toon` package to PyPI.

## Prerequisites

1. **uv package manager**: Ensure `uv` is installed
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **PyPI Account**: Create accounts on:
   - TestPyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

3. **API Tokens**: Create API tokens for both:
   - TestPyPI: https://test.pypi.org/manage/account/token/
   - PyPI: https://pypi.org/manage/account/token/

## Pre-Publishing Checklist

Before publishing, ensure:

- [ ] All tests pass: `uv run pytest`
- [ ] Code is formatted: `uv run ruff format src/json2toon tests`
- [ ] No linting errors: `uv run ruff check src/json2toon tests`
- [ ] Type checking passes: `uv run mypy src/json2toon`
- [ ] Version number is updated in `pyproject.toml`
- [ ] CHANGELOG is updated (create one if needed)
- [ ] README is up-to-date
- [ ] All dependencies are correctly specified

## Building the Package

Build the distribution packages:

```bash
uv build
```

This creates two files in the `dist/` directory:
- `json2toon-X.Y.Z-py3-none-any.whl` (wheel)
- `json2toon-X.Y.Z.tar.gz` (source distribution)

## Testing the Build

### 1. Test Locally

Install the built package locally:

```bash
uv pip install dist/json2toon-*.whl
```

Test the CLI commands:

```bash
json2toon --help
toon2json --help
```

Test in Python:

```python
from json2toon import json_to_toon, toon_to_json

data = {"name": "Alice", "age": 30}
toon = json_to_toon(data)
print(toon)
# name: Alice
# age: 30

result = toon_to_json(toon)
print(result)
# {'name': 'Alice', 'age': 30}
```

### 2. Publish to TestPyPI (Recommended)

First, test the upload process with TestPyPI:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token <YOUR_TEST_PYPI_TOKEN>
```

Or configure the token in `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <YOUR_TEST_PYPI_TOKEN>

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <YOUR_PYPI_TOKEN>
```

Then upload:

```bash
uv publish --publish-url https://test.pypi.org/legacy/
```

Test installation from TestPyPI:

```bash
uv pip install --index-url https://test.pypi.org/simple/ json2toon
```

## Publishing to PyPI

Once you've tested on TestPyPI, publish to the real PyPI:

```bash
uv publish --token <YOUR_PYPI_TOKEN>
```

Or if you configured `~/.pypirc`:

```bash
uv publish
```

## Post-Publishing Steps

1. **Create a Git Tag**:
   ```bash
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```

2. **Create GitHub Release**:
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Select the tag you just created
   - Add release notes
   - Attach the built distributions from `dist/`

3. **Verify Installation**:
   ```bash
   uv pip install json2toon
   ```

4. **Update Documentation**:
   - Update README badges
   - Update version references
   - Announce the release

## Version Bumping

Update version numbers in:
1. `pyproject.toml` - `version = "X.Y.Z"`
2. `src/json2toon/__init__.py` - `__version__ = "X.Y.Z"`

Follow [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for added functionality (backwards-compatible)
- PATCH version for backwards-compatible bug fixes

## Continuous Deployment (Optional)

To automate publishing, you can set up GitHub Actions:

1. Add your PyPI API token to GitHub Secrets:
   - Go to repository Settings → Secrets and variables → Actions
   - Add secret: `PYPI_API_TOKEN`

2. Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Set up Python
        run: uv python install 3.12

      - name: Build package
        run: uv build

      - name: Publish to PyPI
        run: uv publish --token ${{ secrets.PYPI_API_TOKEN }}
```

## Troubleshooting

### Build Failures

If build fails, check:
- All dependencies are properly specified
- No syntax errors in source code
- `pyproject.toml` is valid

### Upload Rejected

Common reasons:
- Version number already exists (bump the version)
- Package name already taken (choose a different name)
- Invalid authentication token

### Installation Issues

If users report installation issues:
- Verify Python version requirements
- Check dependency compatibility
- Test installation in a fresh virtual environment

## Additional Resources

- [PyPI Help](https://pypi.org/help/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Semantic Versioning](https://semver.org/)

## Quick Reference

```bash
# Run tests
uv run pytest

# Format code
uv run ruff format src/json2toon tests

# Lint code
uv run ruff check src/json2toon tests

# Type check
uv run mypy src/json2toon

# Build package
uv build

# Publish to TestPyPI
uv publish --publish-url https://test.pypi.org/legacy/ --token <TOKEN>

# Publish to PyPI
uv publish --token <TOKEN>

# Tag release
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

## Support

For issues or questions:
- GitHub Issues: https://github.com/maqbool-tharayil/json2toon/issues
- Email: maqbool@reddoak.com
