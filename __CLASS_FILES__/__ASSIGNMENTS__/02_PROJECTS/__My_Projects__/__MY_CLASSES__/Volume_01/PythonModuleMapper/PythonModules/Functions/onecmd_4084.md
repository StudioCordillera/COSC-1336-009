---
type: function
name: onecmd
module: cmd
lineno: 200
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: onecmd()

## Overview

Interpret the argument as though it had been typed in response
to the prompt.

This may be overridden, but should not normally need to be;
see the precmd() and postcmd() methods for useful execution hooks.
The return value is a flag indicating whether interpretation of
commands by the interpreter should stop.

```python
def onecmd(self, line)
```

**Module:** [[Modules/cmd|cmd]]
**Class:** [[Classes/Cmd|Cmd]]
**Type:** Method
**Line:** 200

## Categories

- [[Taxonomy/public_method|public_method]]
