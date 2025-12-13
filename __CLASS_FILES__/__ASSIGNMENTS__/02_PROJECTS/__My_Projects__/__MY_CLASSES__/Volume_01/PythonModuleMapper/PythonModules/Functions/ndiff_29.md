---
type: function
name: ndiff
module: difflib
lineno: 1303
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ndiff()

## Overview

Compare `a` and `b` (lists of strings); return a `Differ`-style delta.

Optional keyword parameters `linejunk` and `charjunk` are for filter
functions, or can be None:

- linejunk: A function that should accept a single string argument and
  return true iff the string is junk.  The default is None, and is
  recommended; the underlying SequenceMatcher class has an adaptive
  notion of "noise" lines.

- charjunk: A function that accepts a character (string of length
  1), and returns true iff the character is junk. The default is
  the module-level function IS_CHARACTER_JUNK, which filters out
  whitespace characters (a blank or tab; note: it's a bad idea to
  include newline in this!).

Tools/scripts/ndiff.py is a command-line front-end to this function.

Example:

>>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
...              'ore\ntree\nemu\n'.splitlines(keepends=True))
>>> print(''.join(diff), end="")
- one
?  ^
+ ore
?  ^
- two
- three
?  -
+ tree
+ emu

```python
def ndiff(a, b, linejunk, charjunk)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1303
