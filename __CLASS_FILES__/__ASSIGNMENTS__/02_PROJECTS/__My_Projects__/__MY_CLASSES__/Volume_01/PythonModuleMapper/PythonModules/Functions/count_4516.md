---
type: function
name: count
module: tkinter
lineno: 3787
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: count()

## Overview

Counts the number of relevant things between the two indices.

If INDEX1 is after INDEX2, the result will be a negative number
(and this holds for each of the possible options).

The actual items which are counted depends on the options given.
The result is a tuple of integers, one for the result of each
counting option given, if more than one option is specified or
return_ints is false (default), otherwise it is an integer.
Valid counting options are "chars", "displaychars",
"displayindices", "displaylines", "indices", "lines", "xpixels"
and "ypixels". The default value, if no option is specified, is
"indices". There is an additional possible option "update",
which if given then all subsequent options ensure that any
possible out of date information is recalculated.

```python
def count(self, index1, index2)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Text|Text]]
**Type:** Method
**Line:** 3787

## Categories

- [[Taxonomy/public_method|public_method]]
