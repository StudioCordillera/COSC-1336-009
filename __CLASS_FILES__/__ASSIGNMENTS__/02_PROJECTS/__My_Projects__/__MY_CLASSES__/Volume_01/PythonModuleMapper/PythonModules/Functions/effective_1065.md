---
type: function
name: effective
module: bdb
lineno: 877
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: effective()

## Overview

Return (active breakpoint, delete temporary flag) or (None, None) as
breakpoint to act upon.

The "active breakpoint" is the first entry in bplist[line, file] (which
must exist) that is enabled, for which checkfuncname is True, and that
has neither a False condition nor a positive ignore count.  The flag,
meaning that a temporary breakpoint should be deleted, is False only
when the condiion cannot be evaluated (in which case, ignore count is
ignored).

If no such entry exists, then (None, None) is returned.

```python
def effective(file, line, frame)
```

**Module:** [[Modules/bdb|bdb]]
**Type:** Module-level function
**Line:** 877
