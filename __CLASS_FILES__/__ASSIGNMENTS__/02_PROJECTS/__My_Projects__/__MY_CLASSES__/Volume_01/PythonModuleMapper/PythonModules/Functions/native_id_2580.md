---
type: function
name: native_id
module: threading
lineno: 1126
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: native_id()

## Overview

Native integral thread ID of this thread, or None if it has not been started.

This is a non-negative integer. See the get_native_id() function.
This represents the Thread ID as reported by the kernel.

```python
@property
def native_id(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Thread|Thread]]
**Type:** Method
**Line:** 1126

## Categories

- [[Taxonomy/public_method|public_method]]
