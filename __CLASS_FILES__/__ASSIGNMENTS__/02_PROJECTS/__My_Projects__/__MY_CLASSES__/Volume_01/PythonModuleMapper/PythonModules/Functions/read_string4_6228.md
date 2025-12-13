---
type: function
name: read_string4
module: pickletools
lineno: 438
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_string4()

## Overview

>>> import io
>>> read_string4(io.BytesIO(b"\x00\x00\x00\x00abc"))
''
>>> read_string4(io.BytesIO(b"\x03\x00\x00\x00abcdef"))
'abc'
>>> read_string4(io.BytesIO(b"\x00\x00\x00\x03abcdef"))
Traceback (most recent call last):
...
ValueError: expected 50331648 bytes in a string4, but only 6 remain

```python
def read_string4(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 438
