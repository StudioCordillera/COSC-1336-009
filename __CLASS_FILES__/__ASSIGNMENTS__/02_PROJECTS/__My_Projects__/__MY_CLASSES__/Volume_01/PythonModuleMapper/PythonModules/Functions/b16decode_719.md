---
type: function
name: b16decode
module: base64
lineno: 276
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: b16decode()

## Overview

Decode the Base16 encoded bytes-like object or ASCII string s.

Optional casefold is a flag specifying whether a lowercase alphabet is
acceptable as input.  For security purposes, the default is False.

The result is returned as a bytes object.  A binascii.Error is raised if
s is incorrectly padded or if there are non-alphabet characters present
in the input.

```python
def b16decode(s, casefold)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 276
