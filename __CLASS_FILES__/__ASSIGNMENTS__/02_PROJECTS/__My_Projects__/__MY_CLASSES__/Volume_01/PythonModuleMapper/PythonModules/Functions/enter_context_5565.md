---
type: function
name: enter_context
module: contextlib
lineno: 515
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: enter_context()

## Overview

Enters the supplied context manager.

If successful, also pushes its __exit__ method as a callback and
returns the result of the __enter__ method.

```python
def enter_context(self, cm)
```

**Module:** [[Modules/contextlib|contextlib]]
**Class:** [[Classes/_BaseExitStack|_BaseExitStack]]
**Type:** Method
**Line:** 515

## Categories

- [[Taxonomy/public_method|public_method]]
