---
type: function
name: towards
module: turtle
lineno: 1858
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: towards()

## Overview

Return the angle of the line from the turtle's position to (x, y).

Arguments:
x -- a number   or  a pair/vector of numbers   or   a turtle instance
y -- a number       None                            None

call: distance(x, y)         # two coordinates
--or: distance((x, y))       # a pair (tuple) of coordinates
--or: distance(vec)          # e.g. as returned by pos()
--or: distance(mypen)        # where mypen is another turtle

Return the angle, between the line from turtle-position to position
specified by x, y and the turtle's start orientation. (Depends on
modes - "standard" or "logo")

Example (for a Turtle instance named turtle):
>>> turtle.pos()
(10.00, 10.00)
>>> turtle.towards(0,0)
225.0

```python
def towards(self, x, y)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TNavigator|TNavigator]]
**Type:** Method
**Line:** 1858

## Categories

- [[Taxonomy/public_method|public_method]]
