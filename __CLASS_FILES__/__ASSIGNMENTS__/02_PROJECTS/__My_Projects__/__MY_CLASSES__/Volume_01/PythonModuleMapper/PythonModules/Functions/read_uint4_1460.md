---
type: function
name: read_uint4
module: pickletools
lineno: 273
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_uint4()

## Overview

>>> import io
>>> read_uint4(io.BytesIO(b'\xff\x00\x00\x00'))
255
>>> read_uint4(io.BytesIO(b'\x00\x00\x00\x80')) == 2**31
True

```python
def read_uint4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 273
