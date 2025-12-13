---
type: function
name: ident
module: threading
lineno: 1113
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: ident()

## Overview

Thread identifier of this thread or None if it has not been started.

This is a nonzero integer. See the get_ident() function. Thread
identifiers may be recycled when a thread exits and another thread is
created. The identifier is available even after the thread has exited.

```python
@property
def ident(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Thread|Thread]]
**Type:** Method
**Line:** 1113

## Categories

- [[Taxonomy/public_method|public_method]]
