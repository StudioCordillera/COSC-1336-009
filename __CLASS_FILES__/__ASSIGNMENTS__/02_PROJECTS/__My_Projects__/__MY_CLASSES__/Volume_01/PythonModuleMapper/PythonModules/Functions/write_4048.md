---
type: function
name: write
module: turtle
lineno: 3446
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write()

## Overview

Write text at the current turtle position.

Arguments:
arg -- info, which is to be written to the TurtleScreen
move (optional) -- True/False
align (optional) -- one of the strings "left", "center" or right"
font (optional) -- a triple (fontname, fontsize, fonttype)

Write text - the string representation of arg - at the current
turtle position according to align ("left", "center" or right")
and with the given font.
If move is True, the pen is moved to the bottom-right corner
of the text. By default, move is False.

Example (for a Turtle instance named turtle):
>>> turtle.write('Home = ', True, align="center")
>>> turtle.write((0,0), True)

```python
def write(self, arg, move, align, font)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3446

## Categories

- [[Taxonomy/public_method|public_method]]
