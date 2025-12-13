---
type: function
name: write
module: socket
lineno: 728
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write()

## Overview

Write the given bytes or bytearray object *b* to the socket
and return the number of bytes written.  This can be less than
len(b) if not all data could be written.  If the socket is
non-blocking and no bytes could be written None is returned.

```python
def write(self, b)
```

**Module:** [[Modules/socket|socket]]
**Class:** [[Classes/SocketIO|SocketIO]]
**Type:** Method
**Line:** 728

## Categories

- [[Taxonomy/public_method|public_method]]
