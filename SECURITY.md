# Security Policy

## Supported Versions

We actively support the following versions of json2toon with security updates:

| Version | Supported          | Status |
| ------- | ------------------ | ------ |
| 0.1.x   | :white_check_mark: | Current stable release |
| < 0.1   | :x:                | Not supported |

## Reporting a Vulnerability

If you discover a security vulnerability in json2toon, we appreciate your help in disclosing it to us responsibly.

### How to Report

**Please do NOT create public GitHub issues for security vulnerabilities.**

Instead, use one of these methods:

#### 1. Email (Preferred)
- **Email**: maqboolthoufeeq@gmail.com
- **Subject**: `[SECURITY] json2toon vulnerability report`
- **Include**:
  - Detailed description of the vulnerability
  - Steps to reproduce the issue
  - Potential impact
  - Suggested fix (if any)
  - Your name/handle for acknowledgment (optional)

#### 2. Private Security Advisory
- Go to https://github.com/maqboolthoufeeq/json2toon/security/advisories
- Click **"Report a vulnerability"**
- Fill in the details using the provided template

### What to Include

Please provide as much information as possible:

```
- Vulnerability Type: [e.g., injection, DoS, information disclosure]
- Affected Component: [e.g., encoder, decoder, CLI]
- Affected Versions: [e.g., 0.1.0, 0.1.1]
- Attack Vector: [e.g., network, local, physical]
- Severity: [e.g., critical, high, medium, low]
- Proof of Concept: [code or steps to reproduce]
- Suggested Mitigation: [if you have ideas]
```

### Example Report

```markdown
Subject: [SECURITY] Code injection vulnerability in TOON decoder

Description:
The TOON decoder improperly sanitizes user input when parsing
certain special characters, allowing arbitrary code execution.

Affected Versions: 0.1.0, 0.1.1

Reproduction:
1. Create a TOON file with malicious payload:
   ```
   malicious: __import__('os').system('echo pwned')
   ```
2. Parse the file using toon_to_json()
3. Code is executed during parsing

Impact: Critical - allows arbitrary code execution

Suggested Fix: Validate and sanitize all input values before
parsing, especially when using eval() or exec().
```

## Response Timeline

We take security seriously and will respond promptly:

| Stage | Timeline |
|-------|----------|
| **Initial Response** | Within 48 hours |
| **Status Update** | Within 5 business days |
| **Triage & Assessment** | Within 7 days |
| **Fix Development** | Depends on severity |
| **Patch Release** | Critical: < 7 days<br>High: < 14 days<br>Medium: < 30 days<br>Low: Next release |

## Security Update Process

When a vulnerability is confirmed:

1. **Acknowledgment**: We confirm receipt and begin investigation
2. **Assessment**: We evaluate severity and impact
3. **Development**: We develop and test a fix
4. **Notification**: We notify the reporter before public disclosure
5. **Release**: We release a security patch
6. **Disclosure**: We publish a security advisory

## Disclosure Policy

### Coordinated Disclosure

We follow responsible disclosure practices:

1. **Private Fix**: We develop a fix privately
2. **Advance Notice**: Reporter gets 7-day advance notice before public disclosure
3. **Public Release**: We release the patched version
4. **Advisory**: We publish a security advisory with:
   - Vulnerability description
   - Affected versions
   - Fixed versions
   - Mitigation steps
   - Credit to reporter (if desired)

### Public Disclosure

After the patch is released, we will:
- Update the CHANGELOG
- Create a GitHub Security Advisory
- Credit the reporter in release notes (unless anonymity requested)
- Notify users through GitHub releases and PyPI

## Security Best Practices

### For Users

When using json2toon in your applications:

1. **Keep Updated**: Always use the latest stable version
   ```bash
   uv pip install --upgrade json2toon
   ```

2. **Validate Input**: Don't parse TOON from untrusted sources without validation
   ```python
   # Good: Validate before parsing
   if is_trusted_source(toon_data):
       result = toon_to_json(toon_data)
   ```

3. **Limit Scope**: Use json2toon in sandboxed environments when parsing untrusted data

4. **Monitor Dependencies**: Although json2toon has zero runtime dependencies, keep your Python version updated

5. **Enable Strict Mode**: Use strict mode for additional validation
   ```python
   config = ToonParseConfig(strict=True)
   result = toon_to_json(toon_data, config=config)
   ```

### For Contributors

When contributing to json2toon:

1. **Code Review**: All code changes require review
2. **Testing**: Write tests for security-sensitive code
3. **Input Validation**: Always validate and sanitize user input
4. **Avoid Unsafe Functions**: Don't use `eval()`, `exec()`, or similar
5. **Dependencies**: Keep dependencies minimal and audited
6. **Type Safety**: Use type hints and run mypy checks

## Known Security Considerations

### Input Parsing

json2toon parses structured text, which inherently requires careful handling:

- **No Code Execution**: json2toon does NOT use `eval()` or `exec()`
- **Type Inference**: Values are inferred as primitives (string, number, boolean, null)
- **No External Calls**: No network requests or file system access during parsing
- **Memory Safety**: Python's memory management prevents buffer overflows

### Potential Risks

Users should be aware of:

1. **Large Files**: Very large TOON files may consume significant memory
   - **Mitigation**: Limit input file size in your application

2. **Deeply Nested Structures**: Extremely nested objects may cause stack issues
   - **Mitigation**: Validate structure depth before parsing

3. **Malformed Input**: Invalid TOON syntax may raise exceptions
   - **Mitigation**: Use try-except blocks when parsing untrusted input

## Security Audit History

| Date | Auditor | Scope | Result |
|------|---------|-------|--------|
| 2025-01-13 | Internal | Code review of v0.1.1 | No issues found |
| - | - | - | Awaiting external audit |

We welcome security researchers to audit our code!

## Bug Bounty Program

We currently do not have a formal bug bounty program, but we deeply appreciate security researchers' efforts. We will:

- Acknowledge your contribution publicly (if desired)
- Credit you in release notes and security advisories
- Provide a reference/recommendation letter upon request

## Contact

For security concerns:
- **Email**: maqboolthoufeeq@gmail.com
- **GitHub**: [@maqboolthoufeeq](https://github.com/maqboolthoufeeq)

For general questions:
- **Issues**: https://github.com/maqboolthoufeeq/json2toon/issues
- **Discussions**: https://github.com/maqboolthoufeeq/json2toon/discussions

## References

- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

---

**Thank you for helping keep json2toon and its users secure!** 🔒
