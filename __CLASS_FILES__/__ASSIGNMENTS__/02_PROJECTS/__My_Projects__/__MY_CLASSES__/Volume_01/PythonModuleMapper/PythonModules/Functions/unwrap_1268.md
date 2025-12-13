---
type: function
name: unwrap
module: inspect
lineno: 764
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: unwrap()

## Overview

Get the object wrapped by *func*.

Follows the chain of :attr:`__wrapped__` attributes returning the last
object in the chain.

*stop* is an optional callback accepting an object in the wrapper chain
as its sole argument that allows the unwrapping to be terminated early if
the callback returns a true value. If the callback never returns a true
value, the last object in the chain is returned as usual. For example,
:func:`signature` uses this to stop unwrapping if any object in the
chain has a ``__signature__`` attribute defined.

:exc:`ValueError` is raised if a cycle is encountered.

 

```python
def unwrap(func)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 764
