---
type: function
name: create_server
module: socket
lineno: 889
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: create_server()

## Overview

Convenience function which creates a SOCK_STREAM type socket
bound to *address* (a 2-tuple (host, port)) and return the socket
object.

*family* should be either AF_INET or AF_INET6.
*backlog* is the queue size passed to socket.listen().
*reuse_port* dictates whether to use the SO_REUSEPORT socket option.
*dualstack_ipv6*: if true and the platform supports it, it will
create an AF_INET6 socket able to accept both IPv4 or IPv6
connections. When false it will explicitly disable this option on
platforms that enable it by default (e.g. Linux).

>>> with create_server(('', 8000)) as server:
...     while True:
...         conn, addr = server.accept()
...         # handle new connection

```python
def create_server(address)
```

**Module:** [[Modules/socket|socket]]
**Type:** Module-level function
**Line:** 889
