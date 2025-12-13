---
type: function
name: _parse_octet
module: ipaddress
lineno: 1214
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _parse_octet()

## Overview

Convert a decimal octet into an integer.

Args:
    octet_str: A string, the number to parse.

Returns:
    The octet as an integer.

Raises:
    ValueError: if the octet isn't strictly a decimal from [0..255].

```python
@classmethod
def _parse_octet(cls, octet_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV4|_BaseV4]]
**Type:** Method
**Line:** 1214

## Categories

- [[Taxonomy/protected_method|protected_method]]
