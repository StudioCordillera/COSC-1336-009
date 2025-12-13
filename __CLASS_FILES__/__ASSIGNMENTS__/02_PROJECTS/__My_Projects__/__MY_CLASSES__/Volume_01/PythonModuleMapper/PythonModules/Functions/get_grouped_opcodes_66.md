---
type: function
name: get_grouped_opcodes
module: difflib
lineno: 547
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_grouped_opcodes()

## Overview

Isolate change clusters by eliminating ranges with no changes.

Return a generator of groups with up to n lines of context.
Each group is in the same format as returned by get_opcodes().

>>> from pprint import pprint
>>> a = list(map(str, range(1,40)))
>>> b = a[:]
>>> b[8:8] = ['i']     # Make an insertion
>>> b[20] += 'x'       # Make a replacement
>>> b[23:28] = []      # Make a deletion
>>> b[30] += 'y'       # Make another replacement
>>> pprint(list(SequenceMatcher(None,a,b).get_grouped_opcodes()))
[[('equal', 5, 8, 5, 8), ('insert', 8, 8, 8, 9), ('equal', 8, 11, 9, 12)],
 [('equal', 16, 19, 17, 20),
  ('replace', 19, 20, 20, 21),
  ('equal', 20, 22, 21, 23),
  ('delete', 22, 27, 23, 23),
  ('equal', 27, 30, 23, 26)],
 [('equal', 31, 34, 27, 30),
  ('replace', 34, 35, 30, 31),
  ('equal', 35, 38, 31, 34)]]

```python
def get_grouped_opcodes(self, n)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/SequenceMatcher|SequenceMatcher]]
**Type:** Method
**Line:** 547

## Categories

- [[Taxonomy/accessor|accessor]]
