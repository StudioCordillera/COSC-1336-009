---
type: function
name: onrelease
module: turtle
lineno: 3581
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: onrelease()

## Overview

Bind fun to mouse-button-release event on this turtle on canvas.

Arguments:
fun -- a function with two arguments, to which will be assigned
        the coordinates of the clicked point on the canvas.
btn --  number of the mouse-button defaults to 1 (left mouse button).

Example (for a MyTurtle instance named joe):
>>> class MyTurtle(Turtle):
...     def glow(self,x,y):
...             self.fillcolor("red")
...     def unglow(self,x,y):
...             self.fillcolor("")
...
>>> joe = MyTurtle()
>>> joe.onclick(joe.glow)
>>> joe.onrelease(joe.unglow)

Clicking on joe turns fillcolor red, unclicking turns it to
transparent.

```python
def onrelease(self, fun, btn, add)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3581

## Categories

- [[Taxonomy/public_method|public_method]]
