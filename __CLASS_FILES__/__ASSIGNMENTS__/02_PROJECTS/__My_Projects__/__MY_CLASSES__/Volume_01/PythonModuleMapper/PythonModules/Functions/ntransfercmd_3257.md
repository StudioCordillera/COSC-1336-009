---
type: function
name: ntransfercmd
module: ftplib
lineno: 336
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: ntransfercmd()

## Overview

Initiate a transfer over the data connection.

If the transfer is active, send a port command and the
transfer command, and accept the connection.  If the server is
passive, send a pasv command, connect to it, and start the
transfer command.  Either way, return the socket for the
connection and the expected size of the transfer.  The
expected size may be None if it could not be determined.

Optional `rest' argument can be a string that is sent as the
argument to a REST command.  This is essentially a server
marker used to tell the server to skip over any data up to the
given marker.

```python
def ntransfercmd(self, cmd, rest)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 336

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
