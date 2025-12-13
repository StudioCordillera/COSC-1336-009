---
type: function
name: __init__
module: difflib
lineno: 810
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: __init__()

## Overview

Construct a text differencer, with optional filters.

The two optional keyword parameters are for filter functions:

- `linejunk`: A function that should accept a single string argument,
  and return true iff the string is junk. The module-level function
  `IS_LINE_JUNK` may be used to filter out lines without visible
  characters, except for at most one splat ('#').  It is recommended
  to leave linejunk None; the underlying SequenceMatcher class has
  an adaptive notion of "noise" lines that's better than any static
  definition the author has ever been able to craft.

- `charjunk`: A function that should accept a string of length 1. The
  module-level function `IS_CHARACTER_JUNK` may be used to filter out
  whitespace characters (a blank or tab; **note**: bad idea to include
  newline in this!).  Use of IS_CHARACTER_JUNK is recommended.

```python
def __init__(self, linejunk, charjunk)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/Differ|Differ]]
**Type:** Method
**Line:** 810
