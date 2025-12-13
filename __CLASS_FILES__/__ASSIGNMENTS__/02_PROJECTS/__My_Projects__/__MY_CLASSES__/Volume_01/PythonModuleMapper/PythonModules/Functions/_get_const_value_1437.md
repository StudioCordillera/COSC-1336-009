---
type: function
name: _get_const_value
module: dis
lineno: 636
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_const_value()

## Overview

Helper to get the value of the const in a hasconst op.

Returns the dereferenced constant if this is possible.
Otherwise (if it is a LOAD_CONST and co_consts is not
provided) returns the dis.UNKNOWN sentinel.

```python
def _get_const_value(op, arg, co_consts)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 636

## Categories

- [[Taxonomy/accessor|accessor]]
