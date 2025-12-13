---
type: function
name: format_stack_entry
module: bdb
lineno: 617
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: format_stack_entry()

## Overview

Return a string with information about a stack entry.

The stack entry frame_lineno is a (frame, lineno) tuple.  The
return string contains the canonical filename, the function name
or '<lambda>', the input arguments, the return value, and the
line of code (if it exists).

```python
def format_stack_entry(self, frame_lineno, lprefix)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 617

## Categories

- [[Taxonomy/public_method|public_method]]
