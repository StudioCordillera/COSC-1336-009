---
type: function
name: get_args
module: typing
lineno: 2558
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_args()

## Overview

Get type arguments with all substitutions performed.

For unions, basic simplifications used by Union constructor are performed.

Examples::

    >>> T = TypeVar('T')
    >>> assert get_args(Dict[str, int]) == (str, int)
    >>> assert get_args(int) == ()
    >>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
    >>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
    >>> assert get_args(Callable[[], T][int]) == ([], int)

```python
def get_args(tp)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2558

## Categories

- [[Taxonomy/accessor|accessor]]
