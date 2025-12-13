---
type: function
name: _should_unflatten_callable_args
module: typing
lineno: 211
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _should_unflatten_callable_args()

## Overview

Internal helper for munging collections.abc.Callable's __args__.

The canonical representation for a Callable's __args__ flattens the
argument types, see https://github.com/python/cpython/issues/86361.

For example::

    >>> import collections.abc
    >>> P = ParamSpec('P')
    >>> collections.abc.Callable[[int, int], str].__args__ == (int, int, str)
    True
    >>> collections.abc.Callable[P, str].__args__ == (P, str)
    True

As a result, if we need to reconstruct the Callable from its __args__,
we need to unflatten it.

```python
def _should_unflatten_callable_args(typ, args)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 211
