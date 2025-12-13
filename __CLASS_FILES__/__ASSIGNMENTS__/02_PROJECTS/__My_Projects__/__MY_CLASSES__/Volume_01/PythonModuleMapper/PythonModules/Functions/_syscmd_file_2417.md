---
type: function
name: _syscmd_file
module: platform
lineno: 715
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _syscmd_file()

## Overview

Interface to the system's file command.

The function uses the -b option of the file command to have it
omit the filename in its output. Follow the symlinks. It returns
default in case the command should fail.

```python
def _syscmd_file(target, default)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 715
