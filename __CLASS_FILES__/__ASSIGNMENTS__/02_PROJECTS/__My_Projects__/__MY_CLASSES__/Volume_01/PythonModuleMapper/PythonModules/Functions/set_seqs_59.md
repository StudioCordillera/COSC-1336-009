---
type: function
name: set_seqs
module: difflib
lineno: 184
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_seqs()

## Overview

Set the two sequences to be compared.

>>> s = SequenceMatcher()
>>> s.set_seqs("abcd", "bcde")
>>> s.ratio()
0.75

```python
def set_seqs(self, a, b)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/SequenceMatcher|SequenceMatcher]]
**Type:** Method
**Line:** 184

## Categories

- [[Taxonomy/mutator|mutator]]
