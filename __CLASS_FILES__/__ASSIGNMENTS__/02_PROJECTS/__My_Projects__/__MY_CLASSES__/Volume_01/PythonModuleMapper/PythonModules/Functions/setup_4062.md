---
type: function
name: setup
module: turtle
lineno: 3725
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: setup()

## Overview

Set the size and position of the main window.

Arguments:
width: as integer a size in pixels, as float a fraction of the screen.
  Default is 50% of screen.
height: as integer the height in pixels, as float a fraction of the
  screen. Default is 75% of screen.
startx: if positive, starting position in pixels from the left
  edge of the screen, if negative from the right edge
  Default, startx=None is to center window horizontally.
starty: if positive, starting position in pixels from the top
  edge of the screen, if negative from the bottom edge
  Default, starty=None is to center window vertically.

Examples (for a Screen instance named screen):
>>> screen.setup (width=200, height=200, startx=0, starty=0)

sets window to 200x200 pixels, in upper left of screen

>>> screen.setup(width=.75, height=0.5, startx=None, starty=None)

sets window to 75% of screen by 50% of screen and centers

```python
def setup(self, width, height, startx, starty)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/_Screen|_Screen]]
**Type:** Method
**Line:** 3725

## Categories

- [[Taxonomy/public_method|public_method]]
