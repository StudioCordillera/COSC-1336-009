---
type: function
name: encode_long
module: pickle
lineno: 349
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: encode_long()

## Overview

Encode a long to a two's complement little-endian binary string.
Note that 0 is a special case, returning an empty string, to save a
byte in the LONG1 pickling context.

>>> encode_long(0)
b''
>>> encode_long(255)
b'\xff\x00'
>>> encode_long(32767)
b'\xff\x7f'
>>> encode_long(-256)
b'\x00\xff'
>>> encode_long(-32768)
b'\x00\x80'
>>> encode_long(-128)
b'\x80'
>>> encode_long(127)
b'\x7f'
>>>

```python
def encode_long(x)
```

**Module:** [[Modules/pickle|pickle]]
**Type:** Module-level function
**Line:** 349
