---
type: function
name: _make_netmask
module: ipaddress
lineno: 1162
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
  - protected_method
---

# Function: _make_netmask()

## Overview

Make a (netmask, prefix_len) tuple from the given argument.

Argument can be:
- an integer (the prefix length)
- a string representing the prefix length (e.g. "24")
- a string representing the prefix netmask (e.g. "255.255.255.0")

```python
@classmethod
def _make_netmask(cls, arg)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV4|_BaseV4]]
**Type:** Method
**Line:** 1162

## Categories

- [[Taxonomy/protected_method|protected_method]]
- [[Taxonomy/protected_method|protected_method]]
