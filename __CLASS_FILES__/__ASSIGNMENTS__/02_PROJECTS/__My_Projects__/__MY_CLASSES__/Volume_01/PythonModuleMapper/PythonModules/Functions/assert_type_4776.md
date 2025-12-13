---
type: function
name: assert_type
module: typing
lineno: 2382
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: assert_type()

## Overview

Ask a static type checker to confirm that the value is of the given type.

At runtime this does nothing: it returns the first argument unchanged with no
checks or side effects, no matter the actual type of the argument.

When a static type checker encounters a call to assert_type(), it
emits an error if the value is not of the specified type::

    def greet(name: str) -> None:
        assert_type(name, str)  # OK
        assert_type(name, int)  # type checker error

```python
def assert_type()
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2382
