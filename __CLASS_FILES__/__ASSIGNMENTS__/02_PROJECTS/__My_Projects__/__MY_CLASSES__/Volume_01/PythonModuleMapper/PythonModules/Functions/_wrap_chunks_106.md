---
type: function
name: _wrap_chunks
module: textwrap
lineno: 238
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _wrap_chunks()

## Overview

_wrap_chunks(chunks : [string]) -> [string]

Wrap a sequence of text chunks and return a list of lines of
length 'self.width' or less.  (If 'break_long_words' is false,
some lines may be longer than this.)  Chunks correspond roughly
to words and the whitespace between them: each chunk is
indivisible (modulo 'break_long_words'), but a line break can
come between any two chunks.  Chunks should not have internal
whitespace; ie. a chunk is either all whitespace or a "word".
Whitespace chunks will be removed from the beginning and end of
lines, but apart from that whitespace is preserved.

```python
def _wrap_chunks(self, chunks)
```

**Module:** [[Modules/textwrap|textwrap]]
**Class:** [[Classes/TextWrapper|TextWrapper]]
**Type:** Method
**Line:** 238

## Categories

- [[Taxonomy/protected_method|protected_method]]
