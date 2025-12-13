---
type: function
name: _dnsname_match
module: ssl
lineno: 280
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _dnsname_match()

## Overview

Matching according to RFC 6125, section 6.4.3

- Hostnames are compared lower-case.
- For IDNA, both dn and hostname must be encoded as IDN A-label (ACE).
- Partial wildcards like 'www*.example.org', multiple wildcards, sole
  wildcard or wildcards in labels other then the left-most label are not
  supported and a CertificateError is raised.
- A wildcard must match at least one character.

```python
def _dnsname_match(dn, hostname)
```

**Module:** [[Modules/ssl|ssl]]
**Type:** Module-level function
**Line:** 280
