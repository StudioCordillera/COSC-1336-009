---
type: function
name: IS_CHARACTER_JUNK
module: difflib
lineno: 1061
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: IS_CHARACTER_JUNK()

## Overview

Return True for ignorable character: iff `ch` is a space or tab.

Examples:

>>> IS_CHARACTER_JUNK(' ')
True
>>> IS_CHARACTER_JUNK('\t')
True
>>> IS_CHARACTER_JUNK('\n')
False
>>> IS_CHARACTER_JUNK('x')
False

```python
def IS_CHARACTER_JUNK(ch, ws)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1061
