---
type: function
name: _hold_exceptions
module: pdb
lineno: 584
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _hold_exceptions()

## Overview

Context manager to ensure proper cleaning of exceptions references

When given a chained exception instead of a traceback,
pdb may hold references to many objects which may leak memory.

We use this context manager to make sure everything is properly cleaned

```python
@contextmanager
def _hold_exceptions(self, exceptions)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 584

## Categories

- [[Taxonomy/protected_method|protected_method]]
