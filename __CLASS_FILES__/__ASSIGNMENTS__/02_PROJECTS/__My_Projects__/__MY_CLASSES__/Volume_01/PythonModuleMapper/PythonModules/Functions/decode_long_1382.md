---
type: function
name: decode_long
module: pickle
lineno: 379
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: decode_long()

## Overview

Decode a long from a two's complement little-endian binary string.

>>> decode_long(b'')
0
>>> decode_long(b"\xff\x00")
255
>>> decode_long(b"\xff\x7f")
32767
>>> decode_long(b"\x00\xff")
-256
>>> decode_long(b"\x00\x80")
-32768
>>> decode_long(b"\x80")
-128
>>> decode_long(b"\x7f")
127

```python
def decode_long(data)
```

**Module:** [[Modules/pickle|pickle]]
**Type:** Module-level function
**Line:** 379
