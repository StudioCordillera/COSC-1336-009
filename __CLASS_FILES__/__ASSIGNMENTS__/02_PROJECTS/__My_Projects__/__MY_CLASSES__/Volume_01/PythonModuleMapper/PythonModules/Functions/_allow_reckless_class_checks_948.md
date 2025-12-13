---
type: function
name: _allow_reckless_class_checks
module: typing
lineno: 1984
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _allow_reckless_class_checks()

## Overview

Allow instance and class checks for special stdlib modules.

The abc and functools modules indiscriminately call isinstance() and
issubclass() on the whole MRO of a user class, which may contain protocols.

```python
def _allow_reckless_class_checks(depth)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 1984
