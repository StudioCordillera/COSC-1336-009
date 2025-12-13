---
type: function
name: fmean
module: statistics
lineno: 494
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: fmean()

## Overview

Convert data to floats and compute the arithmetic mean.

This runs faster than the mean() function and it always returns a float.
If the input dataset is empty, it raises a StatisticsError.

>>> fmean([3.5, 4.0, 5.25])
4.25

```python
def fmean(data, weights)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 494
