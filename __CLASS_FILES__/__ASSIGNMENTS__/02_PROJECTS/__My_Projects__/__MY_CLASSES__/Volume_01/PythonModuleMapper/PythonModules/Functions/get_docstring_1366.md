---
type: function
name: get_docstring
module: ast
lineno: 298
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_docstring()

## Overview

Return the docstring for the given node or None if no docstring can
be found.  If the node provided does not have docstrings a TypeError
will be raised.

If *clean* is `True`, all tabs are expanded to spaces and any whitespace
that can be uniformly removed from the second line onwards is removed.

```python
def get_docstring(node, clean)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 298

## Categories

- [[Taxonomy/accessor|accessor]]
