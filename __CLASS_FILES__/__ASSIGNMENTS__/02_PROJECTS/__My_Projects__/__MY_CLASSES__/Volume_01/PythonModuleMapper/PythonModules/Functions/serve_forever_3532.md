---
type: function
name: serve_forever
module: socketserver
lineno: 218
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: serve_forever()

## Overview

Handle one request at a time until shutdown.

Polls for shutdown every poll_interval seconds. Ignores
self.timeout. If you need to do periodic tasks, do them in
another thread.

```python
def serve_forever(self, poll_interval)
```

**Module:** [[Modules/socketserver|socketserver]]
**Class:** [[Classes/BaseServer|BaseServer]]
**Type:** Method
**Line:** 218

## Categories

- [[Taxonomy/public_method|public_method]]
