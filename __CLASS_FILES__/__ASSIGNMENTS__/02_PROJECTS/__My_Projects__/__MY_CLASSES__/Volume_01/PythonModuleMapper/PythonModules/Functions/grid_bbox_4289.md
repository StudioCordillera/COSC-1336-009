---
type: function
name: grid_bbox
module: tkinter
lineno: 1896
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: grid_bbox()

## Overview

Return a tuple of integer coordinates for the bounding
box of this widget controlled by the geometry manager grid.

If COLUMN, ROW is given the bounding box applies from
the cell with row and column 0 to the specified
cell. If COL2 and ROW2 are given the bounding box
starts at that cell.

The returned integers specify the offset of the upper left
corner in the master widget and the width and height.

```python
def grid_bbox(self, column, row, col2, row2)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 1896

## Categories

- [[Taxonomy/public_method|public_method]]
