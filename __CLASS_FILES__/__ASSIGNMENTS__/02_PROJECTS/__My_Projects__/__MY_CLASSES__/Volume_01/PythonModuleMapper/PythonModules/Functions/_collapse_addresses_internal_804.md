---
type: function
name: _collapse_addresses_internal
module: ipaddress
lineno: 255
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _collapse_addresses_internal()

## Overview

Loops through the addresses, collapsing concurrent netblocks.

Example:

    ip1 = IPv4Network('192.0.2.0/26')
    ip2 = IPv4Network('192.0.2.64/26')
    ip3 = IPv4Network('192.0.2.128/26')
    ip4 = IPv4Network('192.0.2.192/26')

    _collapse_addresses_internal([ip1, ip2, ip3, ip4]) ->
      [IPv4Network('192.0.2.0/24')]

    This shouldn't be called directly; it is called via
      collapse_addresses([]).

Args:
    addresses: A list of IPv4Network's or IPv6Network's

Returns:
    A list of IPv4Network's or IPv6Network's depending on what we were
    passed.

```python
def _collapse_addresses_internal(addresses)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 255
