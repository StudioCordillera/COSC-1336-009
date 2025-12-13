---
type: function
name: pvariance
module: statistics
lineno: 1155
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: pvariance()

## Overview

Return the population variance of ``data``.

data should be a sequence or iterable of Real-valued numbers, with at least one
value. The optional argument mu, if given, should be the mean of
the data. If it is missing or None, the mean is automatically calculated.

Use this function to calculate the variance from the entire population.
To estimate the variance from a sample, the ``variance`` function is
usually a better choice.

Examples:

>>> data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
>>> pvariance(data)
1.25

If you have already calculated the mean of the data, you can pass it as
the optional second argument to avoid recalculating it:

>>> mu = mean(data)
>>> pvariance(data, mu)
1.25

Decimals and Fractions are supported:

>>> from decimal import Decimal as D
>>> pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('24.815')

>>> from fractions import Fraction as F
>>> pvariance([F(1, 4), F(5, 4), F(1, 2)])
Fraction(13, 72)

```python
def pvariance(data, mu)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1155
