---
type: function
name: standard_b64decode
module: base64
lineno: 98
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: standard_b64decode()

## Overview

Decode bytes encoded with the standard Base64 alphabet.

Argument s is a bytes-like object or ASCII string to decode.  The result
is returned as a bytes object.  A binascii.Error is raised if the input
is incorrectly padded.  Characters that are not in the standard alphabet
are discarded prior to the padding check.

```python
def standard_b64decode(s)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 98
