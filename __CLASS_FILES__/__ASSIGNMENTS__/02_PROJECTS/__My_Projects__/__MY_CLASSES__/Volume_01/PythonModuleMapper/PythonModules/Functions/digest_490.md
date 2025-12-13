---
type: function
name: digest
module: hmac
lineno: 187
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: digest()

## Overview

Fast inline implementation of HMAC.

key: bytes or buffer, The key for the keyed hash object.
msg: bytes or buffer, Input message.
digest: A hash name suitable for hashlib.new() for best performance. *OR*
        A hashlib constructor returning a new hash object. *OR*
        A module supporting PEP 247.

```python
def digest(key, msg, digest)
```

**Module:** [[Modules/hmac|hmac]]
**Type:** Module-level function
**Line:** 187
