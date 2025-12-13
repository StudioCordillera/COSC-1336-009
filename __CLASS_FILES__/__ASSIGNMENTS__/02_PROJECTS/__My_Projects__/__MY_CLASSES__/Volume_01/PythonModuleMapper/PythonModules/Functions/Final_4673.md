---
type: function
name: Final
module: typing
lineno: 732
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: Final()

## Overview

Special typing construct to indicate final names to type checkers.

A final name cannot be re-assigned or overridden in a subclass.

For example::

    MAX_SIZE: Final = 9000
    MAX_SIZE += 1  # Error reported by type checker

    class Connection:
        TIMEOUT: Final[int] = 10

    class FastConnector(Connection):
        TIMEOUT = 1  # Error reported by type checker

There is no runtime checking of these properties.

```python
@_SpecialForm
def Final(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 732
