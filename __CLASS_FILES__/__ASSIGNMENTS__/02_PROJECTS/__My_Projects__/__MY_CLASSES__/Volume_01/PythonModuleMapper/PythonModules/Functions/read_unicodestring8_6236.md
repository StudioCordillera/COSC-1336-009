---
type: function
name: read_unicodestring8
module: pickletools
lineno: 709
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_unicodestring8()

## Overview

>>> import io
>>> s = 'abcd\uabcd'
>>> enc = s.encode('utf-8')
>>> enc
b'abcd\xea\xaf\x8d'
>>> n = bytes([len(enc)]) + b'\0' * 7  # little-endian 8-byte length
>>> t = read_unicodestring8(io.BytesIO(n + enc + b'junk'))
>>> s == t
True

>>> read_unicodestring8(io.BytesIO(n + enc[:-1]))
Traceback (most recent call last):
...
ValueError: expected 7 bytes in a unicodestring8, but only 6 remain

```python
def read_unicodestring8(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 709
