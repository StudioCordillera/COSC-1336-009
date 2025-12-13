---
type: function
name: _fancy_replace
module: difflib
lineno: 893
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _fancy_replace()

## Overview

When replacing one block of lines with another, search the blocks
for *similar* lines; the best-matching pair (if any) is used as a
synch point, and intraline difference marking is done on the
similar pair. Lots of work, but often worth it.

Example:

>>> d = Differ()
>>> results = d._fancy_replace(['abcDefghiJkl\n'], 0, 1,
...                            ['abcdefGhijkl\n'], 0, 1)
>>> print(''.join(results), end="")
- abcDefghiJkl
?    ^  ^  ^
+ abcdefGhijkl
?    ^  ^  ^

```python
def _fancy_replace(self, a, alo, ahi, b, blo, bhi)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/Differ|Differ]]
**Type:** Method
**Line:** 893

## Categories

- [[Taxonomy/protected_method|protected_method]]
