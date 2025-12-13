---
type: function
name: _string_from_ip_int
module: ipaddress
lineno: 1849
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: _string_from_ip_int()

## Overview

Turns a 128-bit integer into hexadecimal notation.

Args:
    ip_int: An integer, the IP address.

Returns:
    A string, the hexadecimal representation of the address.

Raises:
    ValueError: The address is bigger than 128 bits of all ones.

```python
@classmethod
def _string_from_ip_int(cls, ip_int)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV6|_BaseV6]]
**Type:** Method
**Line:** 1849
