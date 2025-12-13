---
type: function
name: _fix_sentence_endings
module: textwrap
lineno: 179
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _fix_sentence_endings()

## Overview

_fix_sentence_endings(chunks : [string])

Correct for sentence endings buried in 'chunks'.  Eg. when the
original text contains "... foo.\nBar ...", munge_whitespace()
and split() will convert that to [..., "foo.", " ", "Bar", ...]
which has one too few spaces; this method simply changes the one
space to two.

```python
def _fix_sentence_endings(self, chunks)
```

**Module:** [[Modules/textwrap|textwrap]]
**Class:** [[Classes/TextWrapper|TextWrapper]]
**Type:** Method
**Line:** 179

## Categories

- [[Taxonomy/protected_method|protected_method]]
