---
type: function
name: storlines
module: ftplib
lineno: 505
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: storlines()

## Overview

Store a file in line mode.  A new port is created for you.

Args:
  cmd: A STOR command.
  fp: A file-like object with a readline() method.
  callback: An optional single parameter callable that is called on
            each line after it is sent.  [default: None]

Returns:
  The response code.

```python
def storlines(self, cmd, fp, callback)
```

**Module:** [[Modules/ftplib|ftplib]]
**Class:** [[Classes/FTP|FTP]]
**Type:** Method
**Line:** 505

## Categories

- [[Taxonomy/public_method|public_method]]
