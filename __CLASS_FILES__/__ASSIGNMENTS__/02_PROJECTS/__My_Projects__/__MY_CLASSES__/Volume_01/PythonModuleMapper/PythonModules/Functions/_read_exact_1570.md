---
type: function
name: _read_exact
module: gzip
lineno: 449
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _read_exact()

## Overview

Read exactly *n* bytes from `fp`

This method is required because fp may be unbuffered,
i.e. return short reads.

```python
def _read_exact(fp, n)
```

**Module:** [[Modules/gzip|gzip]]
**Type:** Module-level function
**Line:** 449
