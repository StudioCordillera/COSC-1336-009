---
type: function
name: _use_posix_spawn
module: subprocess
lineno: 701
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _use_posix_spawn()

## Overview

Check if posix_spawn() can be used for subprocess.

subprocess requires a posix_spawn() implementation that properly reports
errors to the parent process, & sets errno on the following failures:

* Process attribute actions failed.
* File actions failed.
* exec() failed.

Prefer an implementation which can use vfork() in some cases for best
performance.

```python
def _use_posix_spawn()
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 701
