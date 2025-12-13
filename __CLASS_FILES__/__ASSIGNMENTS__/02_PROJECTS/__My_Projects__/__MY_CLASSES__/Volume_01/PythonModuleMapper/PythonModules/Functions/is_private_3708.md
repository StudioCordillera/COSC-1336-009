---
type: function
name: is_private
module: ipaddress
lineno: 2112
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: is_private()

## Overview

``True`` if the address is defined as not globally reachable by
iana-ipv4-special-registry_ (for IPv4) or iana-ipv6-special-registry_
(for IPv6) with the following exceptions:

* ``is_private`` is ``False`` for ``100.64.0.0/10``
* For IPv4-mapped IPv6-addresses the ``is_private`` value is determined by the
    semantics of the underlying IPv4 addresses and the following condition holds
    (see :attr:`IPv6Address.ipv4_mapped`)::

        address.is_private == address.ipv4_mapped.is_private

``is_private`` has value opposite to :attr:`is_global`, except for the ``100.64.0.0/10``
IPv4 range where they are both ``False``.

```python
@property
@functools.lru_cache
def is_private(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/IPv6Address|IPv6Address]]
**Type:** Method
**Line:** 2112
