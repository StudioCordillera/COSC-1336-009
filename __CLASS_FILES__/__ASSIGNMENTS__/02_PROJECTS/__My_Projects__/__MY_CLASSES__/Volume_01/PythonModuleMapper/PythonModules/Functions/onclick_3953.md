---
type: function
name: onclick
module: turtle
lineno: 1340
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: onclick()

## Overview

Bind fun to mouse-click event on canvas.

Arguments:
fun -- a function with two arguments, the coordinates of the
       clicked point on the canvas.
btn -- the number of the mouse-button, defaults to 1

Example (for a TurtleScreen instance named screen)

>>> screen.onclick(goto)
>>> # Subsequently clicking into the TurtleScreen will
>>> # make the turtle move to the clicked point.
>>> screen.onclick(None)

```python
def onclick(self, fun, btn, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1340

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
