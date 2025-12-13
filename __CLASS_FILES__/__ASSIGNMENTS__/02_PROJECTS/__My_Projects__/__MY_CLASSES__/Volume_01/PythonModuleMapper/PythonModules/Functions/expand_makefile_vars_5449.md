---
type: function
name: expand_makefile_vars
module: sysconfig
lineno: 697
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: expand_makefile_vars()

## Overview

Expand Makefile-style variables -- "${foo}" or "$(foo)" -- in
'string' according to 'vars' (a dictionary mapping variable names to
values).  Variables not present in 'vars' are silently expanded to the
empty string.  The variable values in 'vars' should not contain further
variable expansions; if 'vars' is the output of 'parse_makefile()',
you're fine.  Returns a variable-expanded version of 's'.

```python
def expand_makefile_vars(s, vars)
```

**Module:** [[Modules/sysconfig|sysconfig]]
**Type:** Module-level function
**Line:** 697
