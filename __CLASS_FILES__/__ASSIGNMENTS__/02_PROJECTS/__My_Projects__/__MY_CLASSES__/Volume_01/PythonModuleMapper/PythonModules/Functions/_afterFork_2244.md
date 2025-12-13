---
type: function
name: _afterFork
module: logging
lineno: 245
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _afterFork()

## Overview

After a new child process has been forked, release the module-level lock.

This should be used in conjunction with _prepareFork().

```python
def _afterFork()
```

**Module:** [[Modules/logging|logging]]
**Type:** Module-level function
**Line:** 245
