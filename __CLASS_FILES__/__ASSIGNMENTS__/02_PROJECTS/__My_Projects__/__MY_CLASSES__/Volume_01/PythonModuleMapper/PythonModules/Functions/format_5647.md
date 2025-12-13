---
type: function
name: format
module: traceback
lineno: 1363
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: format()

## Overview

Format the exception.

If chain is not *True*, *__cause__* and *__context__* will not be formatted.

The return value is a generator of strings, each ending in a newline and
some containing internal newlines. `print_exception` is a wrapper around
this method which just prints the lines to a file.

The message indicating which exception occurred is always the last
string in the output.

```python
def format(self)
```

**Module:** [[Modules/traceback|traceback]]
**Class:** [[Classes/TracebackException|TracebackException]]
**Type:** Method
**Line:** 1363
