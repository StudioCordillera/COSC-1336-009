---
type: function
name: Never
module: typing
lineno: 638
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Never()

## Overview

The bottom type, a type that has no members.

This can be used to define a function that should never be
called, or a function that never returns::

    from typing import Never

    def never_call_me(arg: Never) -> None:
        pass

    def int_or_str(arg: int | str) -> None:
        never_call_me(arg)  # type checker error
        match arg:
            case int():
                print("It's an int")
            case str():
                print("It's a str")
            case _:
                never_call_me(arg)  # OK, arg is of type Never

```python
@_SpecialForm
def Never(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 638
