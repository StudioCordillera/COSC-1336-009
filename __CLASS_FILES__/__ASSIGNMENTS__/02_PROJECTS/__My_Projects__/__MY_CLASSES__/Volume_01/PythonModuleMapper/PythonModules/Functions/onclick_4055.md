---
type: function
name: onclick
module: turtle
lineno: 3560
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: onclick()

## Overview

Bind fun to mouse-click event on this turtle on canvas.

Arguments:
fun --  a function with two arguments, to which will be assigned
        the coordinates of the clicked point on the canvas.
btn --  number of the mouse-button defaults to 1 (left mouse button).
add --  True or False. If True, new binding will be added, otherwise
        it will replace a former binding.

Example for the anonymous turtle, i. e. the procedural way:

>>> def turn(x, y):
...     left(360)
...
>>> onclick(turn)  # Now clicking into the turtle will turn it.
>>> onclick(None)  # event-binding will be removed

```python
def onclick(self, fun, btn, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3560
