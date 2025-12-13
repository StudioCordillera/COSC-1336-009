---
type: function
name: set_break
module: bdb
lineno: 434
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_break()

## Overview

Set a new breakpoint for filename:lineno.

If lineno doesn't exist for the filename, return an error message.
The filename should be in canonical form.

```python
def set_break(self, filename, lineno, temporary, cond, funcname)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 434

## Categories

- [[Taxonomy/mutator|mutator]]
