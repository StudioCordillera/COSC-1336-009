---
type: function
name: gammavariate
module: random
lineno: 665
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: gammavariate()

## Overview

Gamma distribution.  Not the gamma function!

Conditions on the parameters are alpha > 0 and beta > 0.

The probability distribution function is:

            x ** (alpha - 1) * math.exp(-x / beta)
  pdf(x) =  --------------------------------------
              math.gamma(alpha) * beta ** alpha

The mean (expected value) and variance of the random variable are:

    E[X] = alpha * beta
    Var[X] = alpha * beta ** 2

```python
def gammavariate(self, alpha, beta)
```

**Module:** [[Modules/random|random]]
**Class:** [[Classes/Random|Random]]
**Type:** Method
**Line:** 665

## Categories

- [[Taxonomy/public_method|public_method]]
