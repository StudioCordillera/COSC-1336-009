---
type: function
name: readinto
module: socket
lineno: 706
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: readinto()

## Overview

Read up to len(b) bytes into the writable buffer *b* and return
the number of bytes read.  If the socket is non-blocking and no bytes
are available, None is returned.

If *b* is non-empty, a 0 return value indicates that the connection
was shutdown at the other end.

```python
def readinto(self, b)
```

**Module:** [[Modules/socket|socket]]
**Class:** [[Classes/SocketIO|SocketIO]]
**Type:** Method
**Line:** 706

## Categories

- [[Taxonomy/public_method|public_method]]
