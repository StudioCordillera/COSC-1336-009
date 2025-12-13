---
type: function
name: getaddrinfo
module: socket
lineno: 960
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getaddrinfo()

## Overview

Resolve host and port into list of address info entries.

Translate the host/port argument into a sequence of 5-tuples that contain
all the necessary arguments for creating a socket connected to that service.
host is a domain name, a string representation of an IPv4/v6 address or
None. port is a string service name such as 'http', a numeric port number or
None. By passing None as the value of host and port, you can pass NULL to
the underlying C API.

The family, type and proto arguments can be optionally specified in order to
narrow the list of addresses returned. Passing zero as a value for each of
these arguments selects the full range of results.

```python
def getaddrinfo(host, port, family, type, proto, flags)
```

**Module:** [[Modules/socket|socket]]
**Type:** Module-level function
**Line:** 960
