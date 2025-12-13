---
type: function
name: is_global
module: ipaddress
lineno: 1566
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: is_global()

## Overview

Test if this address is allocated for public networks.

Returns:
    A boolean, True if the address is not reserved per
    iana-ipv4-special-registry.

```python
@property
@functools.lru_cache
def is_global(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/IPv4Network|IPv4Network]]
**Type:** Method
**Line:** 1566
