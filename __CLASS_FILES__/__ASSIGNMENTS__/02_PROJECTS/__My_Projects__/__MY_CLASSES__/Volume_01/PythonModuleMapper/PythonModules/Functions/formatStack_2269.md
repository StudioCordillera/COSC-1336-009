---
type: function
name: formatStack
module: logging
lineno: 686
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: formatStack()

## Overview

This method is provided as an extension point for specialized
formatting of stack information.

The input data is a string as returned from a call to
:func:`traceback.print_stack`, but with the last trailing newline
removed.

The base implementation just returns the value passed in.

```python
def formatStack(self, stack_info)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Formatter|Formatter]]
**Type:** Method
**Line:** 686

## Categories

- [[Taxonomy/public_method|public_method]]
