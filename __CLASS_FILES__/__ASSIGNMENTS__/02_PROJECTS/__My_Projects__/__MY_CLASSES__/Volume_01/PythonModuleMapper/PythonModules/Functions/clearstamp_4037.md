---
type: function
name: clearstamp
module: turtle
lineno: 3142
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: clearstamp()

## Overview

Delete stamp with given stampid

Argument:
stampid - an integer, must be return value of previous stamp() call.

Example (for a Turtle instance named turtle):
>>> turtle.color("blue")
>>> astamp = turtle.stamp()
>>> turtle.fd(50)
>>> turtle.clearstamp(astamp)

```python
def clearstamp(self, stampid)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 3142

## Categories

- [[Taxonomy/public_method|public_method]]
