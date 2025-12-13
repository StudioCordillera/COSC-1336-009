---
type: function
name: recv_fds
module: socket
lineno: 566
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: recv_fds()

## Overview

recv_fds(sock, bufsize, maxfds[, flags]) -> (data, list of file
descriptors, msg_flags, address)

Receive up to maxfds file descriptors returning the message
data and a list containing the descriptors.

```python
def recv_fds(sock, bufsize, maxfds, flags)
```

**Module:** [[Modules/socket|socket]]
**Type:** Module-level function
**Line:** 566
