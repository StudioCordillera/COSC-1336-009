---
type: function
name: read_int4
module: pickletools
lineno: 252
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_int4()

## Overview

>>> import io
>>> read_int4(io.BytesIO(b'\xff\x00\x00\x00'))
255
>>> read_int4(io.BytesIO(b'\x00\x00\x00\x80')) == -(2**31)
True

```python
def read_int4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 252
