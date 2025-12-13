---
type: function
name: setundobuffer
module: turtle
lineno: 2591
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: setundobuffer()

## Overview

Set or disable undobuffer.

Argument:
size -- an integer or None

If size is an integer an empty undobuffer of given size is installed.
Size gives the maximum number of turtle-actions that can be undone
by the undo() function.
If size is None, no undobuffer is present.

Example (for a Turtle instance named turtle):
>>> turtle.setundobuffer(42)

```python
def setundobuffer(self, size)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2591

## Categories

- [[Taxonomy/public_method|public_method]]
