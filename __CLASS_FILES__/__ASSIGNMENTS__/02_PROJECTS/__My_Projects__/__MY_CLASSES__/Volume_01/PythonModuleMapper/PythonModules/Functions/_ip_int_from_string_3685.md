---
type: function
name: _ip_int_from_string
module: ipaddress
lineno: 1662
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: _ip_int_from_string()

## Overview

Turn an IPv6 ip_str into an integer.

Args:
    ip_str: A string, the IPv6 ip_str.

Returns:
    An int, the IPv6 address

Raises:
    AddressValueError: if ip_str isn't a valid IPv6 Address.

```python
@classmethod
def _ip_int_from_string(cls, ip_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV6|_BaseV6]]
**Type:** Method
**Line:** 1662
