---
type: function
name: select
module: selectors
lineno: 159
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

# Function: select()

## Overview

Perform the actual selection, until some monitored file objects are
ready or a timeout expires.

Parameters:
timeout -- if timeout > 0, this specifies the maximum wait time, in
           seconds
           if timeout <= 0, the select() call won't block, and will
           report the currently ready file objects
           if timeout is None, select() will block until a monitored
           file object becomes ready

Returns:
list of (key, events) for ready file objects
`events` is a bitwise mask of EVENT_READ|EVENT_WRITE

```python
@abstractmethod
def select(self, timeout)
```

**Module:** [[Modules/selectors|selectors]]
**Class:** [[Classes/BaseSelector|BaseSelector]]
**Type:** Method
**Line:** 159

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
