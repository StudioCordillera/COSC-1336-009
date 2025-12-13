---
type: function
name: speed
module: turtle
lineno: 2136
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: speed()

## Overview

Return or set the turtle's speed.

Optional argument:
speed -- an integer in the range 0..10 or a speedstring (see below)

Set the turtle's speed to an integer value in the range 0 .. 10.
If no argument is given: return current speed.

If input is a number greater than 10 or smaller than 0.5,
speed is set to 0.
Speedstrings  are mapped to speedvalues in the following way:
    'fastest' :  0
    'fast'    :  10
    'normal'  :  6
    'slow'    :  3
    'slowest' :  1
speeds from 1 to 10 enforce increasingly faster animation of
line drawing and turtle turning.

Attention:
speed = 0 : *no* animation takes place. forward/back makes turtle jump
and likewise left/right make the turtle turn instantly.

Example (for a Turtle instance named turtle):
>>> turtle.speed(3)

```python
def speed(self, speed)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2136
