---
type: function
name: enter_async_context
module: contextlib
lineno: 654
is_async: True
is_method: True
tags:
  - python
  - function
categories:
  - async_function
---

# Function: async enter_async_context()

## Overview

Enters the supplied async context manager.

If successful, also pushes its __aexit__ method as a callback and
returns the result of the __aenter__ method.

```python
def enter_async_context(self, cm)
```

**Module:** [[Modules/contextlib|contextlib]]
**Class:** [[Classes/AsyncExitStack|AsyncExitStack]]
**Type:** Method
**Line:** 654
**Async:** Yes (coroutine)

## Categories

- [[Taxonomy/async_function|async_function]]
