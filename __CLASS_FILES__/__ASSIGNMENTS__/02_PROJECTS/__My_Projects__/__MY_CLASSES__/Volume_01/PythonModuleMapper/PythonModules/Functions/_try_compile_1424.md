---
type: function
name: _try_compile
module: dis
lineno: 65
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _try_compile()

## Overview

Attempts to compile the given source, first as an expression and
then as a statement if the first approach fails.

Utility function to accept strings in functions that otherwise
expect code objects

```python
def _try_compile(source, name)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 65
