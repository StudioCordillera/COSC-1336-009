---
type: function
name: variance
module: statistics
lineno: 1111
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: variance()

## Overview

Return the sample variance of data.

data should be an iterable of Real-valued numbers, with at least two
values. The optional argument xbar, if given, should be the mean of
the data. If it is missing or None, the mean is automatically calculated.

Use this function when your data is a sample from a population. To
calculate the variance from the entire population, see ``pvariance``.

Examples:

>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> variance(data)
1.3720238095238095

If you have already calculated the mean of your data, you can pass it as
the optional second argument ``xbar`` to avoid recalculating it:

>>> m = mean(data)
>>> variance(data, m)
1.3720238095238095

This function does not check that ``xbar`` is actually the mean of
``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
impossible results.

Decimals and Fractions are supported:

>>> from decimal import Decimal as D
>>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
Decimal('31.01875')

>>> from fractions import Fraction as F
>>> variance([F(1, 6), F(1, 2), F(5, 3)])
Fraction(67, 108)

```python
def variance(data, xbar)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1111
