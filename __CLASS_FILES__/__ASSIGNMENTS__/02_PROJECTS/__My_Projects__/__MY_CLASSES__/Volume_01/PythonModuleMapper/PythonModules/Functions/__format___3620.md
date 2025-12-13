---
type: function
name: __format__
module: ipaddress
lineno: 621
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __format__()

## Overview

Returns an IP address as a formatted string.

Supported presentation types are:
's': returns the IP address as a string (default)
'b': converts to binary and returns a zero-padded string
'X' or 'x': converts to upper- or lower-case hex and returns a zero-padded string
'n': the same as 'b' for IPv4 and 'x' for IPv6

For binary and hex presentation types, the alternate form specifier
'#' and the grouping option '_' are supported.

```python
def __format__(self, fmt)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseAddress|_BaseAddress]]
**Type:** Method
**Line:** 621

## Categories

- [[Taxonomy/magic_method|magic_method]]
