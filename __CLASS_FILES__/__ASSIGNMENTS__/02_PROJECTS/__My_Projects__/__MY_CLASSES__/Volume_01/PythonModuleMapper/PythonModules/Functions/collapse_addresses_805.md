---
type: function
name: collapse_addresses
module: ipaddress
lineno: 304
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: collapse_addresses()

## Overview

Collapse a list of IP objects.

Example:
    collapse_addresses([IPv4Network('192.0.2.0/25'),
                        IPv4Network('192.0.2.128/25')]) ->
                       [IPv4Network('192.0.2.0/24')]

Args:
    addresses: An iterable of IPv4Network or IPv6Network objects.

Returns:
    An iterator of the collapsed IPv(4|6)Network objects.

Raises:
    TypeError: If passed a list of mixed version objects.

```python
def collapse_addresses(addresses)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 304
