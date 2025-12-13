---
type: function
name: clearstamps
module: turtle
lineno: 3157
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: clearstamps()

## Overview

Delete all or first/last n of turtle's stamps.

Optional argument:
n -- an integer

If n is None, delete all of pen's stamps,
else if n > 0 delete first n stamps
else if n < 0 delete last n stamps.

Example (for a Turtle instance named turtle):
>>> for i in range(8):
...     turtle.stamp(); turtle.fd(30)
...
>>> turtle.clearstamps(2)
>>> turtle.clearstamps(-2)
>>> turtle.clearstamps()

```python
def clearstamps(self, n)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3157

## Categories

- [[Taxonomy/public_method|public_method]]
