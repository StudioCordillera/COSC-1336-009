---
type: function
name: selection_adjust
module: tkinter
lineno: 4689
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: selection_adjust()

## Overview

Locate the end of the selection nearest to the character
given by index,

Then adjust that end of the selection to be at index
(i.e including but not going beyond index). The other
end of the selection is made the anchor point for future
select to commands. If the selection isn't currently in
the spinbox, then a new selection is created to include
the characters between index and the most recent selection
anchor point, inclusive.

```python
def selection_adjust(self, index)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Spinbox|Spinbox]]
**Type:** Method
**Line:** 4689
