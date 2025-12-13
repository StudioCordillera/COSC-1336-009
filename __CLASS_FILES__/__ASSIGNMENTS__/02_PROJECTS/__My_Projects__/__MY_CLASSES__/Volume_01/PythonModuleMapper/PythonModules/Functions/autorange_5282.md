---
type: function
name: autorange
module: timeit
lineno: 212
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: autorange()

## Overview

Return the number of loops and time taken so that total time >= 0.2.

Calls the timeit method with increasing numbers from the sequence
1, 2, 5, 10, 20, 50, ... until the time taken is at least 0.2
second.  Returns (number, time_taken).

If *callback* is given and is not None, it will be called after
each trial with two arguments: ``callback(number, time_taken)``.

```python
def autorange(self, callback)
```

**Module:** [[Modules/timeit|timeit]]
**Class:** [[Classes/Timer|Timer]]
**Type:** Method
**Line:** 212

## Categories

- [[Taxonomy/public_method|public_method]]
