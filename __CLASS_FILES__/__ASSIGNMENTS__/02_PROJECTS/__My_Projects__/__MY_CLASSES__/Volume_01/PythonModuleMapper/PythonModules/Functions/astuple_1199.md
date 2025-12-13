---
type: function
name: astuple
module: dataclasses
lineno: 1430
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: astuple()

## Overview

Return the fields of a dataclass instance as a new tuple of field values.

Example usage::

  @dataclass
  class C:
      x: int
      y: int

  c = C(1, 2)
  assert astuple(c) == (1, 2)

If given, 'tuple_factory' will be used instead of built-in tuple.
The function applies recursively to field values that are
dataclass instances. This will also look into built-in containers:
tuples, lists, and dicts. Other objects are copied with 'copy.deepcopy()'.

```python
def astuple(obj)
```

**Module:** [[Modules/dataclasses|dataclasses]]
**Type:** Module-level function
**Line:** 1430
