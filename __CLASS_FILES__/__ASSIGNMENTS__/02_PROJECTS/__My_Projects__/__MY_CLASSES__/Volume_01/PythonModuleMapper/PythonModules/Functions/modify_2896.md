---
type: function
name: modify
module: selectors
lineno: 141
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
  - public_method
---

# Function: modify()

## Overview

Change a registered file object monitored events or attached data.

Parameters:
fileobj -- file object or file descriptor
events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
data    -- attached data

Returns:
SelectorKey instance

Raises:
Anything that unregister() or register() raises

```python
def modify(self, fileobj, events, data)
```

**Module:** [[Modules/selectors|selectors]]
**Class:** [[Classes/BaseSelector|BaseSelector]]
**Type:** Method
**Line:** 141

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
