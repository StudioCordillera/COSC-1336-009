---
type: function
name: extract_stack
module: traceback
lineno: 249
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: extract_stack()

## Overview

Extract the raw traceback from the current stack frame.

The return value has the same format as for extract_tb().  The
optional 'f' and 'limit' arguments have the same meaning as for
print_stack().  Each item in the list is a quadruple (filename,
line number, function name, text), and the entries are in order
from oldest to newest stack frame.

```python
def extract_stack(f, limit)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 249
