---
type: function
name: print_exception
module: traceback
lineno: 115
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: print_exception()

## Overview

Print exception up to 'limit' stack trace entries from 'tb' to 'file'.

This differs from print_tb() in the following ways: (1) if
traceback is not None, it prints a header "Traceback (most recent
call last):"; (2) it prints the exception type and value after the
stack trace; (3) if type is SyntaxError and value has the
appropriate format, it prints the line where the syntax error
occurred with a caret on the next line indicating the approximate
position of the error.

```python
def print_exception(value, tb, limit, file, chain)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 115
