---
type: function
name: reveal_type
module: typing
lineno: 3608
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: reveal_type()

## Overview

Ask a static type checker to reveal the inferred type of an expression.

When a static type checker encounters a call to ``reveal_type()``,
it will emit the inferred type of the argument::

    x: int = 1
    reveal_type(x)

Running a static type checker (e.g., mypy) on this example
will produce output similar to 'Revealed type is "builtins.int"'.

At runtime, the function prints the runtime type of the
argument and returns the argument unchanged.

```python
def reveal_type() -> T
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 3608
