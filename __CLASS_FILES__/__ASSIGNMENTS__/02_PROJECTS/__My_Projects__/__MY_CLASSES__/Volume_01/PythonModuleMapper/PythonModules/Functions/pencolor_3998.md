---
type: function
name: pencolor
module: turtle
lineno: 2220
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: pencolor()

## Overview

Return or set the pencolor.

Arguments:
Four input formats are allowed:
  - pencolor()
    Return the current pencolor as color specification string,
    possibly in hex-number format (see example).
    May be used as input to another color/pencolor/fillcolor call.
  - pencolor(colorstring)
    s is a Tk color specification string, such as "red" or "yellow"
  - pencolor((r, g, b))
    *a tuple* of r, g, and b, which represent, an RGB color,
    and each of r, g, and b are in the range 0..colormode,
    where colormode is either 1.0 or 255
  - pencolor(r, g, b)
    r, g, and b represent an RGB color, and each of r, g, and b
    are in the range 0..colormode

If turtleshape is a polygon, the outline of that polygon is drawn
with the newly set pencolor.

Example (for a Turtle instance named turtle):
>>> turtle.pencolor('brown')
>>> tup = (0.2, 0.8, 0.55)
>>> turtle.pencolor(tup)
>>> turtle.pencolor()
'#33cc8c'

```python
def pencolor(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2220

## Categories

- [[Taxonomy/public_method|public_method]]
