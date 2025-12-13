---
type: function
name: register_shape
module: turtle
lineno: 1098
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: register_shape()

## Overview

Adds a turtle shape to TurtleScreen's shapelist.

Arguments:
(1) name is the name of a gif-file and shape is None.
    Installs the corresponding image shape.
    !! Image-shapes DO NOT rotate when turning the turtle,
    !! so they do not display the heading of the turtle!
(2) name is an arbitrary string and shape is a tuple
    of pairs of coordinates. Installs the corresponding
    polygon shape
(3) name is an arbitrary string and shape is a
    (compound) Shape object. Installs the corresponding
    compound shape.
To use a shape, you have to issue the command shape(shapename).

call: register_shape("turtle.gif")
--or: register_shape("tri", ((0,0), (10,10), (-10,10)))

Example (for a TurtleScreen instance named screen):
>>> screen.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

```python
def register_shape(self, name, shape)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1098

## Categories

- [[Taxonomy/public_method|public_method]]
