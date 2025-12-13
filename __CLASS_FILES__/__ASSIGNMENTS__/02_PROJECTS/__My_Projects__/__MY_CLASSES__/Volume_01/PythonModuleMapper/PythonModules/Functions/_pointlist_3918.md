---
type: function
name: _pointlist
module: turtle
lineno: 736
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _pointlist()

## Overview

returns list of coordinate-pairs of points of item
Example (for insiders):
>>> from turtle import *
>>> getscreen()._pointlist(getturtle().turtle._item)
[(0.0, 9.9999999999999982), (0.0, -9.9999999999999982),
(9.9999999999999982, 0.0)]
>>> 

```python
def _pointlist(self, item)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 736

## Categories

- [[Taxonomy/protected_method|protected_method]]
