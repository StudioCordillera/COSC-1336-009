---
type: function
name: block
module: ast
lineno: 799
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: block()

## Overview

A context manager for preparing the source for blocks. It adds
the character':', increases the indentation on enter and decreases
the indentation on exit. If *extra* is given, it will be directly
appended after the colon character.

```python
@contextmanager
def block(self)
```

**Module:** [[Modules/ast|ast]]
**Class:** [[Classes/_Unparser|_Unparser]]
**Type:** Method
**Line:** 799

## Categories

- [[Taxonomy/public_method|public_method]]
