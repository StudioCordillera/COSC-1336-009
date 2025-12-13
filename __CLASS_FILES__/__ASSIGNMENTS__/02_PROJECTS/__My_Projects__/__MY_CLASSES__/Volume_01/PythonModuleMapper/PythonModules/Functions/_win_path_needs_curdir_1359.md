---
type: function
name: _win_path_needs_curdir
module: shutil
lineno: 1493
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _win_path_needs_curdir()

## Overview

On Windows, we can use NeedCurrentDirectoryForExePath to figure out
if we should add the cwd to PATH when searching for executables if
the mode is executable.

```python
def _win_path_needs_curdir(cmd, mode)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1493
