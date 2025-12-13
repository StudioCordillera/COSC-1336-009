---
type: function
name: detach
module: socket
lineno: 507
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: detach()

## Overview

detach() -> file descriptor

Close the socket object without closing the underlying file descriptor.
The object cannot be used after this call, but the file descriptor
can be reused for other purposes.  The file descriptor is returned.

```python
def detach(self)
```

**Module:** [[Modules/socket|socket]]
**Class:** [[Classes/socket|socket]]
**Type:** Method
**Line:** 507

## Categories

- [[Taxonomy/public_method|public_method]]
