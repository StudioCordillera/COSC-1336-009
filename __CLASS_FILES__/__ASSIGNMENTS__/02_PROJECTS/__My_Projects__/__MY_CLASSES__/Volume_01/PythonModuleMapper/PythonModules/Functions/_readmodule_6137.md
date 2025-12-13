---
type: function
name: _readmodule
module: pyclbr
lineno: 122
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _readmodule()

## Overview

Do the hard work for readmodule[_ex].

If inpackage is given, it must be the dotted name of the package in
which we are searching for a submodule, and then PATH must be the
package search path; otherwise, we are searching for a top-level
module, and path is combined with sys.path.

```python
def _readmodule(module, path, inpackage)
```

**Module:** [[Modules/pyclbr|pyclbr]]
**Type:** Module-level function
**Line:** 122
