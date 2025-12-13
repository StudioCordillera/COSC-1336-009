---
type: function
name: get_source_segment
module: ast
lineno: 347
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_source_segment()

## Overview

Get source code segment of the *source* that generated *node*.

If some location information (`lineno`, `end_lineno`, `col_offset`,
or `end_col_offset`) is missing, return None.

If *padded* is `True`, the first line of a multi-line statement will
be padded with spaces to match its original position.

```python
def get_source_segment(source, node)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 347

## Categories

- [[Taxonomy/accessor|accessor]]
