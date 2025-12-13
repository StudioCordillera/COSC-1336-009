---
type: function
name: IS_LINE_JUNK
module: difflib
lineno: 1045
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: IS_LINE_JUNK()

## Overview

Return True for ignorable line: iff `line` is blank or contains a single '#'.

Examples:

>>> IS_LINE_JUNK('\n')
True
>>> IS_LINE_JUNK('  #   \n')
True
>>> IS_LINE_JUNK('hello\n')
False

```python
def IS_LINE_JUNK(line, pat)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1045
