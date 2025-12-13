---
type: function
name: harmonic_mean
module: statistics
lineno: 565
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: harmonic_mean()

## Overview

Return the harmonic mean of data.

The harmonic mean is the reciprocal of the arithmetic mean of the
reciprocals of the data.  It can be used for averaging ratios or
rates, for example speeds.

Suppose a car travels 40 km/hr for 5 km and then speeds-up to
60 km/hr for another 5 km. What is the average speed?

    >>> harmonic_mean([40, 60])
    48.0

Suppose a car travels 40 km/hr for 5 km, and when traffic clears,
speeds-up to 60 km/hr for the remaining 30 km of the journey. What
is the average speed?

    >>> harmonic_mean([40, 60], weights=[5, 30])
    56.0

If ``data`` is empty, or any element is less than zero,
``harmonic_mean`` will raise ``StatisticsError``.

```python
def harmonic_mean(data, weights)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 565
