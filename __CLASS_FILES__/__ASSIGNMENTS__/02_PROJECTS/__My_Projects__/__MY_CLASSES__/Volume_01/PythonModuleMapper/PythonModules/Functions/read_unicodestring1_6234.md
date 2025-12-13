---
type: function
name: read_unicodestring1
module: pickletools
lineno: 629
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_unicodestring1()

## Overview

>>> import io
>>> s = 'abcd\uabcd'
>>> enc = s.encode('utf-8')
>>> enc
b'abcd\xea\xaf\x8d'
>>> n = bytes([len(enc)])  # little-endian 1-byte length
>>> t = read_unicodestring1(io.BytesIO(n + enc + b'junk'))
>>> s == t
True

>>> read_unicodestring1(io.BytesIO(n + enc[:-1]))
Traceback (most recent call last):
...
ValueError: expected 7 bytes in a unicodestring1, but only 6 remain

```python
def read_unicodestring1(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 629
