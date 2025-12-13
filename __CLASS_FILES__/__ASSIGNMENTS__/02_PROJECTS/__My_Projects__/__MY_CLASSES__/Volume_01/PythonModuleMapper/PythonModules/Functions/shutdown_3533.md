---
type: function
name: shutdown
module: socketserver
lineno: 247
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shutdown()

## Overview

Stops the serve_forever loop.

Blocks until the loop has finished. This must be called while
serve_forever() is running in another thread, or it will
deadlock.

```python
def shutdown(self)
```

**Module:** [[Modules/socketserver|socketserver]]
**Class:** [[Classes/BaseServer|BaseServer]]
**Type:** Method
**Line:** 247

## Categories

- [[Taxonomy/public_method|public_method]]
