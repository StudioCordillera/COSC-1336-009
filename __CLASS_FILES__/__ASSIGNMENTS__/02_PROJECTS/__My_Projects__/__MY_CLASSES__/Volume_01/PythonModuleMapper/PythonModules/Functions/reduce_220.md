---
type: function
name: reduce
module: functools
lineno: 238
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: reduce()

## Overview

reduce(function, iterable[, initial], /) -> value

Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

This effectively reduces the iterable to a single value.  If initial is present,
it is placed before the items of the iterable in the calculation, and serves as
a default when the iterable is empty.

For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
calculates ((((1 + 2) + 3) + 4) + 5).

```python
def reduce(function, sequence, initial)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 238
