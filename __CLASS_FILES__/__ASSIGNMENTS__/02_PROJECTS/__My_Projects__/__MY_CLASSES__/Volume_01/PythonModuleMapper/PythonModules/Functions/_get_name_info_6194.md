---
type: function
name: _get_name_info
module: dis
lineno: 662
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_name_info()

## Overview

Helper to get optional details about named references

Returns the dereferenced name as both value and repr if the name
list is defined.
Otherwise returns the sentinel value dis.UNKNOWN for the value
and an empty string for its repr.

```python
def _get_name_info(name_index, get_name)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 662

## Categories

- [[Taxonomy/accessor|accessor]]
