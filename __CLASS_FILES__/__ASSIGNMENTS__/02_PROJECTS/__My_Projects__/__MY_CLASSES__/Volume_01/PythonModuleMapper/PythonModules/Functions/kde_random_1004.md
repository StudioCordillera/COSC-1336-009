---
type: function
name: kde_random
module: statistics
lineno: 1766
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: kde_random()

## Overview

Return a function that makes a random selection from the estimated
probability density function created by kde(data, h, kernel).

Providing a *seed* allows reproducible selections within a single
thread.  The seed may be an integer, float, str, or bytes.

A StatisticsError will be raised if the *data* sequence is empty.

Example:

>>> data = [-2.1, -1.3, -0.4, 1.9, 5.1, 6.2]
>>> rand = kde_random(data, h=1.5, seed=8675309)
>>> new_selections = [rand() for i in range(10)]
>>> [round(x, 1) for x in new_selections]
[0.7, 6.2, 1.2, 6.9, 7.0, 1.8, 2.5, -0.5, -1.8, 5.6]

```python
def kde_random(data, h, kernel)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1766
