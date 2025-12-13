---
type: function
name: retrlines
module: ftplib
lineno: 444
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: retrlines()

## Overview

Retrieve data in line mode.  A new port is created for you.

Args:
  cmd: A RETR, LIST, or NLST command.
  callback: An optional single parameter callable that is called
            for each line with the trailing CRLF stripped.
            [default: print_line()]

Returns:
  The response code.

```python
def retrlines(self, cmd, callback)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 444

## Categories

- [[Taxonomy/public_method|public_method]]
