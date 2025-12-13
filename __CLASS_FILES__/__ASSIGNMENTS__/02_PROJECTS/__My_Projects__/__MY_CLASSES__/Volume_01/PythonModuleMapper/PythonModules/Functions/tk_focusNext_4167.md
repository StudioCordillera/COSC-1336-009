---
type: function
name: tk_focusNext
module: tkinter
lineno: 829
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: tk_focusNext()

## Overview

Return the next widget in the focus order which follows
widget which has currently the focus.

The focus order first goes to the next child, then to
the children of the child recursively and then to the
next sibling which is higher in the stacking order.  A
widget is omitted if it has the takefocus resource set
to 0.

```python
def tk_focusNext(self)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 829

## Categories

- [[Taxonomy/public_method|public_method]]
