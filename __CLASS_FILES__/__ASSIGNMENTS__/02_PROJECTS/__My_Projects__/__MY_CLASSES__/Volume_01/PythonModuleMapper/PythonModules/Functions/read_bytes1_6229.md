---
type: function
name: read_bytes1
module: pickletools
lineno: 472
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_bytes1()

## Overview

>>> import io
>>> read_bytes1(io.BytesIO(b"\x00"))
b''
>>> read_bytes1(io.BytesIO(b"\x03abcdef"))
b'abc'

```python
def read_bytes1(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 472
