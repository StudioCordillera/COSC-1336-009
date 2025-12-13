---
type: function
name: read_uint2
module: pickletools
lineno: 231
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_uint2()

## Overview

>>> import io
>>> read_uint2(io.BytesIO(b'\xff\x00'))
255
>>> read_uint2(io.BytesIO(b'\xff\xff'))
65535

```python
def read_uint2(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 231
