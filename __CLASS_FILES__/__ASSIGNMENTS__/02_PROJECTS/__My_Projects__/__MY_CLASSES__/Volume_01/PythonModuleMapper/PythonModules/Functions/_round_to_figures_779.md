---
type: function
name: _round_to_figures
module: fractions
lineno: 103
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _round_to_figures()

## Overview

Round a rational number to a given number of significant figures.

Rounds the rational number n/d to the given number of significant figures
using the round-ties-to-even rule, and returns a triple
(sign: bool, significand: int, exponent: int) representing the rounded
value (-1)**sign * significand * 10**exponent.

In the special case where n = 0, returns a significand of zero and
an exponent of 1 - figures, for compatibility with formatting.
Otherwise, the returned significand satisfies
10**(figures - 1) <= significand < 10**figures.

d must be positive, but n and d need not be relatively prime.
figures must be positive.

```python
def _round_to_figures(n, d, figures)
```

**Module:** [[Modules/fractions|fractions]]
**Type:** Module-level function
**Line:** 103
