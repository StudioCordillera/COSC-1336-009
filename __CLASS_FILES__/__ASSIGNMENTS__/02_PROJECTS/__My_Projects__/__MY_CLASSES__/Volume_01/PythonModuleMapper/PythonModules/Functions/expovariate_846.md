---
type: function
name: expovariate
module: random
lineno: 603
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: expovariate()

## Overview

Exponential distribution.

lambd is 1.0 divided by the desired mean.  It should be
nonzero.  (The parameter would be called "lambda", but that is
a reserved word in Python.)  Returned values range from 0 to
positive infinity if lambd is positive, and from negative
infinity to 0 if lambd is negative.

The mean (expected value) and variance of the random variable are:

    E[X] = 1 / lambd
    Var[X] = 1 / lambd ** 2

```python
def expovariate(self, lambd)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 603

## Categories

- [[Taxonomy/public_method|public_method]]
