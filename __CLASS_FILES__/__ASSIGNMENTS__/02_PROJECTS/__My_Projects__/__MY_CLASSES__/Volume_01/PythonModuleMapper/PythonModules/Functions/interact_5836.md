---
type: function
name: interact
module: code
lineno: 348
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: interact()

## Overview

Closely emulate the interactive Python interpreter.

This is a backwards compatible interface to the InteractiveConsole
class.  When readfunc is not specified, it attempts to import the
readline module to enable GNU readline if it is available.

Arguments (all optional, all default to None):

banner -- passed to InteractiveConsole.interact()
readfunc -- if not None, replaces InteractiveConsole.raw_input()
local -- passed to InteractiveInterpreter.__init__()
exitmsg -- passed to InteractiveConsole.interact()
local_exit -- passed to InteractiveConsole.__init__()

```python
def interact(banner, readfunc, local, exitmsg, local_exit)
```

**Module:** [[Modules/code|code]]
**Type:** Module-level function
**Line:** 348
