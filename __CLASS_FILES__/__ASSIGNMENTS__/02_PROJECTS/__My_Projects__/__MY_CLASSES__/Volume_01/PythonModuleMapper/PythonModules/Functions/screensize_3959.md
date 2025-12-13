---
type: function
name: screensize
module: turtle
lineno: 1476
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: screensize()

## Overview

Resize the canvas the turtles are drawing on.

Optional arguments:
canvwidth -- positive integer, new width of canvas in pixels
canvheight --  positive integer, new height of canvas in pixels
bg -- colorstring or color-tuple, new backgroundcolor
If no arguments are given, return current (canvaswidth, canvasheight)

Do not alter the drawing window. To observe hidden parts of
the canvas use the scrollbars. (Can make visible those parts
of a drawing, which were outside the canvas before!)

Example (for a Turtle instance named turtle):
>>> turtle.screensize(2000,1500)
>>> # e.g. to search for an erroneously escaped turtle ;-)

```python
def screensize(self, canvwidth, canvheight, bg)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1476

## Categories

- [[Taxonomy/public_method|public_method]]
