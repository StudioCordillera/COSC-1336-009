---
type: function
name: _simple_enum
module: enum
lineno: 1737
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _simple_enum()

## Overview

Class decorator that converts a normal class into an :class:`Enum`.  No
safety checks are done, and some advanced behavior (such as
:func:`__init_subclass__`) is not available.  Enum creation can be faster
using :func:`_simple_enum`.

    >>> from enum import Enum, _simple_enum
    >>> @_simple_enum(Enum)
    ... class Color:
    ...     RED = auto()
    ...     GREEN = auto()
    ...     BLUE = auto()
    >>> Color
    <enum 'Color'>

```python
def _simple_enum(etype)
```

**Module:** [[Modules/enum|enum]]
**Type:** Module-level function
**Line:** 1737
