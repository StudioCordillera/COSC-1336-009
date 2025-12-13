---
type: function
name: __init__
module: difflib
lineno: 1688
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: __init__()

## Overview

HtmlDiff instance initializer

Arguments:
tabsize -- tab stop spacing, defaults to 8.
wrapcolumn -- column number where lines are broken and wrapped,
    defaults to None where lines are not wrapped.
linejunk,charjunk -- keyword arguments passed into ndiff() (used by
    HtmlDiff() to generate the side by side HTML differences).  See
    ndiff() documentation for argument default values and descriptions.

```python
def __init__(self, tabsize, wrapcolumn, linejunk, charjunk)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/HtmlDiff|HtmlDiff]]
**Type:** Method
**Line:** 1688
