---
type: function
name: correlation
module: statistics
lineno: 1301
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: correlation()

## Overview

Pearson's correlation coefficient

Return the Pearson's correlation coefficient for two inputs. Pearson's
correlation coefficient *r* takes values between -1 and +1. It measures
the strength and direction of a linear relationship.

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> correlation(x, x)
1.0
>>> correlation(x, y)
-1.0

If *method* is "ranked", computes Spearman's rank correlation coefficient
for two inputs.  The data is replaced by ranks.  Ties are averaged
so that equal values receive the same rank.  The resulting coefficient
measures the strength of a monotonic relationship.

Spearman's rank correlation coefficient is appropriate for ordinal
data or for continuous data that doesn't meet the linear proportion
requirement for Pearson's correlation coefficient.

```python
def correlation()
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 1301
