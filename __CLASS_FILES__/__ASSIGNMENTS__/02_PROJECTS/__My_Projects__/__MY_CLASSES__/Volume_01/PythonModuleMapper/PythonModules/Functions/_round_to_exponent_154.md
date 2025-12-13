---
type: function
name: _round_to_exponent
module: fractions
lineno: 74
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _round_to_exponent()

## Overview

Round a rational number to the nearest multiple of a given power of 10.

Rounds the rational number n/d to the nearest integer multiple of
10**exponent, rounding to the nearest even integer multiple in the case of
a tie. Returns a pair (sign: bool, significand: int) representing the
rounded value (-1)**sign * significand * 10**exponent.

If no_neg_zero is true, then the returned sign will always be False when
the significand is zero. Otherwise, the sign reflects the sign of the
input.

d must be positive, but n and d need not be relatively prime.

```python
def _round_to_exponent(n, d, exponent, no_neg_zero)
```

**Module:** [[Modules/fractions|fractions]]
**Type:** Module-level function
**Line:** 74
