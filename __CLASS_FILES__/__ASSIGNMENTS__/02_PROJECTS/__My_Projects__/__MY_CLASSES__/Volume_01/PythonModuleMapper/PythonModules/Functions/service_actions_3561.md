---
type: function
name: service_actions
module: socketserver
lineno: 608
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: service_actions()

## Overview

Collect the zombie child processes regularly in the ForkingMixIn.

service_actions is called in the BaseServer's serve_forever loop.

```python
def service_actions(self)
```

**Module:** [[Modules/socketserver|socketserver]]
**Class:** [[Classes/ForkingMixIn|ForkingMixIn]]
**Type:** Method
**Line:** 608
