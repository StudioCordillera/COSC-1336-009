---
type: function
name: distance
module: turtle
lineno: 1826
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: distance()

## Overview

Return the distance from the turtle to (x,y) in turtle step units.

Arguments:
x -- a number   or  a pair/vector of numbers   or   a turtle instance
y -- a number       None                            None

call: distance(x, y)         # two coordinates
--or: distance((x, y))       # a pair (tuple) of coordinates
--or: distance(vec)          # e.g. as returned by pos()
--or: distance(mypen)        # where mypen is another turtle

Example (for a Turtle instance named turtle):
>>> turtle.pos()
(0.00, 0.00)
>>> turtle.distance(30,40)
50.0
>>> pen = Turtle()
>>> pen.forward(77)
>>> turtle.distance(pen)
77.0

```python
def distance(self, x, y)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TNavigator|TNavigator]]
**Type:** Method
**Line:** 1826

## Categories

- [[Taxonomy/public_method|public_method]]
