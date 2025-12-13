---
type: function
name: overlap
module: statistics
lineno: 1563
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: overlap()

## Overview

Compute the overlapping coefficient (OVL) between two normal distributions.

Measures the agreement between two normal probability distributions.
Returns a value between 0.0 and 1.0 giving the overlapping area in
the two underlying probability density functions.

    >>> N1 = NormalDist(2.4, 1.6)
    >>> N2 = NormalDist(3.2, 2.0)
    >>> N1.overlap(N2)
    0.8035050657330205

```python
def overlap(self, other)
```

**Module:** [[Modules/statistics|statistics]]
**Class:** [[Classes/NormalDist|NormalDist]]
**Type:** Method
**Line:** 1563

## Categories

- [[Taxonomy/public_method|public_method]]
