---
type: function
name: read_decimalnl_long
module: pickletools
lineno: 772
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_decimalnl_long()

## Overview

>>> import io

>>> read_decimalnl_long(io.BytesIO(b"1234L\n56"))
1234

>>> read_decimalnl_long(io.BytesIO(b"123456789012345678901234L\n6"))
123456789012345678901234

```python
def read_decimalnl_long(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 772
