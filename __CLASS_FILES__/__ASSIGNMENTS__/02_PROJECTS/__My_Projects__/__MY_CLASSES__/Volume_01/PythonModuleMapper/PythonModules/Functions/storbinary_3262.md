---
type: function
name: storbinary
module: ftplib
lineno: 479
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: storbinary()

## Overview

Store a file in binary mode.  A new port is created for you.

Args:
  cmd: A STOR command.
  fp: A file-like object with a read(num_bytes) method.
  blocksize: The maximum data size to read from fp and send over
             the connection at once.  [default: 8192]
  callback: An optional single parameter callable that is called on
            each block of data after it is sent.  [default: None]
  rest: Passed to transfercmd().  [default: None]

Returns:
  The response code.

```python
def storbinary(self, cmd, fp, blocksize, callback, rest)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 479

## Categories

- [[Taxonomy/public_method|public_method]]
