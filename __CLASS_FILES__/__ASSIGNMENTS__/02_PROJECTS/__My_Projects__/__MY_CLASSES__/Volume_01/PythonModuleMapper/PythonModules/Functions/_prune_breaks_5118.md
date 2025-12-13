---
type: function
name: _prune_breaks
module: bdb
lineno: 469
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _prune_breaks()

## Overview

Prune breakpoints for filename:lineno.

A list of breakpoints is maintained in the Bdb instance and in
the Breakpoint class.  If a breakpoint in the Bdb instance no
longer exists in the Breakpoint class, then it's removed from the
Bdb instance.

```python
def _prune_breaks(self, filename, lineno)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 469

## Categories

- [[Taxonomy/protected_method|protected_method]]
