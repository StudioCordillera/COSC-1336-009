---
type: function
name: addcomponent
module: turtle
lineno: 884
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: addcomponent()

## Overview

Add component to a shape of type compound.

Arguments: poly is a polygon, i. e. a tuple of number pairs.
fill is the fillcolor of the component,
outline is the outline color of the component.

call (for a Shapeobject namend s):
--   s.addcomponent(((0,0), (10,10), (-10,10)), "red", "blue")

Example:
>>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s = Shape("compound")
>>> s.addcomponent(poly, "red", "blue")
>>> # .. add more components and then use register_shape()

```python
def addcomponent(self, poly, fill, outline)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/Shape|Shape]]
**Type:** Method
**Line:** 884

## Categories

- [[Taxonomy/public_method|public_method]]
