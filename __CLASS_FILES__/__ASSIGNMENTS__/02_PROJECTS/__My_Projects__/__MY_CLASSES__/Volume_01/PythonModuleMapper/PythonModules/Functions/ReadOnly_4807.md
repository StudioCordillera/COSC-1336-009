---
type: function
name: ReadOnly
module: typing
lineno: 3371
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ReadOnly()

## Overview

A special typing construct to mark an item of a TypedDict as read-only.

For example::

    class Movie(TypedDict):
        title: ReadOnly[str]
        year: int

    def mutate_movie(m: Movie) -> None:
        m["year"] = 1992  # allowed
        m["title"] = "The Matrix"  # typechecker error

There is no runtime checking for this property.

```python
@_SpecialForm
def ReadOnly(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3371
