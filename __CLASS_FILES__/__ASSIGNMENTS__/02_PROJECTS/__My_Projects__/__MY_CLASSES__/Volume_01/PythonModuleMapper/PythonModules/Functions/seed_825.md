---
type: function
name: seed
module: random
lineno: 128
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: seed()

## Overview

Initialize internal state from a seed.

The only supported seed types are None, int, float,
str, bytes, and bytearray.

None or no argument seeds from current time or from an operating
system specific randomness source if available.

If *a* is an int, all bits are used.

For version 2 (the default), all of the bits are used if *a* is a str,
bytes, or bytearray.  For version 1 (provided for reproducing random
sequences from older versions of Python), the algorithm for str and
bytes generates a narrower range of seeds.

```python
def seed(self, a, version)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 128

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
