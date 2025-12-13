---
type: function
name: read_long1
module: pickletools
lineno: 873
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_long1()

## Overview

>>> import io
>>> read_long1(io.BytesIO(b"\x00"))
0
>>> read_long1(io.BytesIO(b"\x02\xff\x00"))
255
>>> read_long1(io.BytesIO(b"\x02\xff\x7f"))
32767
>>> read_long1(io.BytesIO(b"\x02\x00\xff"))
-256
>>> read_long1(io.BytesIO(b"\x02\x00\x80"))
-32768

```python
def read_long1(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 873
