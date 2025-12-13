---
type: function
name: _handle_exitstatus
module: subprocess
lineno: 1978
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _handle_exitstatus()

## Overview

All callers to this function MUST hold self._waitpid_lock.

```python
def _handle_exitstatus(self, sts, _del_safe)
```

**Module:** [[Modules/subprocess|subprocess]]
**Class:** [[Classes/Popen|Popen]]
**Type:** Method
**Line:** 1978

## Categories

- [[Taxonomy/protected_method|protected_method]]
