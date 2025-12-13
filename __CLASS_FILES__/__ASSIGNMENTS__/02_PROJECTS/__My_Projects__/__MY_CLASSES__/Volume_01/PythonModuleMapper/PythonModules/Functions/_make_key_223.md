---
type: function
name: _make_key
module: functools
lineno: 473
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _make_key()

## Overview

Make a cache key from optionally typed positional and keyword arguments

The key is constructed in a way that is flat as possible rather than
as a nested structure that would take more memory.

If there is only a single argument and its data type is known to cache
its hash value, then that argument is returned without a wrapper.  This
saves space and improves lookup speed.

```python
def _make_key(args, kwds, typed, kwd_mark, fasttypes, tuple, type, len)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 473
