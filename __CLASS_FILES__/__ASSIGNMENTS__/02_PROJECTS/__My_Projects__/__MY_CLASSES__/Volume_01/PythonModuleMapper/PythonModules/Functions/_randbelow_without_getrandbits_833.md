---
type: function
name: _randbelow_without_getrandbits
module: random
lineno: 255
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _randbelow_without_getrandbits()

## Overview

Return a random int in the range [0,n).  Defined for n > 0.

The implementation does not use getrandbits, but only random.

```python
def _randbelow_without_getrandbits(self, n, maxsize)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 255

## Categories

- [[Taxonomy/protected_method|protected_method]]
