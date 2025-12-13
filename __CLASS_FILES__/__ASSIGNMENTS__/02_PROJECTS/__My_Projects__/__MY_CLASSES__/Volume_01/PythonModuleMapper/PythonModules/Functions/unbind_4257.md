---
type: function
name: unbind
module: tkinter
lineno: 1547
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: unbind()

## Overview

Unbind for this widget the event SEQUENCE.

If FUNCID is given, only unbind the function identified with FUNCID
and also delete the corresponding Tcl command.

Otherwise destroy the current binding for SEQUENCE, leaving SEQUENCE
unbound.

```python
def unbind(self, sequence, funcid)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 1547

## Categories

- [[Taxonomy/public_method|public_method]]
