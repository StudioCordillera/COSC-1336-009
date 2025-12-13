---
type: function
name: make_dataclass
module: dataclasses
lineno: 1490
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: make_dataclass()

## Overview

Return a new dynamically created dataclass.

The dataclass name will be 'cls_name'.  'fields' is an iterable
of either (name), (name, type) or (name, type, Field) objects. If type is
omitted, use the string 'typing.Any'.  Field objects are created by
the equivalent of calling 'field(name, type [, Field-info])'.::

  C = make_dataclass('C', ['x', ('y', int), ('z', int, field(init=False))], bases=(Base,))

is equivalent to::

  @dataclass
  class C(Base):
      x: 'typing.Any'
      y: int
      z: int = field(init=False)

For the bases and namespace parameters, see the builtin type() function.

The parameters init, repr, eq, order, unsafe_hash, frozen, match_args, kw_only,
slots, and weakref_slot are passed to dataclass().

If module parameter is defined, the '__module__' attribute of the dataclass is
set to that value.

```python
def make_dataclass(cls_name, fields)
```

**Module:** [[Modules/dataclasses|dataclasses]]
**Type:** Module-level function
**Line:** 1490
