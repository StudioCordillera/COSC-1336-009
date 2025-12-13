---
type: function
name: simplefilter
module: warnings
lineno: 170
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: simplefilter()

## Overview

Insert a simple entry into the list of warnings filters (at the front).

A simple filter matches all modules and messages.
'action' -- one of "error", "ignore", "always", "default", "module",
            or "once"
'category' -- a class that the warning must be a subclass of
'lineno' -- an integer line number, 0 matches all warnings
'append' -- if true, append to the list of filters

```python
def simplefilter(action, category, lineno, append)
```

**Module:** [[Modules/warnings|warnings]]
**Type:** Module-level function
**Line:** 170
