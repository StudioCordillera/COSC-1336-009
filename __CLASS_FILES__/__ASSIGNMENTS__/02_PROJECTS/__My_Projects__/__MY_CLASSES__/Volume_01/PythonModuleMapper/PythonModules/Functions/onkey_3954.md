---
type: function
name: onkey
module: turtle
lineno: 1357
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: onkey()

## Overview

Bind fun to key-release event of key.

Arguments:
fun -- a function with no arguments
key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

In order to be able to register key-events, TurtleScreen
must have focus. (See method listen.)

Example (for a TurtleScreen instance named screen):

>>> def f():
...     fd(50)
...     lt(60)
...
>>> screen.onkey(f, "Up")
>>> screen.listen()

Subsequently the turtle can be moved by repeatedly pressing
the up-arrow key, consequently drawing a hexagon

```python
def onkey(self, fun, key)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1357

## Categories

- [[Taxonomy/public_method|public_method]]
