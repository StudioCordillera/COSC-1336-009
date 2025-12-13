---
type: function
name: Union
module: typing
lineno: 754
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Union()

## Overview

Union type; Union[X, Y] means either X or Y.

On Python 3.10 and higher, the | operator
can also be used to denote unions;
X | Y means the same thing to the type checker as Union[X, Y].

To define a union, use e.g. Union[int, str]. Details:
- The arguments must be types and there must be at least one.
- None as an argument is a special case and is replaced by
  type(None).
- Unions of unions are flattened, e.g.::

    assert Union[Union[int, str], float] == Union[int, str, float]

- Unions of a single argument vanish, e.g.::

    assert Union[int] == int  # The constructor actually returns int

- Redundant arguments are skipped, e.g.::

    assert Union[int, str, int] == Union[int, str]

- When comparing unions, the argument order is ignored, e.g.::

    assert Union[int, str] == Union[str, int]

- You cannot subclass or instantiate a union.
- You can use Optional[X] as a shorthand for Union[X, None].

```python
@_SpecialForm
def Union(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 754
