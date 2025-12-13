---
type: function
name: runcode
module: code
lineno: 79
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: runcode()

## Overview

Execute a code object.

When an exception occurs, self.showtraceback() is called to
display a traceback.  All exceptions are caught except
SystemExit, which is reraised.

A note about KeyboardInterrupt: this exception may occur
elsewhere in this code, and may not always be caught.  The
caller should be prepared to deal with it.

```python
def runcode(self, code)
```

**Module:** [[Modules/code|code]]
**Class:** [[Classes/InteractiveInterpreter|InteractiveInterpreter]]
**Type:** Method
**Line:** 79

## Categories

- [[Taxonomy/public_method|public_method]]
