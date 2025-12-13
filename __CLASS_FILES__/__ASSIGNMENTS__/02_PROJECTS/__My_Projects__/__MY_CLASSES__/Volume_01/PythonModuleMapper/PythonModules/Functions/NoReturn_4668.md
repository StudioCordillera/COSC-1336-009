---
type: function
name: NoReturn
module: typing
lineno: 617
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: NoReturn()

## Overview

Special type indicating functions that never return.

Example::

    from typing import NoReturn

    def stop() -> NoReturn:
        raise Exception('no way')

NoReturn can also be used as a bottom type, a type that
has no values. Starting in Python 3.11, the Never type should
be used for this concept instead. Type checkers should treat the two
equivalently.

```python
@_SpecialForm
def NoReturn(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 617
