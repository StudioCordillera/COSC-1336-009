---
type: function
name: checkfuncname
module: bdb
lineno: 845
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: checkfuncname()

## Overview

Return True if break should happen here.

Whether a break should happen depends on the way that b (the breakpoint)
was set.  If it was set via line number, check if b.line is the same as
the one in the frame.  If it was set via function name, check if this is
the right function and if it is on the first executable line.

```python
def checkfuncname(b, frame)
```

**Module:** [[Modules/bdb|bdb]]
**Type:** Module-level function
**Line:** 845
