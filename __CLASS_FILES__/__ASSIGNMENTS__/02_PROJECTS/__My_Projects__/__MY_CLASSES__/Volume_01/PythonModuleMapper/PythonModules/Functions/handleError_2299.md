---
type: function
name: handleError
module: logging
lineno: 1060
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: handleError()

## Overview

Handle errors which occur during an emit() call.

This method should be called from handlers when an exception is
encountered during an emit() call. If raiseExceptions is false,
exceptions get silently ignored. This is what is mostly wanted
for a logging system - most users will not care about errors in
the logging system, they are more interested in application errors.
You could, however, replace this with a custom handler if you wish.
The record which was being processed is passed in to this method.

```python
def handleError(self, record)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Handler|Handler]]
**Type:** Method
**Line:** 1060

## Categories

- [[Taxonomy/public_method|public_method]]
