---
type: function
name: median
module: statistics
lineno: 621
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: median()

## Overview

Return the median (middle value) of numeric data.

When the number of data points is odd, return the middle data point.
When the number of data points is even, the median is interpolated by
taking the average of the two middle values:

>>> median([1, 3, 5])
3
>>> median([1, 3, 5, 7])
4.0

```python
def median(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 621
