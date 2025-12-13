---
type: function
name: shearfactor
module: turtle
lineno: 2875
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shearfactor()

## Overview

Set or return the current shearfactor.

Optional argument: shear -- number, tangent of the shear angle

Shear the turtleshape according to the given shearfactor shear,
which is the tangent of the shear angle. DO NOT change the
turtle's heading (direction of movement).
If shear is not given: return the current shearfactor, i. e. the
tangent of the shear angle, by which lines parallel to the
heading of the turtle are sheared.

Examples (for a Turtle instance named turtle):
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.shearfactor(0.5)
>>> turtle.shearfactor()
>>> 0.5

```python
def shearfactor(self, shear)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2875

## Categories

- [[Taxonomy/public_method|public_method]]
