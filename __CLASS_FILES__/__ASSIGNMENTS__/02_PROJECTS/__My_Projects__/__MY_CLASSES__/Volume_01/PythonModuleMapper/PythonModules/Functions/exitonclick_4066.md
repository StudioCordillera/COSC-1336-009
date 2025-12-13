---
type: function
name: exitonclick
module: turtle
lineno: 3800
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: exitonclick()

## Overview

Go into mainloop until the mouse is clicked.

No arguments.

Bind bye() method to mouseclick on TurtleScreen.
If "using_IDLE" - value in configuration dictionary is False
(default value), enter mainloop.
If IDLE with -n switch (no subprocess) is used, this value should be
set to True in turtle.cfg. In this case IDLE's mainloop
is active also for the client script.

This is a method of the Screen-class and not available for
TurtleScreen instances.

Example (for a Screen instance named screen):
>>> screen.exitonclick()

```python
def exitonclick(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/_Screen|_Screen]]
**Type:** Method
**Line:** 3800

## Categories

- [[Taxonomy/public_method|public_method]]
