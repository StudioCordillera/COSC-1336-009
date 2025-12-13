---
type: function
name: which
module: shutil
lineno: 1503
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: which()

## Overview

Given a command, mode, and a PATH string, return the path which
conforms to the given mode on the PATH, or None if there is no such
file.

`mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
of os.environ.get("PATH"), or can be overridden with a custom search
path.

```python
def which(cmd, mode, path)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1503
