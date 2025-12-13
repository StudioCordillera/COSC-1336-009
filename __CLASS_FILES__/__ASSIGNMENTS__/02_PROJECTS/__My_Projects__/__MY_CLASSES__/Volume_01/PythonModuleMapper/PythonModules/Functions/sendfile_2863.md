---
type: function
name: sendfile
module: ssl
lineno: 1268
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: sendfile()

## Overview

Send a file, possibly by using os.sendfile() if this is a
clear-text socket.  Return the total number of bytes sent.

```python
def sendfile(self, file, offset, count)
```

**Module:** [[Modules/ssl|ssl]]
**Class:** [[Classes/SSLSocket|SSLSocket]]
**Type:** Method
**Line:** 1268
