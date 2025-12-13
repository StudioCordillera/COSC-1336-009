---
type: function
name: _prefix_from_ip_int
module: ipaddress
lineno: 445
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _prefix_from_ip_int()

## Overview

Return prefix length from the bitwise netmask.

Args:
    ip_int: An integer, the netmask in expanded bitwise format

Returns:
    An integer, the prefix length.

Raises:
    ValueError: If the input intermingles zeroes & ones

```python
@classmethod
def _prefix_from_ip_int(cls, ip_int)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_IPAddressBase|_IPAddressBase]]
**Type:** Method
**Line:** 445

## Categories

- [[Taxonomy/protected_method|protected_method]]
