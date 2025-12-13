---
type: function
name: indent
module: textwrap
lineno: 470
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: indent()

## Overview

Adds 'prefix' to the beginning of selected lines in 'text'.

If 'predicate' is provided, 'prefix' will only be added to the lines
where 'predicate(line)' is True. If 'predicate' is not provided,
it will default to adding 'prefix' to all non-empty lines that do not
consist solely of whitespace characters.

```python
def indent(text, prefix, predicate)
```

**Module:** [[Modules/textwrap|textwrap]]
**Type:** Module-level function
**Line:** 470
