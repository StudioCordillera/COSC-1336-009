---
type: function
name: get_protocol_members
module: typing
lineno: 3775
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_protocol_members()

## Overview

Return the set of members defined in a Protocol.

Example::

    >>> from typing import Protocol, get_protocol_members
    >>> class P(Protocol):
    ...     def a(self) -> str: ...
    ...     b: int
    >>> get_protocol_members(P) == frozenset({'a', 'b'})
    True

Raise a TypeError for arguments that are not Protocols.

```python
def get_protocol_members() -> frozenset[str]
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3775

## Categories

- [[Taxonomy/accessor|accessor]]
