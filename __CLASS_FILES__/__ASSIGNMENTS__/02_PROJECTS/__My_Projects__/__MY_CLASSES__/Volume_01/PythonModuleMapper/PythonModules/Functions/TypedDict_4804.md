---
type: function
name: TypedDict
module: typing
lineno: 3240
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: TypedDict()

## Overview

A simple typed namespace. At runtime it is equivalent to a plain dict.

TypedDict creates a dictionary type such that a type checker will expect all
instances to have a certain set of keys, where each key is
associated with a value of a consistent type. This expectation
is not checked at runtime.

Usage::

    >>> class Point2D(TypedDict):
    ...     x: int
    ...     y: int
    ...     label: str
    ...
    >>> a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
    >>> b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check
    >>> Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
    True

The type info can be accessed via the Point2D.__annotations__ dict, and
the Point2D.__required_keys__ and Point2D.__optional_keys__ frozensets.
TypedDict supports an additional equivalent form::

    Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

By default, all keys must be present in a TypedDict. It is possible
to override this by specifying totality::

    class Point2D(TypedDict, total=False):
        x: int
        y: int

This means that a Point2D TypedDict can have any of the keys omitted. A type
checker is only expected to support a literal False or True as the value of
the total argument. True is the default, and makes all items defined in the
class body be required.

The Required and NotRequired special forms can also be used to mark
individual keys as being required or not required::

    class Point2D(TypedDict):
        x: int               # the "x" key must always be present (Required is the default)
        y: NotRequired[int]  # the "y" key can be omitted

See PEP 655 for more details on Required and NotRequired.

The ReadOnly special form can be used
to mark individual keys as immutable for type checkers::

    class DatabaseUser(TypedDict):
        id: ReadOnly[int]  # the "id" key must not be modified
        username: str      # the "username" key can be changed

```python
def TypedDict()
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3240
