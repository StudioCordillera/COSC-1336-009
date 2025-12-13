---
type: function
name: clear
module: threading
lineno: 631
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: clear()

## Overview

Reset the internal flag to false.

Subsequently, threads calling wait() will block until set() is called to
set the internal flag to true again.

```python
def clear(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Event|Event]]
**Type:** Method
**Line:** 631
