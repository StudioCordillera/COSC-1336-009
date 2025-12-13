---
type: function
name: context_diff
module: difflib
lineno: 1180
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: context_diff()

## Overview

Compare two sequences of lines; generate the delta as a context diff.

Context diffs are a compact way of showing line changes and a few
lines of context.  The number of context lines is set by 'n' which
defaults to three.

By default, the diff control lines (those with *** or ---) are
created with a trailing newline.  This is helpful so that inputs
created from file.readlines() result in diffs that are suitable for
file.writelines() since both the inputs and outputs have trailing
newlines.

For inputs that do not have trailing newlines, set the lineterm
argument to "" so that the output will be uniformly newline free.

The context diff format normally has a header for filenames and
modification times.  Any or all of these may be specified using
strings for 'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
The modification times are normally expressed in the ISO 8601 format.
If not specified, the strings default to blanks.

Example:

>>> print(''.join(context_diff('one\ntwo\nthree\nfour\n'.splitlines(True),
...       'zero\none\ntree\nfour\n'.splitlines(True), 'Original', 'Current')),
...       end="")
*** Original
--- Current
***************
*** 1,4 ****
  one
! two
! three
  four
--- 1,4 ----
+ zero
  one
! tree
  four

```python
def context_diff(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1180
