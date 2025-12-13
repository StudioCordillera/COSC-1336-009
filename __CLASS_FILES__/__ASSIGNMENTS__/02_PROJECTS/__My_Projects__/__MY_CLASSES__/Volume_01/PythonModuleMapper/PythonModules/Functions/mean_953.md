---
type: function
name: mean
module: statistics
lineno: 472
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: mean()

## Overview

Return the sample arithmetic mean of data.

>>> mean([1, 2, 3, 4, 4])
2.8

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
Fraction(13, 21)

>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
Decimal('0.5625')

If ``data`` is empty, StatisticsError will be raised.

```python
def mean(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 472
