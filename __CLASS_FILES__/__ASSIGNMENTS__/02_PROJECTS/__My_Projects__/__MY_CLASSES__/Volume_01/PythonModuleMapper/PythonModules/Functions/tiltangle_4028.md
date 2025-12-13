---
type: function
name: tiltangle
module: turtle
lineno: 2898
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: tiltangle()

## Overview

Set or return the current tilt-angle.

Optional argument: angle -- number

Rotate the turtleshape to point in the direction specified by angle,
regardless of its current tilt-angle. DO NOT change the turtle's
heading (direction of movement).
If angle is not given: return the current tilt-angle, i. e. the angle
between the orientation of the turtleshape and the heading of the
turtle (its direction of movement).

Examples (for a Turtle instance named turtle):
>>> turtle.shape("circle")
>>> turtle.shapesize(5, 2)
>>> turtle.tiltangle()
0.0
>>> turtle.tiltangle(45)
>>> turtle.tiltangle()
45.0
>>> turtle.stamp()
>>> turtle.fd(50)
>>> turtle.tiltangle(-45)
>>> turtle.tiltangle()
315.0
>>> turtle.stamp()
>>> turtle.fd(50)

```python
def tiltangle(self, angle)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2898

## Categories

- [[Taxonomy/public_method|public_method]]
