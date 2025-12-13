---
type: function
name: read_string1
module: pickletools
lineno: 409
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_string1()

## Overview

>>> import io
>>> read_string1(io.BytesIO(b"\x00"))
''
>>> read_string1(io.BytesIO(b"\x03abcdef"))
'abc'

```python
def read_string1(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 409
