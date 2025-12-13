---
type: function
name: _parse_localename
module: locale
lineno: 464
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _parse_localename()

## Overview

Parses the locale code for localename and returns the
result as tuple (language code, encoding).

The localename is normalized and passed through the locale
alias engine. A ValueError is raised in case the locale name
cannot be parsed.

The language code corresponds to RFC 1766.  code and encoding
can be None in case the values cannot be determined or are
unknown to this implementation.

```python
def _parse_localename(localename)
```

**Module:** [[Modules/locale|locale]]
**Type:** Module-level function
**Line:** 464
