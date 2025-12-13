---
type: function
name: sash_coord
module: tkinter
lineno: 4839
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: sash_coord()

## Overview

Return the current x and y pair for the sash given by index.

Index must be an integer between 0 and 1 less than the
number of panes in the panedwindow. The coordinates given are
those of the top left corner of the region containing the sash.
pathName sash dragto index x y This command computes the
difference between the given coordinates and the coordinates
given to the last sash coord command for the given sash. It then
moves that sash the computed difference. The return value is the
empty string.

```python
def sash_coord(self, index)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/PanedWindow|PanedWindow]]
**Type:** Method
**Line:** 4839

## Categories

- [[Taxonomy/public_method|public_method]]
