---
type: function
name: post_mortem
module: pdb
lineno: 2351
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: post_mortem()

## Overview

Enter post-mortem debugging of the given *traceback*, or *exception*
object.

If no traceback is given, it uses the one of the exception that is
currently being handled (an exception must be being handled if the
default is to be used).

If `t` is an exception object, the `exceptions` command makes it possible to
list and inspect its chained exceptions (if any).

```python
def post_mortem(t)
```

**Module:** [[Modules/pdb|pdb]]
**Type:** Module-level function
**Line:** 2351
