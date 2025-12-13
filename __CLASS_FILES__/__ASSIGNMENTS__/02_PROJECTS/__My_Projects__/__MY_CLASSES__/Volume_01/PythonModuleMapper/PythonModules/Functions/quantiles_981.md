---
type: function
name: quantiles
module: statistics
lineno: 1552
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: quantiles()

## Overview

Divide into *n* continuous intervals with equal probability.

Returns a list of (n - 1) cut points separating the intervals.

Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
Set *n* to 100 for percentiles which gives the 99 cuts points that
separate the normal distribution in to 100 equal sized groups.

```python
def quantiles(self, n)
```

**Module:** [[Modules/statistics|statistics]]
**Class:** [[Classes/NormalDist|NormalDist]]
**Type:** Method
**Line:** 1552
