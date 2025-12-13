---
type: function
name: get_matching_blocks
module: difflib
lineno: 421
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_matching_blocks()

## Overview

Return list of triples describing matching subsequences.

Each triple is of the form (i, j, n), and means that
a[i:i+n] == b[j:j+n].  The triples are monotonically increasing in
i and in j.  New in Python 2.5, it's also guaranteed that if
(i, j, n) and (i', j', n') are adjacent triples in the list, and
the second is not the last triple in the list, then i+n != i' or
j+n != j'.  IOW, adjacent triples never describe adjacent equal
blocks.

The last triple is a dummy, (len(a), len(b), 0), and is the only
triple with n==0.

>>> s = SequenceMatcher(None, "abxcd", "abcd")
>>> list(s.get_matching_blocks())
[Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]

```python
def get_matching_blocks(self)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/SequenceMatcher|SequenceMatcher]]
**Type:** Method
**Line:** 421

## Categories

- [[Taxonomy/accessor|accessor]]
