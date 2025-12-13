---
type: function
name: median_grouped
module: statistics
lineno: 686
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: median_grouped()

## Overview

Estimates the median for numeric data binned around the midpoints
of consecutive, fixed-width intervals.

The *data* can be any iterable of numeric data with each value being
exactly the midpoint of a bin.  At least one value must be present.

The *interval* is width of each bin.

For example, demographic information may have been summarized into
consecutive ten-year age groups with each group being represented
by the 5-year midpoints of the intervals:

    >>> demographics = Counter({
    ...    25: 172,   # 20 to 30 years old
    ...    35: 484,   # 30 to 40 years old
    ...    45: 387,   # 40 to 50 years old
    ...    55:  22,   # 50 to 60 years old
    ...    65:   6,   # 60 to 70 years old
    ... })

The 50th percentile (median) is the 536th person out of the 1071
member cohort.  That person is in the 30 to 40 year old age group.

The regular median() function would assume that everyone in the
tricenarian age group was exactly 35 years old.  A more tenable
assumption is that the 484 members of that age group are evenly
distributed between 30 and 40.  For that, we use median_grouped().

    >>> data = list(demographics.elements())
    >>> median(data)
    35
    >>> round(median_grouped(data, interval=10), 1)
    37.5

The caller is responsible for making sure the data points are separated
by exact multiples of *interval*.  This is essential for getting a
correct result.  The function does not check this precondition.

Inputs may be any numeric type that can be coerced to a float during
the interpolation step.

```python
def median_grouped(data, interval)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 686
