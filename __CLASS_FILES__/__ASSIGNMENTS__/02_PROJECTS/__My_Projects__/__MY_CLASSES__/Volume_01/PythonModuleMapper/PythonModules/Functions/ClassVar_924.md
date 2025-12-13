---
type: function
name: ClassVar
module: typing
lineno: 710
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ClassVar()

## Overview

Special type construct to mark class variables.

An annotation wrapped in ClassVar indicates that a given
attribute is intended to be used as a class variable and
should not be set on instances of that class.

Usage::

    class Starship:
        stats: ClassVar[dict[str, int]] = {} # class variable
        damage: int = 10                     # instance variable

ClassVar accepts only types and cannot be further subscribed.

Note that ClassVar is not a class itself, and should not
be used with isinstance() or issubclass().

```python
@_SpecialForm
def ClassVar(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 710
