---
type: function
name: _test_simple_enum
module: enum
lineno: 2029
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _test_simple_enum()

## Overview

A function that can be used to test an enum created with :func:`_simple_enum`
against the version created by subclassing :class:`Enum`::

    >>> from enum import Enum, _simple_enum, _test_simple_enum
    >>> @_simple_enum(Enum)
    ... class Color:
    ...     RED = auto()
    ...     GREEN = auto()
    ...     BLUE = auto()
    >>> class CheckedColor(Enum):
    ...     RED = auto()
    ...     GREEN = auto()
    ...     BLUE = auto()
    >>> _test_simple_enum(CheckedColor, Color)

If differences are found, a :exc:`TypeError` is raised.

```python
def _test_simple_enum(checked_enum, simple_enum)
```

**Module:** [[Modules/enum|enum]]
**Type:** Module-level function
**Line:** 2029
