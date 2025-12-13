---
type: function
name: shapesize
module: turtle
lineno: 2835
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shapesize()

## Overview

Set/return turtle's stretchfactors/outline. Set resizemode to "user".

Optional arguments:
   stretch_wid : positive number
   stretch_len : positive number
   outline  : positive number

Return or set the pen's attributes x/y-stretchfactors and/or outline.
Set resizemode to "user".
If and only if resizemode is set to "user", the turtle will be displayed
stretched according to its stretchfactors:
stretch_wid is stretchfactor perpendicular to orientation
stretch_len is stretchfactor in direction of turtles orientation.
outline determines the width of the shapes's outline.

Examples (for a Turtle instance named turtle):
>>> turtle.resizemode("user")
>>> turtle.shapesize(5, 5, 12)
>>> turtle.shapesize(outline=8)

```python
def shapesize(self, stretch_wid, stretch_len, outline)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2835

## Categories

- [[Taxonomy/public_method|public_method]]
