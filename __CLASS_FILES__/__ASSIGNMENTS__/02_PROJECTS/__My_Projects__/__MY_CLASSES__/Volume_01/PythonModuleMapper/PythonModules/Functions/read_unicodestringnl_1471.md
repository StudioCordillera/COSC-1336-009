---
type: function
name: read_unicodestringnl
module: pickletools
lineno: 603
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_unicodestringnl()

## Overview

>>> import io
>>> read_unicodestringnl(io.BytesIO(b"abc\\uabcd\njunk")) == 'abc\uabcd'
True

```python
def read_unicodestringnl(f)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 603
