---
type: function
name: triangular
module: random
lineno: 509
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: triangular()

## Overview

Triangular distribution.

Continuous distribution bounded by given lower and upper limits,
and having a given mode value in-between.

http://en.wikipedia.org/wiki/Triangular_distribution

The mean (expected value) and variance of the random variable are:

    E[X] = (low + high + mode) / 3
    Var[X] = (low**2 + high**2 + mode**2 - low*high - low*mode - high*mode) / 18

```python
def triangular(self, low, high, mode)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 509

## Categories

- [[Taxonomy/public_method|public_method]]
