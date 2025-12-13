---
type: function
name: _split_scope_id
module: ipaddress
lineno: 1905
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _split_scope_id()

## Overview

Helper function to parse IPv6 string address with scope id.

See RFC 4007 for details.

Args:
    ip_str: A string, the IPv6 address.

Returns:
    (addr, scope_id) tuple.

```python
@staticmethod
def _split_scope_id(ip_str)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV6|_BaseV6]]
**Type:** Method
**Line:** 1905

## Categories

- [[Taxonomy/protected_method|protected_method]]
