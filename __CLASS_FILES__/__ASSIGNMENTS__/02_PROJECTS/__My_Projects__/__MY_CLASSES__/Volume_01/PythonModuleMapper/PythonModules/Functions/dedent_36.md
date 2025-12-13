---
type: function
name: dedent
module: textwrap
lineno: 419
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: dedent()

## Overview

Remove any common leading whitespace from every line in `text`.

This can be used to make triple-quoted strings line up with the left
edge of the display, while still presenting them in the source code
in indented form.

Note that tabs and spaces are both treated as whitespace, but they
are not equal: the lines "  hello" and "\thello" are
considered to have no common leading whitespace.

Entirely blank lines are normalized to a newline character.

```python
def dedent(text)
```

**Module:** [[Modules/textwrap|textwrap]]
**Type:** Module-level function
**Line:** 419
