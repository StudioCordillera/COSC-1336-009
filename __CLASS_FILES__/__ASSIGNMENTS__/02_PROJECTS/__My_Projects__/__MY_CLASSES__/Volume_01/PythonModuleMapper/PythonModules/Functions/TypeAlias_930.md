---
type: function
name: TypeAlias
module: typing
lineno: 848
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: TypeAlias()

## Overview

Special form for marking type aliases.

Use TypeAlias to indicate that an assignment should
be recognized as a proper type alias definition by type
checkers.

For example::

    Predicate: TypeAlias = Callable[..., bool]

It's invalid when used anywhere except as in the example above.

```python
@_SpecialForm
def TypeAlias(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 848
