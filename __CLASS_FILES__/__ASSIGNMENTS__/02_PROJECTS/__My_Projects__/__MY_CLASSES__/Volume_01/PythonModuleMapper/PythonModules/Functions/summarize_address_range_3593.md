---
type: function
name: summarize_address_range
module: ipaddress
lineno: 200
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: summarize_address_range()

## Overview

Summarize a network range given the first and last IP addresses.

Example:
    >>> list(summarize_address_range(IPv4Address('192.0.2.0'),
    ...                              IPv4Address('192.0.2.130')))
    ...                                #doctest: +NORMALIZE_WHITESPACE
    [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'),
     IPv4Network('192.0.2.130/32')]

Args:
    first: the first IPv4Address or IPv6Address in the range.
    last: the last IPv4Address or IPv6Address in the range.

Returns:
    An iterator of the summarized IPv(4|6) network objects.

Raise:
    TypeError:
        If the first and last objects are not IP addresses.
        If the first and last objects are not the same version.
    ValueError:
        If the last object is not greater than the first.
        If the version of the first address is not 4 or 6.

```python
def summarize_address_range(first, last)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Type:** Module-level function
**Line:** 200
