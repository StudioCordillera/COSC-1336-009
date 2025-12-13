---
type: function
name: restore
module: difflib
lineno: 2019
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: restore()

## Overview

Generate one of the two sequences that generated a delta.

Given a `delta` produced by `Differ.compare()` or `ndiff()`, extract
lines originating from file 1 or 2 (parameter `which`), stripping off line
prefixes.

Examples:

>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
...              'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> diff = list(diff)
>>> print(''.join(restore(diff, 1)), end="")
one
two
three
>>> print(''.join(restore(diff, 2)), end="")
ore
tree
emu

```python
def restore(delta, which)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 2019
