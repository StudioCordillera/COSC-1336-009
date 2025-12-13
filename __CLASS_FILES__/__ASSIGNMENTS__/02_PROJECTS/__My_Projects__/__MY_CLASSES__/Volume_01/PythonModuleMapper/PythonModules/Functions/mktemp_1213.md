---
type: function
name: mktemp
module: tempfile
lineno: 400
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: mktemp()

## Overview

User-callable function to return a unique temporary file name.  The
file is not created.

Arguments are similar to mkstemp, except that the 'text' argument is
not accepted, and suffix=None, prefix=None and bytes file names are not
supported.

THIS FUNCTION IS UNSAFE AND SHOULD NOT BE USED.  The file name may
refer to a file that did not exist at some point, but by the time
you get around to creating it, someone else may have beaten you to
the punch.

```python
def mktemp(suffix, prefix, dir)
```

**Module:** [[Modules/tempfile|tempfile]]
**Type:** Module-level function
**Line:** 400
