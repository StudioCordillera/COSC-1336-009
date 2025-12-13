---
type: function
name: _tracer
module: turtle
lineno: 2678
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: _tracer()

## Overview

Turns turtle animation on/off and set delay for update drawings.

Optional arguments:
n -- nonnegative  integer
delay -- nonnegative  integer

If n is given, only each n-th regular screen update is really performed.
(Can be used to accelerate the drawing of complex graphics.)
Second arguments sets delay value (see RawTurtle.delay())

Example (for a Turtle instance named turtle):
>>> turtle.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     turtle.fd(dist)
...     turtle.rt(90)
...     dist += 2

```python
def _tracer(self, flag, delay)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2678
