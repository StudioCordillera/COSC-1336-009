---
type: function
name: pensize
module: turtle
lineno: 2070
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: pensize()

## Overview

Set or return the line thickness.

Aliases:  pensize | width

Argument:
width -- positive number

Set the line thickness to width or return it. If resizemode is set
to "auto" and turtleshape is a polygon, that polygon is drawn with
the same line thickness. If no argument is given, current pensize
is returned.

Example (for a Turtle instance named turtle):
>>> turtle.pensize()
1
>>> turtle.pensize(10)   # from here on lines of width 10 are drawn

```python
def pensize(self, width)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2070

## Categories

- [[Taxonomy/public_method|public_method]]
