---
type: function
name: shapetransform
module: turtle
lineno: 2953
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shapetransform()

## Overview

Set or return the current transformation matrix of the turtle shape.

Optional arguments: t11, t12, t21, t22 -- numbers.

If none of the matrix elements are given, return the transformation
matrix.
Otherwise set the given elements and transform the turtleshape
according to the matrix consisting of first row t11, t12 and
second row t21, 22.
Modify stretchfactor, shearfactor and tiltangle according to the
given matrix.

Examples (for a Turtle instance named turtle):
>>> turtle.shape("square")
>>> turtle.shapesize(4,2)
>>> turtle.shearfactor(-0.5)
>>> turtle.shapetransform()
(4.0, -1.0, -0.0, 2.0)

```python
def shapetransform(self, t11, t12, t21, t22)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2953

## Categories

- [[Taxonomy/public_method|public_method]]
