---
type: function
name: unified_diff
module: difflib
lineno: 1095
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: unified_diff()

## Overview

Compare two sequences of lines; generate the delta as a unified diff.

Unified diffs are a compact way of showing line changes and a few
lines of context.  The number of context lines is set by 'n' which
defaults to three.

By default, the diff control lines (those with ---, +++, or @@) are
created with a trailing newline.  This is helpful so that inputs
created from file.readlines() result in diffs that are suitable for
file.writelines() since both the inputs and outputs have trailing
newlines.

For inputs that do not have trailing newlines, set the lineterm
argument to "" so that the output will be uniformly newline free.

The unidiff format normally has a header for filenames and modification
times.  Any or all of these may be specified using strings for
'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
The modification times are normally expressed in the ISO 8601 format.

Example:

>>> for line in unified_diff('one two three four'.split(),
...             'zero one tree four'.split(), 'Original', 'Current',
...             '2005-01-26 23:30:50', '2010-04-02 10:20:52',
...             lineterm=''):
...     print(line)                 # doctest: +NORMALIZE_WHITESPACE
--- Original        2005-01-26 23:30:50
+++ Current         2010-04-02 10:20:52
@@ -1,4 +1,4 @@
+zero
 one
-two
-three
+tree
 four

```python
def unified_diff(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)
```

**Module:** [[Modules/difflib|difflib]]
**Type:** Module-level function
**Line:** 1095
