---
type: function
name: _compress_hextets
module: ipaddress
lineno: 1801
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _compress_hextets()

## Overview

Compresses a list of hextets.

Compresses a list of strings, replacing the longest continuous
sequence of "0" in the list with "" and adding empty strings at
the beginning or at the end of the string such that subsequently
calling ":".join(hextets) will produce the compressed version of
the IPv6 address.

Args:
    hextets: A list of strings, the hextets to compress.

Returns:
    A list of strings.

```python
@classmethod
def _compress_hextets(cls, hextets)
```

**Module:** [[Modules/ipaddress|ipaddress]]
**Class:** [[Classes/_BaseV6|_BaseV6]]
**Type:** Method
**Line:** 1801

## Categories

- [[Taxonomy/protected_method|protected_method]]
