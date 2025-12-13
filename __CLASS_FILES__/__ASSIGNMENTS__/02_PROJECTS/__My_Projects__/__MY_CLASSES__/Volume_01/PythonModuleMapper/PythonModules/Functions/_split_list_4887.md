---
type: function
name: _split_list
module: pydoc
lineno: 303
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _split_list()

## Overview

Split sequence s via predicate, and return pair ([true], [false]).

The return value is a 2-tuple of lists,
    ([x for x in s if predicate(x)],
     [x for x in s if not predicate(x)])

```python
def _split_list(s, predicate)
```

**Module:** [[Modules/pydoc|pydoc]]
**Type:** Module-level function
**Line:** 303
