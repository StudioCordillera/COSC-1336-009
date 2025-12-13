---
type: function
name: ontimer
module: turtle
lineno: 1431
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: ontimer()

## Overview

Install a timer, which calls fun after t milliseconds.

Arguments:
fun -- a function with no arguments.
t -- a number >= 0

Example (for a TurtleScreen instance named screen):

>>> running = True
>>> def f():
...     if running:
...             fd(50)
...             lt(60)
...             screen.ontimer(f, 250)
...
>>> f()   # makes the turtle marching around
>>> running = False

```python
def ontimer(self, fun, t)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1431

## Categories

- [[Taxonomy/public_method|public_method]]
