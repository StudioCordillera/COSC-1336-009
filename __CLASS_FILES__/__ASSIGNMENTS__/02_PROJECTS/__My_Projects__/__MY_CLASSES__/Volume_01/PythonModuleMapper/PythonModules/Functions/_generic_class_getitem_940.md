---
type: function
name: _generic_class_getitem
module: typing
lineno: 1208
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _generic_class_getitem()

## Overview

Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `args=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.

```python
@_tp_cache
def _generic_class_getitem(cls, args)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 1208
