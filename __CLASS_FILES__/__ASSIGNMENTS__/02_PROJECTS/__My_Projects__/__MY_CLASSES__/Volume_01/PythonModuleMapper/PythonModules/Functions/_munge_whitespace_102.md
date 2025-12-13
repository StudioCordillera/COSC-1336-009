---
type: function
name: _munge_whitespace
module: textwrap
lineno: 143
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _munge_whitespace()

## Overview

_munge_whitespace(text : string) -> string

Munge whitespace in text: expand tabs and convert all other
whitespace characters to spaces.  Eg. " foo\tbar\n\nbaz"
becomes " foo    bar  baz".

```python
def _munge_whitespace(self, text)
```

**Module:** [[Modules/textwrap|textwrap]]
**Class:** [[Classes/TextWrapper|TextWrapper]]
**Type:** Method
**Line:** 143

## Categories

- [[Taxonomy/protected_method|protected_method]]
