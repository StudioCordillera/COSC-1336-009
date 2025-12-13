---
type: function
name: repeat
module: timeit
lineno: 186
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: repeat()

## Overview

Call timeit() a few times.

This is a convenience function that calls the timeit()
repeatedly, returning a list of results.  The first argument
specifies how many times to call timeit(), defaulting to 5;
the second argument specifies the timer argument, defaulting
to one million.

Note: it's tempting to calculate mean and standard deviation
from the result vector and report these.  However, this is not
very useful.  In a typical case, the lowest value gives a
lower bound for how fast your machine can run the given code
snippet; higher values in the result vector are typically not
caused by variability in Python's speed, but by other
processes interfering with your timing accuracy.  So the min()
of the result is probably the only number you should be
interested in.  After that, you should look at the entire
vector and apply common sense rather than statistics.

```python
def repeat(self, repeat, number)
```

**Module:** [[Modules/timeit|timeit]]
**Class:** [[Classes/Timer|Timer]]
**Type:** Method
**Line:** 186

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
