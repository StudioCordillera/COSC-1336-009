---
type: function
name: _ipv4_mapped_ipv6_to_str
module: ipaddress
lineno: 1998
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _ipv4_mapped_ipv6_to_str()

## Overview

Return convenient text representation of IPv4-mapped IPv6 address

See RFC 4291 2.5.5.2, 2.2 p.3 for details.

Returns:
    A string, 'x:x:x:x:x:x:d.d.d.d', where the 'x's are the hexadecimal values of
    the six high-order 16-bit pieces of the address, and the 'd's are
    the decimal values of the four low-order 8-bit pieces of the
    address (standard IPv4 representation) as defined in RFC 4291 2.2 p.3.

```python
def _ipv4_mapped_ipv6_to_str(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/IPv6Address|IPv6Address]]
**Type:** Method
**Line:** 1998

## Categories

- [[Taxonomy/protected_method|protected_method]]
