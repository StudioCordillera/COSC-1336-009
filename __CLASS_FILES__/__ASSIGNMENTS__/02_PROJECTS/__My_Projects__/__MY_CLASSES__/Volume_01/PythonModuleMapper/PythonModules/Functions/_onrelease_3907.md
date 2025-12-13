---
type: function
name: _onrelease
module: turtle
lineno: 609
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _onrelease()

## Overview

Bind fun to mouse-button-release event on turtle.
fun must be a function with two arguments, the coordinates
of the point on the canvas where mouse button is released.
num, the number of the mouse-button defaults to 1

If a turtle is clicked, first _onclick-event will be performed,
then _onscreensclick-event.

```python
def _onrelease(self, item, fun, num, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 609

## Categories

- [[Taxonomy/protected_method|protected_method]]
