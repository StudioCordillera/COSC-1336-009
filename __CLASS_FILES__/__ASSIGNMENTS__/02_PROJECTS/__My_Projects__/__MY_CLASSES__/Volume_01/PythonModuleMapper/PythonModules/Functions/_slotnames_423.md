---
type: function
name: _slotnames
module: copyreg
lineno: 107
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _slotnames()

## Overview

Return a list of slot names for a given class.

This needs to find slots defined by the class and its bases, so we
can't simply return the __slots__ attribute.  We must walk down
the Method Resolution Order and concatenate the __slots__ of each
class found there.  (This assumes classes don't modify their
__slots__ attribute to misrepresent their slots after the class is
defined.)

```python
def _slotnames(cls)
```

**Module:** [[Modules/copyreg|copyreg]]
**Type:** Module-level function
**Line:** 107
