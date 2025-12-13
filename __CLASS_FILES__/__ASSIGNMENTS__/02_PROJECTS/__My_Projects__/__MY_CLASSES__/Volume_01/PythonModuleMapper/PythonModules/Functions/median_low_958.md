---
type: function
name: median_low
module: statistics
lineno: 645
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: median_low()

## Overview

Return the low median of numeric data.

When the number of data points is odd, the middle value is returned.
When it is even, the smaller of the two middle values is returned.

>>> median_low([1, 3, 5])
3
>>> median_low([1, 3, 5, 7])
3

```python
def median_low(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 645
