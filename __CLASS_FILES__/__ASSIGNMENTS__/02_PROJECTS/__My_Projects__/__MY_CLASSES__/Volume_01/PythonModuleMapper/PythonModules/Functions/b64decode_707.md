---
type: function
name: b64decode
module: base64
lineno: 65
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: b64decode()

## Overview

Decode the Base64 encoded bytes-like object or ASCII string s.

Optional altchars must be a bytes-like object or ASCII string of length 2
which specifies the alternative alphabet used instead of the '+' and '/'
characters.

The result is returned as a bytes object.  A binascii.Error is raised if
s is incorrectly padded.

If validate is False (the default), characters that are neither in the
normal base-64 alphabet nor the alternative alphabet are discarded prior
to the padding check.  If validate is True, these non-alphabet characters
in the input result in a binascii.Error.
For more information about the strict base64 check, see:

https://docs.python.org/3.11/library/binascii.html#binascii.a2b_base64

```python
def b64decode(s, altchars, validate)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 65
