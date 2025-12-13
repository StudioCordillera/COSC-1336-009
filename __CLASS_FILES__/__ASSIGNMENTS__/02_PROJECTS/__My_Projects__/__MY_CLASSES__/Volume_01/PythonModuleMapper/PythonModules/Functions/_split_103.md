---
type: function
name: _split
module: textwrap
lineno: 157
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _split()

## Overview

_split(text : string) -> [string]

Split the text to wrap into indivisible chunks.  Chunks are
not quite the same as words; see _wrap_chunks() for full
details.  As an example, the text
  Look, goof-ball -- use the -b option!
breaks into the following chunks:
  'Look,', ' ', 'goof-', 'ball', ' ', '--', ' ',
  'use', ' ', 'the', ' ', '-b', ' ', 'option!'
if break_on_hyphens is True, or in:
  'Look,', ' ', 'goof-ball', ' ', '--', ' ',
  'use', ' ', 'the', ' ', '-b', ' ', option!'
otherwise.

```python
def _split(self, text)
```

**Module:** [[Modules/textwrap|textwrap]]
**Class:** [[Classes/TextWrapper|TextWrapper]]
**Type:** Method
**Line:** 157

## Categories

- [[Taxonomy/protected_method|protected_method]]
