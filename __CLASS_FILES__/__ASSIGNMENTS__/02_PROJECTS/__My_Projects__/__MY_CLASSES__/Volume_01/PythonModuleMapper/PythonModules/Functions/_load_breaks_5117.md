---
type: function
name: _load_breaks
module: bdb
lineno: 458
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _load_breaks()

## Overview

Apply all breakpoints (set in other instances) to this one.

Populates this instance's breaks list from the Breakpoint class's
list, which can have breakpoints set by another Bdb instance. This
is necessary for interactive sessions to keep the breakpoints
active across multiple calls to run().

```python
def _load_breaks(self)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 458

## Categories

- [[Taxonomy/protected_method|protected_method]]
