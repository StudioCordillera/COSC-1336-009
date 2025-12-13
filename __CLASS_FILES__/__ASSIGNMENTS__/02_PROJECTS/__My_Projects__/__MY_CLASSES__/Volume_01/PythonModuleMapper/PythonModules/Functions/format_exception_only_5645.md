---
type: function
name: format_exception_only
module: traceback
lineno: 1218
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: format_exception_only()

## Overview

Format the exception part of the traceback.

The return value is a generator of strings, each ending in a newline.

Generator yields the exception message.
For :exc:`SyntaxError` exceptions, it
also yields (before the exception message)
several lines that (when printed)
display detailed information about where the syntax error occurred.
Following the message, generator also yields
all the exception's ``__notes__``.

When *show_group* is ``True``, and the exception is an instance of
:exc:`BaseExceptionGroup`, the nested exceptions are included as
well, recursively, with indentation relative to their nesting depth.

```python
def format_exception_only(self)
```

**Module:** [[Modules/traceback|traceback]]
**Class:** [[Classes/TracebackException|TracebackException]]
**Type:** Method
**Line:** 1218
