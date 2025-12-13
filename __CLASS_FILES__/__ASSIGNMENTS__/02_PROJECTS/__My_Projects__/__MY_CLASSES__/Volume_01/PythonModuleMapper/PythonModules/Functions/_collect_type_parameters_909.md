---
type: function
name: _collect_type_parameters
module: typing
lineno: 260
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _collect_type_parameters()

## Overview

Collect all type parameters in args
in order of first appearance (lexicographic order).

For example::

    >>> P = ParamSpec('P')
    >>> T = TypeVar('T')
    >>> _collect_type_parameters((T, Callable[P, T]))
    (~T, ~P)

```python
def _collect_type_parameters(args)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 260
