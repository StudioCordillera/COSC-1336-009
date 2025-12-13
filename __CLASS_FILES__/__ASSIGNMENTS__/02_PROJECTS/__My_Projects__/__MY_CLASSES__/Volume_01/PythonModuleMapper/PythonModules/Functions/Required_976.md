---
type: function
name: Required
module: typing
lineno: 3328
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Required()

## Overview

Special typing construct to mark a TypedDict key as required.

This is mainly useful for total=False TypedDicts.

For example::

    class Movie(TypedDict, total=False):
        title: Required[str]
        year: int

    m = Movie(
        title='The Matrix',  # typechecker error if key is omitted
        year=1999,
    )

There is no runtime checking that a required key is actually provided
when instantiating a related TypedDict.

```python
@_SpecialForm
def Required(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3328
