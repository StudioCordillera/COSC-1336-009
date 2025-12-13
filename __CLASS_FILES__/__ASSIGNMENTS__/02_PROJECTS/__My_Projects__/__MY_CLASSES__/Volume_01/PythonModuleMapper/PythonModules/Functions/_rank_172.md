---
type: function
name: _rank
module: statistics
lineno: 363
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _rank()

## Overview

Rank order a dataset. The lowest value has rank 1.

Ties are averaged so that equal values receive the same rank:

    >>> data = [31, 56, 31, 25, 75, 18]
    >>> _rank(data)
    [3.5, 5.0, 3.5, 2.0, 6.0, 1.0]

The operation is idempotent:

    >>> _rank([3.5, 5.0, 3.5, 2.0, 6.0, 1.0])
    [3.5, 5.0, 3.5, 2.0, 6.0, 1.0]

It is possible to rank the data in reverse order so that the
highest value has rank 1.  Also, a key-function can extract
the field to be ranked:

    >>> goals = [('eagles', 45), ('bears', 48), ('lions', 44)]
    >>> _rank(goals, key=itemgetter(1), reverse=True)
    [2.0, 1.0, 3.0]

Ranks are conventionally numbered starting from one; however,
setting *start* to zero allows the ranks to be used as array indices:

    >>> prize = ['Gold', 'Silver', 'Bronze', 'Certificate']
    >>> scores = [8.1, 7.3, 9.4, 8.3]
    >>> [prize[int(i)] for i in _rank(scores, start=0, reverse=True)]
    ['Bronze', 'Certificate', 'Gold', 'Silver']

```python
def _rank() -> list[float]
```

**Module:** [[Modules/statistics|statistics]]
**Type:** Module-level function
**Line:** 363
