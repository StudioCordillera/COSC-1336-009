---
type: function
name: setheading
module: turtle
lineno: 1908
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: setheading()

## Overview

Set the orientation of the turtle to to_angle.

Aliases:  setheading | seth

Argument:
to_angle -- a number (integer or float)

Set the orientation of the turtle to to_angle.
Here are some common directions in degrees:

 standard - mode:          logo-mode:
-------------------|--------------------
   0 - east                0 - north
  90 - north              90 - east
 180 - west              180 - south
 270 - south             270 - west

Example (for a Turtle instance named turtle):
>>> turtle.setheading(90)
>>> turtle.heading()
90

```python
def setheading(self, to_angle)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TNavigator|TNavigator]]
**Type:** Method
**Line:** 1908

## Categories

- [[Taxonomy/public_method|public_method]]
