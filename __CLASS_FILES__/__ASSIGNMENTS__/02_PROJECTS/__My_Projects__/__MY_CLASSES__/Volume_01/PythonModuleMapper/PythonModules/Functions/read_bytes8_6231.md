---
type: function
name: read_bytes8
module: pickletools
lineno: 534
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_bytes8()

## Overview

>>> import io, struct, sys
>>> read_bytes8(io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00abc"))
b''
>>> read_bytes8(io.BytesIO(b"\x03\x00\x00\x00\x00\x00\x00\x00abcdef"))
b'abc'
>>> bigsize8 = struct.pack("<Q", sys.maxsize//3)
>>> read_bytes8(io.BytesIO(bigsize8 + b"abcdef"))  #doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: expected ... bytes in a bytes8, but only 6 remain

```python
def read_bytes8(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 534
