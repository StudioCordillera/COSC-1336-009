---
type: function
name: tk_busy_hold
module: tkinter
lineno: 977
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: tk_busy_hold()

## Overview

Make this widget appear busy.

The specified widget and its descendants will be blocked from
user interactions.  Normally update() should be called
immediately afterward to insure that the hold operation is in
effect before the application starts its processing.

The only supported configuration option is:

    cursor: the cursor to be displayed when the widget is made
            busy.

```python
def tk_busy_hold(self)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 977

## Categories

- [[Taxonomy/public_method|public_method]]
