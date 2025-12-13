---
type: function
name: get_terminal_size
module: shutil
lineno: 1439
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_terminal_size()

## Overview

Get the size of the terminal window.

For each of the two dimensions, the environment variable, COLUMNS
and LINES respectively, is checked. If the variable is defined and
the value is a positive integer, it is used.

When COLUMNS or LINES is not defined, which is the common case,
the terminal connected to sys.__stdout__ is queried
by invoking os.get_terminal_size.

If the terminal size cannot be successfully queried, either because
the system doesn't support querying, or because we are not
connected to a terminal, the value given in fallback parameter
is used. Fallback defaults to (80, 24) which is the default
size used by many terminal emulators.

The value returned is a named tuple of type os.terminal_size.

```python
def get_terminal_size(fallback)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 1439

## Categories

- [[Taxonomy/accessor|accessor]]
