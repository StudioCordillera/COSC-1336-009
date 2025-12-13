---
type: function
name: fix_missing_locations
module: ast
lineno: 214
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: fix_missing_locations()

## Overview

When you compile a node tree with compile(), the compiler expects lineno and
col_offset attributes for every node that supports them.  This is rather
tedious to fill in for generated nodes, so this helper adds these attributes
recursively where not already set, by setting them to the values of the
parent node.  It works recursively starting at *node*.

```python
def fix_missing_locations(node)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 214
