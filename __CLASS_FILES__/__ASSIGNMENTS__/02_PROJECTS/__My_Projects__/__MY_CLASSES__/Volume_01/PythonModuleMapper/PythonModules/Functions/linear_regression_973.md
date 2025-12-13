---
type: function
name: linear_regression
module: statistics
lineno: 1352
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: linear_regression()

## Overview

Slope and intercept for simple linear regression.

Return the slope and intercept of simple linear regression
parameters estimated using ordinary least squares. Simple linear
regression describes relationship between an independent variable
*x* and a dependent variable *y* in terms of a linear function:

    y = slope * x + intercept + noise

where *slope* and *intercept* are the regression parameters that are
estimated, and noise represents the variability of the data that was
not explained by the linear regression (it is equal to the
difference between predicted and actual values of the dependent
variable).

The parameters are returned as a named tuple.

>>> x = [1, 2, 3, 4, 5]
>>> noise = NormalDist().samples(5, seed=42)
>>> y = [3 * x[i] + 2 + noise[i] for i in range(5)]
>>> linear_regression(x, y)  #doctest: +ELLIPSIS
LinearRegression(slope=3.17495..., intercept=1.00925...)

If *proportional* is true, the independent variable *x* and the
dependent variable *y* are assumed to be directly proportional.
The data is fit to a line passing through the origin.

Since the *intercept* will always be 0.0, the underlying linear
function simplifies to:

    y = slope * x + noise

>>> y = [3 * x[i] + noise[i] for i in range(5)]
>>> linear_regression(x, y, proportional=True)  #doctest: +ELLIPSIS
LinearRegression(slope=2.90475..., intercept=0.0)

```python
def linear_regression()
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1352
