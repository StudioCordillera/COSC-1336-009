---
type: function
name: get_mixed_type_key
module: ipaddress
lineno: 358
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_mixed_type_key()

## Overview

Return a key suitable for sorting between networks and addresses.

Address and Network objects are not sortable by default; they're
fundamentally different so the expression

    IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

doesn't make any sense.  There are some times however, where you may wish
to have ipaddress sort these for you anyway. If you need to do this, you
can use this function as the key= argument to sorted().

Args:
  obj: either a Network or Address object.
Returns:
  appropriate key.

```python
def get_mixed_type_key(obj)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 358

## Categories

- [[Taxonomy/accessor|accessor]]
