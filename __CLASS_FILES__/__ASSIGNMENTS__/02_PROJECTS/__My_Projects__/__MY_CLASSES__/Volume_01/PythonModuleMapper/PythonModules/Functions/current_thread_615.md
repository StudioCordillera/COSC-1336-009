---
type: function
name: current_thread
module: threading
lineno: 1429
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: current_thread()

## Overview

Return the current Thread object, corresponding to the caller's thread of control.

If the caller's thread of control was not created through the threading
module, a dummy thread object with limited functionality is returned.

```python
def current_thread()
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 1429
