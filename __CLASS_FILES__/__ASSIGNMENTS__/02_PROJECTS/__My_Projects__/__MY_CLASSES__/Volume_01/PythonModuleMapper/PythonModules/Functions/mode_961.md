---
type: function
name: mode
module: statistics
lineno: 758
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: mode()

## Overview

Return the most common data point from discrete or nominal data.

``mode`` assumes discrete data, and returns a single value. This is the
standard treatment of the mode as commonly taught in schools:

    >>> mode([1, 1, 2, 3, 3, 3, 3, 4])
    3

This also works with nominal (non-numeric) data:

    >>> mode(["red", "blue", "blue", "red", "green", "red", "red"])
    'red'

If there are multiple modes with same frequency, return the first one
encountered:

    >>> mode(['red', 'red', 'green', 'blue', 'blue'])
    'red'

If *data* is empty, ``mode``, raises StatisticsError.

```python
def mode(data)
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 758
