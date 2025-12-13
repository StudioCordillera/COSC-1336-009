---
type: function
name: filterwarnings
module: warnings
lineno: 131
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: filterwarnings()

## Overview

Insert an entry into the list of warnings filters (at the front).

'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'message' -- a regex that the warning message must match
'category' -- a class that the warning must be a subclass of
'module' -- a regex that the module name must match
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters

```python
def filterwarnings(action, message, category, module, lineno, append)
```

**Module:** [[Modules/warnings|warnings]]
**Type:** Module-level function
**Line:** 131
