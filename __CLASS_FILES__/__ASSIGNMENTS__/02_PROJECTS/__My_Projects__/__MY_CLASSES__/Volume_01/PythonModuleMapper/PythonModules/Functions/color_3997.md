---
type: function
name: color
module: turtle
lineno: 2174
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: color()

## Overview

Return or set the pencolor and fillcolor.

Arguments:
Several input formats are allowed.
They use 0, 1, 2, or 3 arguments as follows:

color()
    Return the current pencolor and the current fillcolor
    as a pair of color specification strings as are returned
    by pencolor and fillcolor.
color(colorstring), color((r,g,b)), color(r,g,b)
    inputs as in pencolor, set both, fillcolor and pencolor,
    to the given value.
color(colorstring1, colorstring2),
color((r1,g1,b1), (r2,g2,b2))
    equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
    and analogously, if the other input format is used.

If turtleshape is a polygon, outline and interior of that polygon
is drawn with the newly set colors.
For more info see: pencolor, fillcolor

Example (for a Turtle instance named turtle):
>>> turtle.color('red', 'green')
>>> turtle.color()
('red', 'green')
>>> colormode(255)
>>> color((40, 80, 120), (160, 200, 240))
>>> color()
('#285078', '#a0c8f0')

```python
def color(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2174

## Categories

- [[Taxonomy/public_method|public_method]]
