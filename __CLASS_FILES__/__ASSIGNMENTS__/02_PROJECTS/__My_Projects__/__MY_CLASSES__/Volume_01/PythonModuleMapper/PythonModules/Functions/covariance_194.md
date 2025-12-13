---
type: function
name: covariance
module: statistics
lineno: 1273
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: covariance()

## Overview

Covariance

Return the sample covariance of two inputs *x* and *y*. Covariance
is a measure of the joint variability of two inputs.

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> covariance(x, y)
0.75
>>> z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> covariance(x, z)
-7.5
>>> covariance(z, x)
-7.5

```python
def covariance()
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1273
