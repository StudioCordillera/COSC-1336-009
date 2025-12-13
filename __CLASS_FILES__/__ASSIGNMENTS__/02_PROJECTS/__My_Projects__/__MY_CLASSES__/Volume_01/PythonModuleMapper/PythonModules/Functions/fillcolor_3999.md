---
type: function
name: fillcolor
module: turtle
lineno: 2257
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: fillcolor()

## Overview

Return or set the fillcolor.

Arguments:
Four input formats are allowed:
  - fillcolor()
    Return the current fillcolor as color specification string,
    possibly in hex-number format (see example).
    May be used as input to another color/pencolor/fillcolor call.
  - fillcolor(colorstring)
    s is a Tk color specification string, such as "red" or "yellow"
  - fillcolor((r, g, b))
    *a tuple* of r, g, and b, which represent, an RGB color,
    and each of r, g, and b are in the range 0..colormode,
    where colormode is either 1.0 or 255
  - fillcolor(r, g, b)
    r, g, and b represent an RGB color, and each of r, g, and b
    are in the range 0..colormode

If turtleshape is a polygon, the interior of that polygon is drawn
with the newly set fillcolor.

Example (for a Turtle instance named turtle):
>>> turtle.fillcolor('violet')
>>> col = turtle.pencolor()
>>> turtle.fillcolor(col)
>>> turtle.fillcolor(0, .5, 0)

```python
def fillcolor(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2257

## Categories

- [[Taxonomy/public_method|public_method]]
