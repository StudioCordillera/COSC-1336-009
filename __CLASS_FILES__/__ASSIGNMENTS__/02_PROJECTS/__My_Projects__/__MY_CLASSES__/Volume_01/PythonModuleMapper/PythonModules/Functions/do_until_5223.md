---
type: function
name: do_until
module: pdb
lineno: 1545
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_until()

## Overview

unt(il) [lineno]

Without argument, continue execution until the line with a
number greater than the current one is reached.  With a line
number, continue execution until a line with a number greater
or equal to that is reached.  In both cases, also stop when
the current frame returns.

```python
def do_until(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1545

## Categories

- [[Taxonomy/public_method|public_method]]
