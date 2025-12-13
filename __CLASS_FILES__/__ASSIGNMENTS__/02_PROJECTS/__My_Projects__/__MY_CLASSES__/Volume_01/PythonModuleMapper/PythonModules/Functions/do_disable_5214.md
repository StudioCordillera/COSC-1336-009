---
type: function
name: do_disable
module: pdb
lineno: 1285
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_disable()

## Overview

disable bpnumber [bpnumber ...]

Disables the breakpoints given as a space separated list of
breakpoint numbers.  Disabling a breakpoint means it cannot
cause the program to stop execution, but unlike clearing a
breakpoint, it remains in the list of breakpoints and can be
(re-)enabled.

```python
def do_disable(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1285

## Categories

- [[Taxonomy/public_method|public_method]]
