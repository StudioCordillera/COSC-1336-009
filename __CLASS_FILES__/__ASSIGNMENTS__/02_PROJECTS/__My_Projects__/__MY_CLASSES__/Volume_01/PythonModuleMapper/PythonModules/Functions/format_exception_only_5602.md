---
type: function
name: format_exception_only
module: traceback
lineno: 158
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: format_exception_only()

## Overview

Format the exception part of a traceback.

The return value is a list of strings, each ending in a newline.

The list contains the exception's message, which is
normally a single string; however, for :exc:`SyntaxError` exceptions, it
contains several lines that (when printed) display detailed information
about where the syntax error occurred. Following the message, the list
contains the exception's ``__notes__``.

When *show_group* is ``True``, and the exception is an instance of
:exc:`BaseExceptionGroup`, the nested exceptions are included as
well, recursively, with indentation relative to their nesting depth.

```python
def format_exception_only(value)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 158
