---
type: function
name: __init__
module: difflib
lineno: 120
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - constructor
  - constructor
  - constructor
---

# Function: __init__()

## Overview

Construct a SequenceMatcher.

Optional arg isjunk is None (the default), or a one-argument
function that takes a sequence element and returns true iff the
element is junk.  None is equivalent to passing "lambda x: 0", i.e.
no elements are considered to be junk.  For example, pass
    lambda x: x in " \t"
if you're comparing lines as sequences of characters, and don't
want to synch up on blanks or hard tabs.

Optional arg a is the first of two sequences to be compared.  By
default, an empty string.  The elements of a must be hashable.  See
also .set_seqs() and .set_seq1().

Optional arg b is the second of two sequences to be compared.  By
default, an empty string.  The elements of b must be hashable. See
also .set_seqs() and .set_seq2().

Optional arg autojunk should be set to False to disable the
"automatic junk heuristic" that treats popular elements as junk
(see module documentation for more information).

```python
def __init__(self, isjunk, a, b, autojunk)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/SequenceMatcher|SequenceMatcher]]
**Type:** Method
**Line:** 120

## Categories

- [[Taxonomy/constructor|constructor]]
- [[Taxonomy/constructor|constructor]]
- [[Taxonomy/constructor|constructor]]
