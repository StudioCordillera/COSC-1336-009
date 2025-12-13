---
type: function
name: read_float8
module: pickletools
lineno: 835
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_float8()

## Overview

>>> import io, struct
>>> raw = struct.pack(">d", -1.25)
>>> raw
b'\xbf\xf4\x00\x00\x00\x00\x00\x00'
>>> read_float8(io.BytesIO(raw + b"\n"))
-1.25

```python
def read_float8(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 835
