---
type: function
name: degrees
module: turtle
lineno: 1555
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: degrees()

## Overview

Set angle measurement units to degrees.

Optional argument:
fullcircle -  a number

Set angle measurement units, i. e. set number
of 'degrees' for a full circle. Default value is
360 degrees.

Example (for a Turtle instance named turtle):
>>> turtle.left(90)
>>> turtle.heading()
90

Change angle measurement unit to grad (also known as gon,
grade, or gradian and equals 1/100-th of the right angle.)
>>> turtle.degrees(400.0)
>>> turtle.heading()
100

```python
def degrees(self, fullcircle)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TNavigator|TNavigator]]
**Type:** Method
**Line:** 1555

## Categories

- [[Taxonomy/public_method|public_method]]
