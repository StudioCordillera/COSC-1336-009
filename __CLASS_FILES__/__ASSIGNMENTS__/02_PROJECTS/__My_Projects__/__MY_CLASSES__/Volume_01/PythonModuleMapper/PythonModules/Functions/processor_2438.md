---
type: function
name: processor
module: platform
lineno: 1112
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: processor()

## Overview

Returns the (true) processor name, e.g. 'amdk6'

An empty string is returned if the value cannot be
determined. Note that many platforms do not provide this
information or simply return the same value as for machine(),
e.g.  NetBSD does this.

```python
def processor()
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 1112
