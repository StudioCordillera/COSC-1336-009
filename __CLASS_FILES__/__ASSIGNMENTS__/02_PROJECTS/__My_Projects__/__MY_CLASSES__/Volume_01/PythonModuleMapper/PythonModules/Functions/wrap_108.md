---
type: function
name: wrap
module: textwrap
lineno: 347
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: wrap()

## Overview

wrap(text : string) -> [string]

Reformat the single paragraph in 'text' so it fits in lines of
no more than 'self.width' columns, and return a list of wrapped
lines.  Tabs in 'text' are expanded with string.expandtabs(),
and all other whitespace characters (including newline) are
converted to space.

```python
def wrap(self, text)
```

**Module:** [[Modules/textwrap|textwrap]]
**Class:** [[Classes/TextWrapper|TextWrapper]]
**Type:** Method
**Line:** 347

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
