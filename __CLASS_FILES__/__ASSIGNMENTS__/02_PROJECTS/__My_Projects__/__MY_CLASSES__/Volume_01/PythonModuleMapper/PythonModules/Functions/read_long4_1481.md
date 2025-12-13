---
type: function
name: read_long4
module: pickletools
lineno: 905
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_long4()

## Overview

>>> import io
>>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\xff\x00"))
255
>>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\xff\x7f"))
32767
>>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\x00\xff"))
-256
>>> read_long4(io.BytesIO(b"\x02\x00\x00\x00\x00\x80"))
-32768
>>> read_long1(io.BytesIO(b"\x00\x00\x00\x00"))
0

```python
def read_long4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 905
