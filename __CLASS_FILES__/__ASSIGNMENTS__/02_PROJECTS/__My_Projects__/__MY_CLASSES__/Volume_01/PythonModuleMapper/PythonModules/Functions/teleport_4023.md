---
type: function
name: teleport
module: turtle
lineno: 2720
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: teleport()

## Overview

Instantly move turtle to an absolute position.

Arguments:
x -- a number      or     None
y -- a number             None
fill_gap -- a boolean     This argument must be specified by name.

call: teleport(x, y)         # two coordinates
--or: teleport(x)            # teleport to x position, keeping y as is
--or: teleport(y=y)          # teleport to y position, keeping x as is
--or: teleport(x, y, fill_gap=True)
                             # teleport but fill the gap in between

Move turtle to an absolute position. Unlike goto(x, y), a line will not
be drawn. The turtle's orientation does not change. If currently
filling, the polygon(s) teleported from will be filled after leaving,
and filling will begin again after teleporting. This can be disabled
with fill_gap=True, which makes the imaginary line traveled during
teleporting act as a fill barrier like in goto(x, y).

Example (for a Turtle instance named turtle):
>>> tp = turtle.pos()
>>> tp
(0.00,0.00)
>>> turtle.teleport(60)
>>> turtle.pos()
(60.00,0.00)
>>> turtle.teleport(y=10)
>>> turtle.pos()
(60.00,10.00)
>>> turtle.teleport(20, 30)
>>> turtle.pos()
(20.00,30.00)

```python
def teleport(self, x, y) -> None
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2720
