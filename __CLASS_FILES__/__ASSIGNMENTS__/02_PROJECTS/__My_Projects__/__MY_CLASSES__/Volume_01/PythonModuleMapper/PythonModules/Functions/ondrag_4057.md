---
type: function
name: ondrag
module: turtle
lineno: 3606
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: ondrag()

## Overview

Bind fun to mouse-move event on this turtle on canvas.

Arguments:
fun -- a function with two arguments, to which will be assigned
       the coordinates of the clicked point on the canvas.
btn -- number of the mouse-button defaults to 1 (left mouse button).

Every sequence of mouse-move-events on a turtle is preceded by a
mouse-click event on that turtle.

Example (for a Turtle instance named turtle):
>>> turtle.ondrag(turtle.goto)

Subsequently clicking and dragging a Turtle will move it
across the screen thereby producing handdrawings (if pen is
down).

```python
def ondrag(self, fun, btn, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3606

## Categories

- [[Taxonomy/public_method|public_method]]
