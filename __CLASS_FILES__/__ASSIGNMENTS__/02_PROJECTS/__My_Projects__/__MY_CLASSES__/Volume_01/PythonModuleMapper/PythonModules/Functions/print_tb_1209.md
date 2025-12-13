---
type: function
name: print_tb
module: traceback
lineno: 51
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: print_tb()

## Overview

Print up to 'limit' stack trace entries from the traceback 'tb'.

If 'limit' is omitted or None, all entries are printed.  If 'file'
is omitted or None, the output goes to sys.stderr; otherwise
'file' should be an open file or file-like object with a write()
method.

```python
def print_tb(tb, limit, file)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 51
