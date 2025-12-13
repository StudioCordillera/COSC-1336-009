---
type: function
name: scan_dragto
module: tkinter
lineno: 4672
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: scan_dragto()

## Overview

Compute the difference between the given x argument
and the x argument to the last scan mark command

It then adjusts the view left or right by 10 times the
difference in x-coordinates. This command is typically
associated with mouse motion events in the widget, to
produce the effect of dragging the spinbox at high speed
through the window. The return value is an empty string.

```python
def scan_dragto(self, x)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Spinbox|Spinbox]]
**Type:** Method
**Line:** 4672
