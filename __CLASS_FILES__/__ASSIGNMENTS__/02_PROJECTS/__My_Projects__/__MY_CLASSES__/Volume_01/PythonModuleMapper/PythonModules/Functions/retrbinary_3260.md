---
type: function
name: retrbinary
module: ftplib
lineno: 421
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: retrbinary()

## Overview

Retrieve data in binary mode.  A new port is created for you.

Args:
  cmd: A RETR command.
  callback: A single parameter callable to be called on each
            block of data read.
  blocksize: The maximum number of bytes to read from the
             socket at one time.  [default: 8192]
  rest: Passed to transfercmd().  [default: None]

Returns:
  The response code.

```python
def retrbinary(self, cmd, callback, blocksize, rest)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 421

## Categories

- [[Taxonomy/public_method|public_method]]
