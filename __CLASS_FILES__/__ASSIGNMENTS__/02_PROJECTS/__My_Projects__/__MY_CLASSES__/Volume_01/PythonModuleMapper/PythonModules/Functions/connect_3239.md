---
type: function
name: connect
module: ftplib
lineno: 139
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: connect()

## Overview

Connect to host.  Arguments are:
- host: hostname to connect to (string, default previous host)
- port: port to connect to (integer, default previous port)
- timeout: the timeout to set against the ftp socket(s)
- source_address: a 2-tuple (host, port) for the socket to bind
  to as its source address before connecting.

```python
def connect(self, host, port, timeout, source_address)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 139

## Categories

- [[Taxonomy/public_method|public_method]]
