---
type: function
name: token_bytes
module: secrets
lineno: 33
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: token_bytes()

## Overview

Return a random byte string containing *nbytes* bytes.

If *nbytes* is ``None`` or not supplied, a reasonable
default is used.

>>> token_bytes(16)  #doctest:+SKIP
b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'

```python
def token_bytes(nbytes)
```

**Module:** [[Modules/secrets|secrets]]
**Type:** Module-level function
**Line:** 33
