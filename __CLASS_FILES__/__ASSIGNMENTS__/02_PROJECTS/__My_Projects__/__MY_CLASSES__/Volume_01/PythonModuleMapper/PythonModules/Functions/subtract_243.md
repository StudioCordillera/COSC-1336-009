---
type: function
name: subtract
module: collections
lineno: 707
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: subtract()

## Overview

Like dict.update() but subtracts counts instead of replacing them.
Counts can be reduced below zero.  Both the inputs and outputs are
allowed to contain zero and negative counts.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.subtract('witch')             # subtract elements from another iterable
>>> c.subtract(Counter('watch'))    # subtract elements from another counter
>>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
0
>>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
-1

```python
def subtract()
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 707

## Categories

- [[Taxonomy/public_method|public_method]]
