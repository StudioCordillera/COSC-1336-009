---
type: function
name: register
module: selectors
lineno: 100
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
  - public_method
  - public_method
  - public_method
---

# Function: register()

## Overview

Register a file object.

Parameters:
fileobj -- file object or file descriptor
events  -- events to monitor (bitwise mask of EVENT_READ|EVENT_WRITE)
data    -- attached data

Returns:
SelectorKey instance

Raises:
ValueError if events is invalid
KeyError if fileobj is already registered
OSError if fileobj is closed or otherwise is unacceptable to
        the underlying system call (if a system call is made)

Note:
OSError may or may not be raised

```python
@abstractmethod
def register(self, fileobj, events, data)
```

**Module:** [[Modules/selectors|selectors]]
**Class:** [[Classes/BaseSelector|BaseSelector]]
**Type:** Method
**Line:** 100

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
