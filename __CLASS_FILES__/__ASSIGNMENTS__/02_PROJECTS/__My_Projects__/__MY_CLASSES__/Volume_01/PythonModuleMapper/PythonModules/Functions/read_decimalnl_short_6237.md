---
type: function
name: read_decimalnl_short
module: pickletools
lineno: 750
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_decimalnl_short()

## Overview

>>> import io
>>> read_decimalnl_short(io.BytesIO(b"1234\n56"))
1234

>>> read_decimalnl_short(io.BytesIO(b"1234L\n56"))
Traceback (most recent call last):
...
ValueError: invalid literal for int() with base 10: b'1234L'

```python
def read_decimalnl_short(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 750
