---
type: function
name: ip_interface
module: ipaddress
lineno: 86
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ip_interface()

## Overview

Take an IP string/int and return an object of the correct type.

Args:
    address: A string or integer, the IP address.  Either IPv4 or
      IPv6 addresses may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Interface or IPv6Interface object.

Raises:
    ValueError: if the string passed isn't either a v4 or a v6
      address.

Notes:
    The IPv?Interface classes describe an Address on a particular
    Network, so they're basically a combination of both the Address
    and Network classes.

```python
def ip_interface(address)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 86
