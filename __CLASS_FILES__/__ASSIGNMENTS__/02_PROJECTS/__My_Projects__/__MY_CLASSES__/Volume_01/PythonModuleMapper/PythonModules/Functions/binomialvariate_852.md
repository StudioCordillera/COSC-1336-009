---
type: function
name: binomialvariate
module: random
lineno: 787
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: binomialvariate()

## Overview

Binomial random variable.

Gives the number of successes for *n* independent trials
with the probability of success in each trial being *p*:

    sum(random() < p for i in range(n))

Returns an integer in the range:   0 <= X <= n

The mean (expected value) and variance of the random variable are:

    E[X] = n * p
    Var[x] = n * p * (1 - p)

```python
def binomialvariate(self, n, p)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 787

## Categories

- [[Taxonomy/public_method|public_method]]
