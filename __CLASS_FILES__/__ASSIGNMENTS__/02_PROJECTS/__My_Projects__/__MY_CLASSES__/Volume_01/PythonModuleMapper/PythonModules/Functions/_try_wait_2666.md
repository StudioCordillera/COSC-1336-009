---
type: function
name: _try_wait
module: subprocess
lineno: 2021
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _try_wait()

## Overview

All callers to this function MUST hold self._waitpid_lock.

```python
def _try_wait(self, wait_flags)
```

**Module:** [[Modules/subprocess|subprocess]]
**Class:** [[Classes/Popen|Popen]]
**Type:** Method
**Line:** 2021

## Categories

- [[Taxonomy/protected_method|protected_method]]
