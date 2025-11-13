# Quick Start Guide for json2toon

## Installation

```bash
# Using uv (recommended)
uv add json2toon

# Using pip
pip install json2toon
```

## Basic Usage

### Python API

```python
from json2toon import json_to_toon, toon_to_json

# Convert JSON to TOON
data = {
    "users": [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"}
    ]
}

toon_string = json_to_toon(data)
print(toon_string)
```

**Output:**
```
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

### Convert Back to JSON

```python
# Convert TOON back to JSON
json_data = toon_to_json(toon_string)
print(json_data)
```

**Output:**
```python
{
    'users': [
        {'id': 1, 'name': 'Alice', 'role': 'admin'},
        {'id': 2, 'name': 'Bob', 'role': 'user'}
    ]
}
```

## Command Line Usage

### json2toon Command

```bash
# Convert a JSON file to TOON
json2toon input.json -o output.toon

# From stdin
cat data.json | json2toon

# With custom indent
json2toon input.json --indent 4

# With tab delimiter
json2toon input.json --delimiter tab
```

### toon2json Command

```bash
# Convert a TOON file to JSON
toon2json input.toon -o output.json

# From stdin
cat data.toon | toon2json

# Pretty-print JSON
toon2json input.toon --pretty
```

## Configuration Options

### Encoding Options

```python
from json2toon import json_to_toon, ToonConfig

config = ToonConfig(
    indent_size=4,              # Indentation spaces (default: 2)
    delimiter="\t",             # Delimiter: ",", "\t", or "|" (default: ",")
    key_folding="safe",         # Collapse single-key chains (default: None)
    strict=True,                # Enable strict validation (default: True)
)

toon_string = json_to_toon(data, config=config)
```

### Decoding Options

```python
from json2toon import toon_to_json, ToonParseConfig

config = ToonParseConfig(
    expand_paths="safe",        # Expand dotted keys (default: None)
    strict=True,                # Strict mode validation (default: True)
)

json_data = toon_to_json(toon_string, config=config)
```

## Common Use Cases

### 1. LLM Token Optimization

```python
import json
from json2toon import json_to_toon

# Large dataset to send to LLM
data = load_large_dataset()

# Convert to TOON for 30-60% token savings
toon = json_to_toon(data)

# Send to LLM
response = llm.query(f"Analyze this data:\n{toon}")
```

### 2. Data Export

```bash
# Export database query to TOON
psql -c "SELECT * FROM users" --json | json2toon -o users.toon

# Convert back when needed
toon2json users.toon | jq '.'
```

### 3. Pipeline Processing

```bash
# Process data through multiple steps
cat data.json | \
    json2toon | \
    # ... process TOON format ... \
    toon2json | \
    # ... process JSON ...
```

## Examples

### Simple Object

**JSON:**
```json
{
  "name": "Alice",
  "age": 30
}
```

**TOON:**
```
name: Alice
age: 30
```

### Nested Object

**JSON:**
```json
{
  "user": {
    "name": "Bob",
    "active": true
  }
}
```

**TOON:**
```
user:
  name: Bob
  active: true
```

### Array of Primitives

**JSON:**
```json
{
  "tags": ["admin", "ops", "dev"]
}
```

**TOON:**
```
tags[3]: admin,ops,dev
```

### Tabular Data (Most Efficient!)

**JSON:**
```json
{
  "products": [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99}
  ]
}
```

**TOON:**
```
products[3]{id,name,price}:
  1,Laptop,999.99
  2,Mouse,29.99
  3,Keyboard,79.99
```

**Token Savings**: ~40-50% compared to formatted JSON!

## Tips & Best Practices

1. **Use TOON for LLM inputs**: Especially for uniform arrays and tabular data
2. **Tab delimiter for TSV-like data**: Use `--delimiter tab` for spreadsheet-like data
3. **Key folding for nested chains**: Enable `key_folding="safe"` for deeply nested single-key objects
4. **Strict mode**: Keep enabled (default) for data validation
5. **Round-trip testing**: Always test JSON → TOON → JSON for critical data

## Troubleshooting

### Issue: Values parsed as strings instead of numbers

TOON uses type inference. Ensure numeric values aren't quoted in the source.

### Issue: Array count mismatch error

In strict mode, array lengths must match declared length. Disable with `strict=False` or fix the data.

### Issue: Special characters not displaying correctly

Ensure files are UTF-8 encoded. TOON supports full Unicode.

## Next Steps

- Read the [full README](README.md) for detailed documentation
- Check [PUBLISHING.md](PUBLISHING.md) to publish your own packages
- See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical details
- Report issues: https://github.com/maqbool-tharayil/json2toon/issues

## Links

- **TOON Specification**: https://github.com/toon-format/spec
- **GitHub Repository**: https://github.com/maqbool-tharayil/json2toon
- **PyPI Package**: https://pypi.org/project/json2toon/

---

Happy TOONing! 🎨
