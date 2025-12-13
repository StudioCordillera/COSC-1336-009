---
type: function
name: _copyfileobj_readinto
module: shutil
lineno: 176
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _copyfileobj_readinto()

## Overview

readinto()/memoryview() based variant of copyfileobj().
*fsrc* must support readinto() method and both files must be
open in binary mode.

```python
def _copyfileobj_readinto(fsrc, fdst, length)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 176
