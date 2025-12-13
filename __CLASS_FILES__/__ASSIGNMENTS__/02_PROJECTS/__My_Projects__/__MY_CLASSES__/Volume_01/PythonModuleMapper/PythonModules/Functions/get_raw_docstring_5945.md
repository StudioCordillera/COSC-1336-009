---
type: function
name: get_raw_docstring
module: ast
lineno: 838
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_raw_docstring()

## Overview

If a docstring node is found in the body of the *node* parameter,
return that docstring node, None otherwise.

Logic mirrored from ``_PyAST_GetDocString``.

```python
def get_raw_docstring(self, node)
```

**Module:** [[Modules/ast|ast]]
**Class:** [[Classes/_Unparser|_Unparser]]
**Type:** Method
**Line:** 838

## Categories

- [[Taxonomy/accessor|accessor]]
