---
type: function
name: circle
module: turtle
lineno: 1936
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: circle()

## Overview

Draw a circle with given radius.

Arguments:
radius -- a number
extent (optional) -- a number
steps (optional) -- an integer

Draw a circle with given radius. The center is radius units left
of the turtle; extent - an angle - determines which part of the
circle is drawn. If extent is not given, draw the entire circle.
If extent is not a full circle, one endpoint of the arc is the
current pen position. Draw the arc in counterclockwise direction
if radius is positive, otherwise in clockwise direction. Finally
the direction of the turtle is changed by the amount of extent.

As the circle is approximated by an inscribed regular polygon,
steps determines the number of steps to use. If not given,
it will be calculated automatically. Maybe used to draw regular
polygons.

call: circle(radius)                  # full circle
--or: circle(radius, extent)          # arc
--or: circle(radius, extent, steps)
--or: circle(radius, steps=6)         # 6-sided polygon

Example (for a Turtle instance named turtle):
>>> turtle.circle(50)
>>> turtle.circle(120, 180)  # semicircle

```python
def circle(self, radius, extent, steps)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TNavigator|TNavigator]]
**Type:** Method
**Line:** 1936

## Categories

- [[Taxonomy/public_method|public_method]]
