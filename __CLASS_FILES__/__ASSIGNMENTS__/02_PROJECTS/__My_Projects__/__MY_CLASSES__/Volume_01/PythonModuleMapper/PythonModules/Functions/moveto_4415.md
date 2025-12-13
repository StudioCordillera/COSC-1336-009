---
type: function
name: moveto
module: tkinter
lineno: 3122
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: moveto()

## Overview

Move the items given by TAGORID in the canvas coordinate
space so that the first coordinate pair of the bottommost
item with tag TAGORID is located at position (X,Y).
X and Y may be the empty string, in which case the
corresponding coordinate will be unchanged. All items matching
TAGORID remain in the same positions relative to each other.

```python
def moveto(self, tagOrId, x, y)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Canvas|Canvas]]
**Type:** Method
**Line:** 3122

## Categories

- [[Taxonomy/public_method|public_method]]
