---
type: function
name: urlsafe_b64decode
module: base64
lineno: 121
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: urlsafe_b64decode()

## Overview

Decode bytes using the URL- and filesystem-safe Base64 alphabet.

Argument s is a bytes-like object or ASCII string to decode.  The result
is returned as a bytes object.  A binascii.Error is raised if the input
is incorrectly padded.  Characters that are not in the URL-safe base-64
alphabet, and are not a plus '+' or slash '/', are discarded prior to the
padding check.

The alphabet uses '-' instead of '+' and '_' instead of '/'.

```python
def urlsafe_b64decode(s)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 121
