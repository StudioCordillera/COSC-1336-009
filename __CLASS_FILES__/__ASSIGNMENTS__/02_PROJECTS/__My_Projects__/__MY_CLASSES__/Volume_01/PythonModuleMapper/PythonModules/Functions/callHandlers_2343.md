---
type: function
name: callHandlers
module: logging
lineno: 1728
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: callHandlers()

## Overview

Pass a record to all relevant handlers.

Loop through all handlers for this logger and its parents in the
logger hierarchy. If no handler was found, output a one-off error
message to sys.stderr. Stop searching up the hierarchy whenever a
logger with the "propagate" attribute set to zero is found - that
will be the last logger whose handlers are called.

```python
def callHandlers(self, record)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Logger|Logger]]
**Type:** Method
**Line:** 1728

## Categories

- [[Taxonomy/public_method|public_method]]
