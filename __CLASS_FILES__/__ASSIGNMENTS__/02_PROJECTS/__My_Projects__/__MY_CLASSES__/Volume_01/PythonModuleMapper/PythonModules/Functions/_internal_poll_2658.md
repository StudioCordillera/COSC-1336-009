---
type: function
name: _internal_poll
module: subprocess
lineno: 1987
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _internal_poll()

## Overview

Check if child process has terminated.  Returns returncode
attribute.

This method is called by __del__, so it cannot reference anything
outside of the local scope (nor can any methods it calls).

```python
def _internal_poll(self, _deadstate, _del_safe)
```

**Module:** [[Modules/subprocess|subprocess]]
**Class:** [[Classes/Popen|Popen]]
**Type:** Method
**Line:** 1987

## Categories

- [[Taxonomy/protected_method|protected_method]]
