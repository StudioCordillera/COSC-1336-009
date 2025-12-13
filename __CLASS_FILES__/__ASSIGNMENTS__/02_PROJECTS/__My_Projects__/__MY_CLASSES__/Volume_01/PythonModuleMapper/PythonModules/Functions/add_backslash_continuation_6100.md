---
type: function
name: add_backslash_continuation
module: tokenize
lineno: 185
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: add_backslash_continuation()

## Overview

Add backslash continuation characters if the row has increased
without encountering a newline token.

This also inserts the correct amount of whitespace before the backslash.

```python
def add_backslash_continuation(self, start)
```

**Module:** [[Modules/tokenize|tokenize]]
**Class:** [[Classes/Untokenizer|Untokenizer]]
**Type:** Method
**Line:** 185

## Categories

- [[Taxonomy/public_method|public_method]]
