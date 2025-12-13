---
type: function
name: _parse_hextet
module: ipaddress
lineno: 1775
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _parse_hextet()

## Overview

Convert an IPv6 hextet string into an integer.

Args:
    hextet_str: A string, the number to parse.

Returns:
    The hextet as an integer.

Raises:
    ValueError: if the input isn't strictly a hex number from
      [0..FFFF].

```python
@classmethod
def _parse_hextet(cls, hextet_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV6|_BaseV6]]
**Type:** Method
**Line:** 1775

## Categories

- [[Taxonomy/protected_method|protected_method]]
