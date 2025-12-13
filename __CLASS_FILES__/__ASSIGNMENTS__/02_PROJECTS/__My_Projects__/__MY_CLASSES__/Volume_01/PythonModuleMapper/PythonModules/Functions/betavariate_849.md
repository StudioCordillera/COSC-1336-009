---
type: function
name: betavariate
module: random
lineno: 734
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: betavariate()

## Overview

Beta distribution.

Conditions on the parameters are alpha > 0 and beta > 0.
Returned values range between 0 and 1.

The mean (expected value) and variance of the random variable are:

    E[X] = alpha / (alpha + beta)
    Var[X] = alpha * beta / ((alpha + beta)**2 * (alpha + beta + 1))

```python
def betavariate(self, alpha, beta)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 734

## Categories

- [[Taxonomy/public_method|public_method]]
