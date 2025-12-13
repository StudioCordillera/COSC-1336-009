---
type: function
name: asdict
module: dataclasses
lineno: 1338
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: asdict()

## Overview

Return the fields of a dataclass instance as a new dictionary mapping
field names to field values.

Example usage::

  @dataclass
  class C:
      x: int
      y: int

  c = C(1, 2)
  assert asdict(c) == {'x': 1, 'y': 2}

If given, 'dict_factory' will be used instead of built-in dict.
The function applies recursively to field values that are
dataclass instances. This will also look into built-in containers:
tuples, lists, and dicts. Other objects are copied with 'copy.deepcopy()'.

```python
def asdict(obj)
```

**Module:** [[Modules/dataclasses|dataclasses]]
**Type:** Module-level function
**Line:** 1338
