---
type: function
name: _register_atexit
module: threading
lineno: 1494
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _register_atexit()

## Overview

CPython internal: register *func* to be called before joining threads.

The registered *func* is called with its arguments just before all
non-daemon threads are joined in `_shutdown()`. It provides a similar
purpose to `atexit.register()`, but its functions are called prior to
threading shutdown instead of interpreter shutdown.

For similarity to atexit, the registered functions are called in reverse.

```python
def _register_atexit(func)
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 1494
