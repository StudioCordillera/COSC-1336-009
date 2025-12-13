---
type: function
name: push_async_exit
module: contextlib
lineno: 672
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: push_async_exit()

## Overview

Registers a coroutine function with the standard __aexit__ method
signature.

Can suppress exceptions the same way __aexit__ method can.
Also accepts any object with an __aexit__ method (registering a call
to the method instead of the object itself).

```python
def push_async_exit(self, exit)
```

**Module:** [[Modules/contextlib|contextlib]]
**Class:** [[Classes/AsyncExitStack|AsyncExitStack]]
**Type:** Method
**Line:** 672

## Categories

- [[Taxonomy/public_method|public_method]]
