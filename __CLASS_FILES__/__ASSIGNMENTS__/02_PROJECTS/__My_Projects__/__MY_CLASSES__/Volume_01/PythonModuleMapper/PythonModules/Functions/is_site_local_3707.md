---
type: function
name: is_site_local
module: ipaddress
lineno: 2097
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
  - accessor
---

# Function: is_site_local()

## Overview

Test if the address is reserved for site-local.

Note that the site-local address space has been deprecated by RFC 3879.
Use is_private to test if this address is in the space of unique local
addresses as defined by RFC 4193.

Returns:
    A boolean, True if the address is reserved per RFC 3513 2.5.6.

```python
@property
def is_site_local(self)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/IPv6Address|IPv6Address]]
**Type:** Method
**Line:** 2097

## Categories

- [[Taxonomy/accessor|accessor]]
- [[Taxonomy/accessor|accessor]]
