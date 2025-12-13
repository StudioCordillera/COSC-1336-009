---
type: function
name: copy_location
module: ast
lineno: 197
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: copy_location()

## Overview

Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`
attributes) from *old_node* to *new_node* if possible, and return *new_node*.

```python
def copy_location(new_node, old_node)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 197
