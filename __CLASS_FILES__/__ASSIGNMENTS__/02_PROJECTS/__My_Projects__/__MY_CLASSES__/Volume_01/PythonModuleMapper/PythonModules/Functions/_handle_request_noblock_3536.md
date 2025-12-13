---
type: function
name: _handle_request_noblock
module: socketserver
lineno: 305
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _handle_request_noblock()

## Overview

Handle one request, without blocking.

I assume that selector.select() has returned that the socket is
readable before this function was called, so there should be no risk of
blocking in get_request().

```python
def _handle_request_noblock(self)
```

**Module:** [[Modules/socketserver|socketserver]]
**Class:** [[Classes/BaseServer|BaseServer]]
**Type:** Method
**Line:** 305

## Categories

- [[Taxonomy/protected_method|protected_method]]
