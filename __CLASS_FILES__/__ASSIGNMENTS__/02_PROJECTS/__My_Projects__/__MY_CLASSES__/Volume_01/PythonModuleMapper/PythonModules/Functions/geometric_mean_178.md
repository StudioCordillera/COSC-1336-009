---
type: function
name: geometric_mean
module: statistics
lineno: 530
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: geometric_mean()

## Overview

Convert data to floats and compute the geometric mean.

Raises a StatisticsError if the input dataset is empty
or if it contains a negative value.

Returns zero if the product of inputs is zero.

No special efforts are made to achieve exact results.
(However, this may change in the future.)

>>> round(geometric_mean([54, 24, 36]), 9)
36.0

```python
def geometric_mean(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 530
