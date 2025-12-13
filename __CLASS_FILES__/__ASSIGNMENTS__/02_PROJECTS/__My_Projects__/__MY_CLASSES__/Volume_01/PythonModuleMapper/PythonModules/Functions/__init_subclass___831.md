---
type: function
name: __init_subclass__
module: random
lineno: 225
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __init_subclass__()

## Overview

Control how subclasses generate random integers.

The algorithm a subclass can use depends on the random() and/or
getrandbits() implementation available to it and determines
whether it can generate random integers from arbitrarily large
ranges.

```python
def __init_subclass__()
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 225

## Categories

- [[Taxonomy/magic_method|magic_method]]
