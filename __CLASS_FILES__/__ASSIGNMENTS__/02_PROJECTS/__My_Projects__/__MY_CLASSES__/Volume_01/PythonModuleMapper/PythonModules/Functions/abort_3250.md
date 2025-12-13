---
type: function
name: abort
module: ftplib
lineno: 264
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: abort()

## Overview

Abort a file transfer.  Uses out-of-band data.
This does not follow the procedure from the RFC to send Telnet
IP and Synch; that doesn't seem to work with the servers I've
tried.  Instead, just send the ABOR command as OOB data.

```python
def abort(self)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 264

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
