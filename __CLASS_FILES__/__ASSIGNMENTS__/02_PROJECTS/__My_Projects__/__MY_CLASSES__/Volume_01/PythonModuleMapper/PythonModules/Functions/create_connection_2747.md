---
type: function
name: create_connection
module: socket
lineno: 822
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: create_connection()

## Overview

Connect to *address* and return the socket object.

Convenience function.  Connect to *address* (a 2-tuple ``(host,
port)``) and return the socket object.  Passing the optional
*timeout* parameter will set the timeout on the socket instance
before attempting to connect.  If no *timeout* is supplied, the
global default timeout setting returned by :func:`getdefaulttimeout`
is used.  If *source_address* is set it must be a tuple of (host, port)
for the socket to bind as a source address before making the connection.
A host of '' or port 0 tells the OS to use the default. When a connection
cannot be created, raises the last error if *all_errors* is False,
and an ExceptionGroup of all errors if *all_errors* is True.

```python
def create_connection(address, timeout, source_address)
```

**Module:** [[Modules/socket|socket]]
**Type:** Module-level function
**Line:** 822
