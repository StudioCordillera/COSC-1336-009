---
type: function
name: _prefix_from_ip_string
module: ipaddress
lineno: 500
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _prefix_from_ip_string()

## Overview

Turn a netmask/hostmask string into a prefix length

Args:
    ip_str: The netmask/hostmask to be converted

Returns:
    An integer, the prefix length.

Raises:
    NetmaskValueError: If the input is not a valid netmask/hostmask

```python
@classmethod
def _prefix_from_ip_string(cls, ip_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_IPAddressBase|_IPAddressBase]]
**Type:** Method
**Line:** 500

## Categories

- [[Taxonomy/protected_method|protected_method]]
