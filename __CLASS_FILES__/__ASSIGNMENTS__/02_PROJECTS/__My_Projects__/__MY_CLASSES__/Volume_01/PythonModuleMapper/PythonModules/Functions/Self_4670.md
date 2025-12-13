---
type: function
name: Self
module: typing
lineno: 663
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Self()

## Overview

Used to spell the type of "self" in classes.

Example::

    from typing import Self

    class Foo:
        def return_self(self) -> Self:
            ...
            return self

This is especially useful for:
    - classmethods that are used as alternative constructors
    - annotating an `__enter__` method which returns self

```python
@_SpecialForm
def Self(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 663
