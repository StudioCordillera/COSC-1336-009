---
type: function
name: format_exception
module: traceback
lineno: 142
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: format_exception()

## Overview

Format a stack trace and the exception information.

The arguments have the same meaning as the corresponding arguments
to print_exception().  The return value is a list of strings, each
ending in a newline and some containing internal newlines.  When
these lines are concatenated and printed, exactly the same text is
printed as does print_exception().

```python
def format_exception(value, tb, limit, chain)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 142
