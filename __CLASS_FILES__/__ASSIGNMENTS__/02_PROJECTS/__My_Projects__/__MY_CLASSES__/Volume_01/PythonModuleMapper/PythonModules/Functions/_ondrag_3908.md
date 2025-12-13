---
type: function
name: _ondrag
module: turtle
lineno: 628
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _ondrag()

## Overview

Bind fun to mouse-move-event (with pressed mouse button) on turtle.
fun must be a function with two arguments, the coordinates of the
actual mouse position on the canvas.
num, the number of the mouse-button defaults to 1

Every sequence of mouse-move-events on a turtle is preceded by a
mouse-click event on that turtle.

```python
def _ondrag(self, item, fun, num, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 628

## Categories

- [[Taxonomy/protected_method|protected_method]]
