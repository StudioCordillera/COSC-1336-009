---
type: function
name: wm_iconbitmap
module: tkinter
lineno: 2257
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: wm_iconbitmap()

## Overview

Set bitmap for the iconified widget to BITMAP. Return
the bitmap if None is given.

Under Windows, the DEFAULT parameter can be used to set the icon
for the widget and any descendants that don't have an icon set
explicitly.  DEFAULT can be the relative path to a .ico file
(example: root.iconbitmap(default='myicon.ico') ).  See Tk
documentation for more information.

```python
def wm_iconbitmap(self, bitmap, default)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Wm|Wm]]
**Type:** Method
**Line:** 2257

## Categories

- [[Taxonomy/public_method|public_method]]
