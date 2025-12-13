---
type: function
name: Concatenate
module: typing
lineno: 865
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Concatenate()

## Overview

Special form for annotating higher-order functions.

``Concatenate`` can be used in conjunction with ``ParamSpec`` and
``Callable`` to represent a higher-order function which adds, removes or
transforms the parameters of a callable.

For example::

    Callable[Concatenate[int, P], int]

See PEP 612 for detailed information.

```python
@_SpecialForm
def Concatenate(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 865
