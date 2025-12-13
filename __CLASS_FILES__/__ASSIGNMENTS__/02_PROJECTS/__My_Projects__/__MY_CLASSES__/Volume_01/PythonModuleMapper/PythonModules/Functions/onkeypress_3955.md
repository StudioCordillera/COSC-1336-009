---
type: function
name: onkeypress
module: turtle
lineno: 1387
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: onkeypress()

## Overview

Bind fun to key-press event of key if key is given,
or to any key-press-event if no key is given.

Arguments:
fun -- a function with no arguments
key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

In order to be able to register key-events, TurtleScreen
must have focus. (See method listen.)

Example (for a TurtleScreen instance named screen
and a Turtle instance named turtle):

>>> def f():
...     fd(50)
...     lt(60)
...
>>> screen.onkeypress(f, "Up")
>>> screen.listen()

Subsequently the turtle can be moved by repeatedly pressing
the up-arrow key, or by keeping pressed the up-arrow key.
consequently drawing a hexagon.

```python
def onkeypress(self, fun, key)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1387

## Categories

- [[Taxonomy/public_method|public_method]]
