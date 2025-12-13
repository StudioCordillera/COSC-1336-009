---
type: function
name: _type_check_issubclass_arg_1
module: typing
lineno: 2034
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _type_check_issubclass_arg_1()

## Overview

Raise TypeError if `arg` is not an instance of `type`
in `issubclass(arg, <protocol>)`.

In most cases, this is verified by type.__subclasscheck__.
Checking it again unnecessarily would slow down issubclass() checks,
so, we don't perform this check unless we absolutely have to.

For various error paths, however,
we want to ensure that *this* error message is shown to the user
where relevant, rather than a typing.py-specific error message.

```python
def _type_check_issubclass_arg_1(arg)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2034
