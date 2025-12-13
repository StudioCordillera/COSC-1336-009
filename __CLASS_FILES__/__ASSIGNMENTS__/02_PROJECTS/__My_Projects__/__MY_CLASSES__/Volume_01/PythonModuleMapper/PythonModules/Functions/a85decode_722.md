---
type: function
name: a85decode
module: base64
lineno: 367
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: a85decode()

## Overview

Decode the Ascii85 encoded bytes-like object or ASCII string b.

foldspaces is a flag that specifies whether the 'y' short sequence should be
accepted as shorthand for 4 consecutive spaces (ASCII 0x20). This feature is
not supported by the "standard" Adobe encoding.

adobe controls whether the input sequence is in Adobe Ascii85 format (i.e.
is framed with <~ and ~>).

ignorechars should be a byte string containing characters to ignore from the
input. This should only contain whitespace characters, and by default
contains all whitespace characters in ASCII.

The result is returned as a bytes object.

```python
def a85decode(b)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 367
