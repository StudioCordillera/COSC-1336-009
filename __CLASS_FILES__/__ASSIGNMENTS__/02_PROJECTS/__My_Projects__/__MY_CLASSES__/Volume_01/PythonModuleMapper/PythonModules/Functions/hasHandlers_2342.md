---
type: function
name: hasHandlers
module: logging
lineno: 1706
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: hasHandlers()

## Overview

See if this logger has any handlers configured.

Loop through all handlers for this logger and its parents in the
logger hierarchy. Return True if a handler was found, else False.
Stop searching up the hierarchy whenever a logger with the "propagate"
attribute set to zero is found - that will be the last logger which
is checked for the existence of handlers.

```python
def hasHandlers(self)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Logger|Logger]]
**Type:** Method
**Line:** 1706

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
