---
type: function
name: _get_const_info
module: dis
lineno: 650
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_const_info()

## Overview

Helper to get optional details about const references

Returns the dereferenced constant and its repr if the value
can be calculated.
Otherwise returns the sentinel value dis.UNKNOWN for the value
and an empty string for its repr.

```python
def _get_const_info(op, arg, co_consts)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 650

## Categories

- [[Taxonomy/accessor|accessor]]
