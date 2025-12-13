---
type: function
name: uname
module: platform
lineno: 968
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: uname()

## Overview

Fairly portable uname interface. Returns a tuple
of strings (system, node, release, version, machine, processor)
identifying the underlying platform.

Note that unlike the os.uname function this also returns
possible processor information as an additional tuple entry.

Entries which cannot be determined are set to ''.

```python
def uname()
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 968
