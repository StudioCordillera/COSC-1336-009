---
type: function
name: setworldcoordinates
module: turtle
lineno: 1059
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: setworldcoordinates()

## Overview

Set up a user defined coordinate-system.

Arguments:
llx -- a number, x-coordinate of lower left corner of canvas
lly -- a number, y-coordinate of lower left corner of canvas
urx -- a number, x-coordinate of upper right corner of canvas
ury -- a number, y-coordinate of upper right corner of canvas

Set up user coodinat-system and switch to mode 'world' if necessary.
This performs a screen.reset. If mode 'world' is already active,
all drawings are redrawn according to the new coordinates.

But ATTENTION: in user-defined coordinatesystems angles may appear
distorted. (see Screen.mode())

Example (for a TurtleScreen instance named screen):
>>> screen.setworldcoordinates(-10,-0.5,50,1.5)
>>> for _ in range(36):
...     left(10)
...     forward(0.5)

```python
def setworldcoordinates(self, llx, lly, urx, ury)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1059

## Categories

- [[Taxonomy/public_method|public_method]]
