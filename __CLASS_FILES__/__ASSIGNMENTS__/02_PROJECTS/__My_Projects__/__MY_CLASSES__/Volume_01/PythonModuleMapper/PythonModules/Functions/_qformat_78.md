---
type: function
name: _qformat
module: difflib
lineno: 999
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _qformat()

## Overview

Format "?" output and deal with tabs.

Example:

>>> d = Differ()
>>> results = d._qformat('\tabcDefghiJkl\n', '\tabcdefGhijkl\n',
...                      '  ^ ^  ^      ', '  ^ ^  ^      ')
>>> for line in results: print(repr(line))
...
'- \tabcDefghiJkl\n'
'? \t ^ ^  ^\n'
'+ \tabcdefGhijkl\n'
'? \t ^ ^  ^\n'

```python
def _qformat(self, aline, bline, atags, btags)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/Differ|Differ]]
**Type:** Method
**Line:** 999

## Categories

- [[Taxonomy/protected_method|protected_method]]
