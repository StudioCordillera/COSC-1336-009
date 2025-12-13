---
type: function
name: delimit
module: ast
lineno: 813
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: delimit()

## Overview

A context manager for preparing the source for expressions. It adds
*start* to the buffer and enters, after exit it adds *end*.

```python
@contextmanager
def delimit(self, start, end)
```

**Module:** [[Modules/ast|ast]]
**Class:** [[Classes/_Unparser|_Unparser]]
**Type:** Method
**Line:** 813

## Categories

- [[Taxonomy/public_method|public_method]]
