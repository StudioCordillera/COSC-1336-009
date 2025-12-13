---
type: function
name: parse
module: ast
lineno: 30
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: parse()

## Overview

Parse the source into an AST node.
Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
Pass type_comments=True to get back type comments where the syntax allows.

```python
def parse(source, filename, mode)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 30
