---
type: function
name: read_bytearray8
module: pickletools
lineno: 569
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_bytearray8()

## Overview

>>> import io, struct, sys
>>> read_bytearray8(io.BytesIO(b"\x00\x00\x00\x00\x00\x00\x00\x00abc"))
bytearray(b'')
>>> read_bytearray8(io.BytesIO(b"\x03\x00\x00\x00\x00\x00\x00\x00abcdef"))
bytearray(b'abc')
>>> bigsize8 = struct.pack("<Q", sys.maxsize//3)
>>> read_bytearray8(io.BytesIO(bigsize8 + b"abcdef"))  #doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: expected ... bytes in a bytearray8, but only 6 remain

```python
def read_bytearray8(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 569
