---
type: function
name: is_global
module: ipaddress
lineno: 1361
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: is_global()

## Overview

``True`` if the address is defined as globally reachable by
iana-ipv4-special-registry_ (for IPv4) or iana-ipv6-special-registry_
(for IPv6) with the following exception:

For IPv4-mapped IPv6-addresses the ``is_private`` value is determined by the
semantics of the underlying IPv4 addresses and the following condition holds
(see :attr:`IPv6Address.ipv4_mapped`)::

    address.is_global == address.ipv4_mapped.is_global

``is_global`` has value opposite to :attr:`is_private`, except for the ``100.64.0.0/10``
IPv4 range where they are both ``False``.

```python
@property
@functools.lru_cache
def is_global(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/IPv4Address|IPv4Address]]
**Type:** Method
**Line:** 1361
