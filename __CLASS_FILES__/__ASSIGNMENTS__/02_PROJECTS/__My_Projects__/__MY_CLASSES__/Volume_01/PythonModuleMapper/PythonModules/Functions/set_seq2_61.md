---
type: function
name: set_seq2
module: difflib
lineno: 222
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_seq2()

## Overview

Set the second sequence to be compared.

The first sequence to be compared is not changed.

>>> s = SequenceMatcher(None, "abcd", "bcde")
>>> s.ratio()
0.75
>>> s.set_seq2("abcd")
>>> s.ratio()
1.0
>>>

SequenceMatcher computes and caches detailed information about the
second sequence, so if you want to compare one sequence S against
many sequences, use .set_seq2(S) once and call .set_seq1(x)
repeatedly for each of the other sequences.

See also set_seqs() and set_seq1().

```python
def set_seq2(self, b)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/SequenceMatcher|SequenceMatcher]]
**Type:** Method
**Line:** 222

## Categories

- [[Taxonomy/mutator|mutator]]
