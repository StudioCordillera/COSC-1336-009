---
type: function
name: start
module: threading
lineno: 955
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: start()

## Overview

Start the thread's activity.

It must be called at most once per thread object. It arranges for the
object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the
same thread object.

```python
def start(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Thread|Thread]]
**Type:** Method
**Line:** 955

## Categories

- [[Taxonomy/public_method|public_method]]
