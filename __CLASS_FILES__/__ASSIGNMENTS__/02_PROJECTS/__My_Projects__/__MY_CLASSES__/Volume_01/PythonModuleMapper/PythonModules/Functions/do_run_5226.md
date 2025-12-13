---
type: function
name: do_run
module: pdb
lineno: 1597
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_run()

## Overview

run [args...]

Restart the debugged python program. If a string is supplied
it is split with "shlex", and the result is used as the new
sys.argv.  History, breakpoints, actions and debugger options
are preserved.  "restart" is an alias for "run".

```python
def do_run(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1597

## Categories

- [[Taxonomy/public_method|public_method]]
