---
type: function
name: compare
module: difflib
lineno: 833
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: compare()

## Overview

Compare two sequences of lines; generate the resulting delta.

Each sequence must contain individual single-line strings ending with
newlines. Such sequences can be obtained from the `readlines()` method
of file-like objects.  The delta generated also consists of newline-
terminated strings, ready to be printed as-is via the writelines()
method of a file-like object.

Example:

>>> print(''.join(Differ().compare('one\ntwo\nthree\n'.splitlines(True),
...                                'ore\ntree\nemu\n'.splitlines(True))),
...       end="")
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
def compare(self, a, b)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/Differ|Differ]]
**Type:** Method
**Line:** 833

## Categories

- [[Taxonomy/public_method|public_method]]
