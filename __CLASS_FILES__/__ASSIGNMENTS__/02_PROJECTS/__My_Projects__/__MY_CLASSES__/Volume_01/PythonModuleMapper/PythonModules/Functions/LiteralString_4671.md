---
type: function
name: LiteralString
module: typing
lineno: 683
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: LiteralString()

## Overview

Represents an arbitrary literal string.

Example::

    from typing import LiteralString

    def run_query(sql: LiteralString) -> None:
        ...

    def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
        run_query("SELECT * FROM students")  # OK
        run_query(literal_string)  # OK
        run_query("SELECT * FROM " + literal_string)  # OK
        run_query(arbitrary_string)  # type checker error
        run_query(  # type checker error
            f"SELECT * FROM students WHERE name = {arbitrary_string}"
        )

Only string literals and other LiteralStrings are compatible
with LiteralString. This provides a tool to help prevent
security issues such as SQL injection.

```python
@_SpecialForm
def LiteralString(self, parameters)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 683
