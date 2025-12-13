---
type: function
name: ip_network
module: ipaddress
lineno: 57
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ip_network()

## Overview

Take an IP string/int and return an object of the correct type.

Args:
    address: A string or integer, the IP network.  Either IPv4 or
      IPv6 networks may be supplied; integers less than 2**32 will
      be considered to be IPv4 by default.

Returns:
    An IPv4Network or IPv6Network object.

Raises:
    ValueError: if the string passed isn't either a v4 or a v6
      address. Or if the network has host bits set.

```python
def ip_network(address, strict)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 57
