---
type: function
name: _keep_alive
module: copy
lineno: 232
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _keep_alive()

## Overview

Keeps a reference to the object x in the memo.

Because we remember objects by their id, we have
to assure that possibly temporary objects are kept
alive by referencing them.
We store a reference at the id of the memo, which should
normally not be used unless someone tries to deepcopy
the memo itself...

```python
def _keep_alive(x, memo)
```

**Module:** [[Modules/copy|copy]]
**Type:** Module-level function
**Line:** 232
