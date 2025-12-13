---
type: function
name: read_bytes4
module: pickletools
lineno: 500
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_bytes4()

## Overview

>>> import io
>>> read_bytes4(io.BytesIO(b"\x00\x00\x00\x00abc"))
b''
>>> read_bytes4(io.BytesIO(b"\x03\x00\x00\x00abcdef"))
b'abc'
>>> read_bytes4(io.BytesIO(b"\x00\x00\x00\x03abcdef"))
Traceback (most recent call last):
...
ValueError: expected 50331648 bytes in a bytes4, but only 6 remain

```python
def read_bytes4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 500
