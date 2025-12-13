---
type: function
name: tracer
module: turtle
lineno: 1236
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: tracer()

## Overview

Turns turtle animation on/off and set delay for update drawings.

Optional arguments:
n -- nonnegative  integer
delay -- nonnegative  integer

If n is given, only each n-th regular screen update is really performed.
(Can be used to accelerate the drawing of complex graphics.)
Second arguments sets delay value (see RawTurtle.delay())

Example (for a TurtleScreen instance named screen):
>>> screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

```python
def tracer(self, n, delay)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1236

## Categories

- [[Taxonomy/public_method|public_method]]
