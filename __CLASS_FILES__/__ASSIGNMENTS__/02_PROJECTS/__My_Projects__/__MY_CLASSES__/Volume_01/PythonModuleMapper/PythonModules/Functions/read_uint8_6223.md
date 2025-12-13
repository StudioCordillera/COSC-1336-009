---
type: function
name: read_uint8
module: pickletools
lineno: 294
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_uint8()

## Overview

>>> import io
>>> read_uint8(io.BytesIO(b'\xff\x00\x00\x00\x00\x00\x00\x00'))
255
>>> read_uint8(io.BytesIO(b'\xff' * 8)) == 2**64-1
True

```python
def read_uint8(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 294
