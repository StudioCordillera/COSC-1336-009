---
type: function
name: _onscreenclick
module: turtle
lineno: 649
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _onscreenclick()

## Overview

Bind fun to mouse-click event on canvas.
fun must be a function with two arguments, the coordinates
of the clicked point on the canvas.
num, the number of the mouse-button defaults to 1

If a turtle is clicked, first _onclick-event will be performed,
then _onscreensclick-event.

```python
def _onscreenclick(self, fun, num, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 649

## Categories

- [[Taxonomy/protected_method|protected_method]]
