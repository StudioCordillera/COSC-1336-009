---
type: function
name: help_exec
module: pdb
lineno: 2147
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: help_exec()

## Overview

(!) statement

Execute the (one-line) statement in the context of the current
stack frame.  The exclamation point can be omitted unless the
first word of the statement resembles a debugger command, e.g.:
(Pdb) ! n=42
(Pdb)

To assign to a global variable you must always prefix the command with
a 'global' command, e.g.:
(Pdb) global list_options; list_options = ['-l']
(Pdb)

```python
def help_exec(self)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 2147

## Categories

- [[Taxonomy/public_method|public_method]]
