---
type: function
name: supernet
module: ipaddress
lineno: 982
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: supernet()

## Overview

The supernet containing the current network.

Args:
    prefixlen_diff: An integer, the amount the prefix length of
      the network should be decreased by.  For example, given a
      /24 network and a prefixlen_diff of 3, a supernet with a
      /21 netmask is returned.

Returns:
    An IPv4 network object.

Raises:
    ValueError: If self.prefixlen - prefixlen_diff < 0. I.e., you have
      a negative prefix length.
        OR
    If prefixlen_diff and new_prefix are both set or new_prefix is a
      larger number than the current prefix (larger number means a
      smaller network)

```python
def supernet(self, prefixlen_diff, new_prefix)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseNetwork|_BaseNetwork]]
**Type:** Method
**Line:** 982

## Categories

- [[Taxonomy/public_method|public_method]]
