---
type: function
name: readprofile
module: tkinter
lineno: 2509
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: readprofile()

## Overview

Internal function. It reads .BASENAME.tcl and .CLASSNAME.tcl into
the Tcl Interpreter and calls exec on the contents of .BASENAME.py and
.CLASSNAME.py if such a file exists in the home directory.

```python
def readprofile(self, baseName, className)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Tk|Tk]]
**Type:** Method
**Line:** 2509

## Categories

- [[Taxonomy/public_method|public_method]]
