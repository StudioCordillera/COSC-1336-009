---
type: function
name: resizemode
module: turtle
lineno: 2042
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: resizemode()

## Overview

Set resizemode to one of the values: "auto", "user", "noresize".

(Optional) Argument:
rmode -- one of the strings "auto", "user", "noresize"

Different resizemodes have the following effects:
  - "auto" adapts the appearance of the turtle
           corresponding to the value of pensize.
  - "user" adapts the appearance of the turtle according to the
           values of stretchfactor and outlinewidth (outline),
           which are set by shapesize()
  - "noresize" no adaption of the turtle's appearance takes place.
If no argument is given, return current resizemode.
resizemode("user") is called by a call of shapesize with arguments.


Examples (for a Turtle instance named turtle):
>>> turtle.resizemode("noresize")
>>> turtle.resizemode()
'noresize'

```python
def resizemode(self, rmode)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TPen|TPen]]
**Type:** Method
**Line:** 2042

## Categories

- [[Taxonomy/public_method|public_method]]
