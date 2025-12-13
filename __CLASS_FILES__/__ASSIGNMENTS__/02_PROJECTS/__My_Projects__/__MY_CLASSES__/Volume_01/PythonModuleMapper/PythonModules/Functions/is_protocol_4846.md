---
type: function
name: is_protocol
module: typing
lineno: 3754
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: is_protocol()

## Overview

Return True if the given type is a Protocol.

Example::

    >>> from typing import Protocol, is_protocol
    >>> class P(Protocol):
    ...     def a(self) -> str: ...
    ...     b: int
    >>> is_protocol(P)
    True
    >>> is_protocol(int)
    False

```python
def is_protocol() -> bool
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3754

## Categories

- [[Taxonomy/accessor|accessor]]
