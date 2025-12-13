---
type: function
name: _prefix_from_prefix_string
module: ipaddress
lineno: 475
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _prefix_from_prefix_string()

## Overview

Return prefix length from a numeric string

Args:
    prefixlen_str: The string to be converted

Returns:
    An integer, the prefix length.

Raises:
    NetmaskValueError: If the input is not a valid netmask

```python
@classmethod
def _prefix_from_prefix_string(cls, prefixlen_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_IPAddressBase|_IPAddressBase]]
**Type:** Method
**Line:** 475

## Categories

- [[Taxonomy/protected_method|protected_method]]
