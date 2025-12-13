---
type: function
name: token_urlsafe
module: secrets
lineno: 60
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: token_urlsafe()

## Overview

Return a random URL-safe text string, in Base64 encoding.

The string has *nbytes* random bytes.  If *nbytes* is ``None``
or not supplied, a reasonable default is used.

>>> token_urlsafe(16)  #doctest:+SKIP
'Drmhze6EPcv0fN_81Bj-nA'

```python
def token_urlsafe(nbytes)
```

**Module:** [[Modules/secrets|secrets]]
**Type:** Module-level function
**Line:** 60
