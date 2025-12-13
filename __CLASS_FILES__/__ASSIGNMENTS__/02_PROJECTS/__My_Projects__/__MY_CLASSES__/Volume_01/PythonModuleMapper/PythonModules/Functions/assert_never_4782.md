---
type: function
name: assert_never
module: typing
lineno: 2605
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: assert_never()

## Overview

Statically assert that a line of code is unreachable.

Example::

    def int_or_str(arg: int | str) -> None:
        match arg:
            case int():
                print("It's an int")
            case str():
                print("It's a str")
            case _:
                assert_never(arg)

If a type checker finds that a call to assert_never() is
reachable, it will emit an error.

At runtime, this throws an exception when called.

```python
def assert_never() -> Never
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2605
