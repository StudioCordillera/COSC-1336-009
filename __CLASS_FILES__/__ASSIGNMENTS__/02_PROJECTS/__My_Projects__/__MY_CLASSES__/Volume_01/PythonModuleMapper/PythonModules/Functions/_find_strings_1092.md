---
type: function
name: _find_strings
module: trace
lineno: 356
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _find_strings()

## Overview

Return a dict of possible docstring positions.

The dict maps line numbers to strings.  There is an entry for
line that contains only a string or a part of a triple-quoted
string.

```python
def _find_strings(filename, encoding)
```

**Module:** [[Modules/trace|trace]]
**Type:** Module-level function
**Line:** 356
