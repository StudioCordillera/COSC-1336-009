---
type: function
name: read_unicodestring4
module: pickletools
lineno: 668
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_unicodestring4()

## Overview

>>> import io
>>> s = 'abcd\uabcd'
>>> enc = s.encode('utf-8')
>>> enc
b'abcd\xea\xaf\x8d'
>>> n = bytes([len(enc), 0, 0, 0])  # little-endian 4-byte length
>>> t = read_unicodestring4(io.BytesIO(n + enc + b'junk'))
>>> s == t
True

>>> read_unicodestring4(io.BytesIO(n + enc[:-1]))
Traceback (most recent call last):
...
ValueError: expected 7 bytes in a unicodestring4, but only 6 remain

```python
def read_unicodestring4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 668
