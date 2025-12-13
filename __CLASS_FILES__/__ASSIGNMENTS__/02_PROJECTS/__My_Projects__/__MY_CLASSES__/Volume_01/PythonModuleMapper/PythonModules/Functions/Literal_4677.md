---
type: function
name: Literal
module: typing
lineno: 814
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Literal()

## Overview

Special typing form to define literal types (a.k.a. value types).

This form can be used to indicate to type checkers that the corresponding
variable or function parameter has a value equivalent to the provided
literal (or one of several literals)::

    def validate_simple(data: Any) -> Literal[True]:  # always returns True
        ...

    MODE = Literal['r', 'rb', 'w', 'wb']
    def open_helper(file: str, mode: MODE) -> str:
        ...

    open_helper('/some/path', 'r')  # Passes type check
    open_helper('/other/path', 'typo')  # Error in type checker

Literal[...] cannot be subclassed. At runtime, an arbitrary value
is allowed as type argument to Literal[...], but type checkers may
impose restrictions.

```python
@_TypedCacheSpecialForm
@_tp_cache
def Literal(self)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 814
