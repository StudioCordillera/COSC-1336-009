---
type: function
name: after_info
module: tkinter
lineno: 901
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: after_info()

## Overview

Return information about existing event handlers.

With no argument, return a tuple of the identifiers for all existing
event handlers created by the after and after_idle commands for this
interpreter.  If id is supplied, it specifies an existing handler; id
must have been the return value from some previous call to after or
after_idle and it must not have triggered yet or been canceled. If the
id doesn't exist, a TclError is raised.  Otherwise, the return value is
a tuple containing (script, type) where script is a reference to the
function to be called by the event handler and type is either 'idle'
or 'timer' to indicate what kind of event handler it is.

```python
def after_info(self, id)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 901

## Categories

- [[Taxonomy/public_method|public_method]]
