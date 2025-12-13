---
type: function
name: token_hex
module: secrets
lineno: 47
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: token_hex()

## Overview

Return a random text string, in hexadecimal.

The string has *nbytes* random bytes, each byte converted to two
hex digits.  If *nbytes* is ``None`` or not supplied, a reasonable
default is used.

>>> token_hex(16)  #doctest:+SKIP
'f9bf78b9a18ce6d46a0cd2b0b86df9da'

```python
def token_hex(nbytes)
```

**Module:** [[Modules/secrets|secrets]]
**Type:** Module-level function
**Line:** 47
