---
type: function
name: close
module: logging
lineno: 1045
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: close()

## Overview

Tidy up any resources used by the handler.

This version removes the handler from an internal map of handlers,
_handlers, which is used for handler lookup by name. Subclasses
should ensure that this gets called from overridden close()
methods.

```python
def close(self)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Handler|Handler]]
**Type:** Method
**Line:** 1045

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
