---
type: function
name: is_typeddict
module: typing
lineno: 2584
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: is_typeddict()

## Overview

Check if an annotation is a TypedDict class.

For example::

    >>> from typing import TypedDict
    >>> class Film(TypedDict):
    ...     title: str
    ...     year: int
    ...
    >>> is_typeddict(Film)
    True
    >>> is_typeddict(dict)
    False

```python
def is_typeddict(tp)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2584

## Categories

- [[Taxonomy/accessor|accessor]]
