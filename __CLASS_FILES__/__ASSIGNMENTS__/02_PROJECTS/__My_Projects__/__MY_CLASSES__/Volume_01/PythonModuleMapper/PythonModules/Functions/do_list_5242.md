---
type: function
name: do_list
module: pdb
lineno: 1817
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_list()

## Overview

l(ist) [first[, last] | .]

List source code for the current file.  Without arguments,
list 11 lines around the current line or continue the previous
listing.  With . as argument, list 11 lines around the current
line.  With one argument, list 11 lines starting at that line.
With two arguments, list the given range; if the second
argument is less than the first, it is a count.

The current line in the current frame is indicated by "->".
If an exception is being debugged, the line where the
exception was originally raised or propagated is indicated by
">>", if it differs from the current line.

```python
def do_list(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1817

## Categories

- [[Taxonomy/public_method|public_method]]
