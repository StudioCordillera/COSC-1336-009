---
type: function
name: NotRequired
module: typing
lineno: 3352
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: NotRequired()

## Overview

Special typing construct to mark a TypedDict key as potentially missing.

For example::

    class Movie(TypedDict):
        title: str
        year: NotRequired[int]

    m = Movie(
        title='The Matrix',  # typechecker error if key is omitted
        year=1999,
    )

```python
@_SpecialForm
def NotRequired(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3352
