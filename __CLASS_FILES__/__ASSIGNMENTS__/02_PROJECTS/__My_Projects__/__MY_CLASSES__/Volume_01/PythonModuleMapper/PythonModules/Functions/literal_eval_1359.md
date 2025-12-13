---
type: function
name: literal_eval
module: ast
lineno: 54
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: literal_eval()

## Overview

Evaluate an expression node or a string containing only a Python
expression.  The string or node provided may only consist of the following
Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
sets, booleans, and None.

Caution: A complex expression can overflow the C stack and cause a crash.

```python
def literal_eval(node_or_string)
```

**Module:** [[Modules/ast|ast]]
**Type:** Module-level function
**Line:** 54
