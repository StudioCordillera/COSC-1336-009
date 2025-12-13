---
type: function
name: do_ignore
module: pdb
lineno: 1337
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_ignore()

## Overview

ignore bpnumber [count]

Set the ignore count for the given breakpoint number.  If
count is omitted, the ignore count is set to 0.  A breakpoint
becomes active when the ignore count is zero.  When non-zero,
the count is decremented each time the breakpoint is reached
and the breakpoint is not disabled and any associated
condition evaluates to true.

```python
def do_ignore(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1337

## Categories

- [[Taxonomy/public_method|public_method]]
