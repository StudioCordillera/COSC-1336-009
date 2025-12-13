---
type: function
name: ip_address
module: ipaddress
lineno: 28
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ip_address()

## Overview

Take an IP string/int and return an object of the correct type.

Args:
    address: A string or integer, the IP address.  Either IPv4 or
      IPv6 addresses may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Address or IPv6Address object.

Raises:
    ValueError: if the *address* passed isn't either a v4 or a v6
      address

```python
def ip_address(address)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 28
