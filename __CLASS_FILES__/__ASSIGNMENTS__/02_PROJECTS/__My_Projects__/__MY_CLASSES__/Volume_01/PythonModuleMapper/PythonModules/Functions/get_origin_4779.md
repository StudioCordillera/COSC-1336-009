---
type: function
name: get_origin
module: typing
lineno: 2528
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_origin()

## Overview

Get the unsubscripted version of a type.

This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar,
Annotated, and others. Return None for unsupported types.

Examples::

    >>> P = ParamSpec('P')
    >>> assert get_origin(Literal[42]) is Literal
    >>> assert get_origin(int) is None
    >>> assert get_origin(ClassVar[int]) is ClassVar
    >>> assert get_origin(Generic) is Generic
    >>> assert get_origin(Generic[T]) is Generic
    >>> assert get_origin(Union[T, int]) is Union
    >>> assert get_origin(List[Tuple[T, T]][int]) is list
    >>> assert get_origin(P.args) is P

```python
def get_origin(tp)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2528

## Categories

- [[Taxonomy/accessor|accessor]]
