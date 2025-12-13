---
type: function
name: do_condition
module: pdb
lineno: 1306
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_condition()

## Overview

condition bpnumber [condition]

Set a new condition for the breakpoint, an expression which
must evaluate to true before the breakpoint is honored.  If
condition is absent, any existing condition is removed; i.e.,
the breakpoint is made unconditional.

```python
def do_condition(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1306

## Categories

- [[Taxonomy/public_method|public_method]]
