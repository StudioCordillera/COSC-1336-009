---
type: function
name: do_jump
module: pdb
lineno: 1653
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_jump()

## Overview

j(ump) lineno

Set the next line that will be executed.  Only available in
the bottom-most frame.  This lets you jump back and execute
code again, or jump forward to skip code that you don't want
to run.

It should be noted that not all jumps are allowed -- for
instance it is not possible to jump into the middle of a
for loop or out of a finally clause.

```python
def do_jump(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1653

## Categories

- [[Taxonomy/public_method|public_method]]
