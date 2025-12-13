---
type: function
name: _deprecated
module: warnings
lineno: 653
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _deprecated()

## Overview

Warn that *name* is deprecated or should be removed.

RuntimeError is raised if *remove* specifies a major/minor tuple older than
the current Python version or the same version but past the alpha.

The *message* argument is formatted with *name* and *remove* as a Python
version tuple (e.g. (3, 11)).

```python
def _deprecated(name, message)
```

**Module:** [[Modules/warnings|warnings]]
**Type:** Module-level function
**Line:** 653
