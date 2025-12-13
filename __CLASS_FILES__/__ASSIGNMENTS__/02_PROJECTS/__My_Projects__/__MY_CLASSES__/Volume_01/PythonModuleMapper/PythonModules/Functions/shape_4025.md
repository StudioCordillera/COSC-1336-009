---
type: function
name: shape
module: turtle
lineno: 2808
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shape()

## Overview

Set turtle shape to shape with given name / return current shapename.

Optional argument:
name -- a string, which is a valid shapename

Set turtle shape to shape with given name or, if name is not given,
return name of current shape.
Shape with name must exist in the TurtleScreen's shape dictionary.
Initially there are the following polygon shapes:
'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
To learn about how to deal with shapes see Screen-method register_shape.

Example (for a Turtle instance named turtle):
>>> turtle.shape()
'arrow'
>>> turtle.shape("turtle")
>>> turtle.shape()
'turtle'

```python
def shape(self, name)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/RawTurtle|RawTurtle]]
**Type:** Method
**Line:** 2808

## Categories

- [[Taxonomy/public_method|public_method]]
