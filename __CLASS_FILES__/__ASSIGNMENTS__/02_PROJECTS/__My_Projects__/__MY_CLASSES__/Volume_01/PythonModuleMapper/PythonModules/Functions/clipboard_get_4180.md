---
type: function
name: clipboard_get
module: tkinter
lineno: 1000
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: clipboard_get()

## Overview

Retrieve data from the clipboard on window's display.

The window keyword defaults to the root window of the Tkinter
application.

The type keyword specifies the form in which the data is
to be returned and should be an atom name such as STRING
or FILE_NAME.  Type defaults to STRING, except on X11, where the default
is to try UTF8_STRING and fall back to STRING.

This command is equivalent to:

selection_get(CLIPBOARD)

```python
def clipboard_get(self)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 1000

## Categories

- [[Taxonomy/public_method|public_method]]
