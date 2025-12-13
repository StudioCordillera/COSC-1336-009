---
type: function
name: stamp
module: turtle
lineno: 3075
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: stamp()

## Overview

Stamp a copy of the turtleshape onto the canvas and return its id.

No argument.

Stamp a copy of the turtle shape onto the canvas at the current
turtle position. Return a stamp_id for that stamp, which can be
used to delete it by calling clearstamp(stamp_id).

Example (for a Turtle instance named turtle):
>>> turtle.color("blue")
>>> turtle.stamp()
13
>>> turtle.fd(50)

```python
def stamp(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3075

## Categories

- [[Taxonomy/public_method|public_method]]
