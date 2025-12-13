---
type: function
name: _signature_strip_non_python_syntax
module: inspect
lineno: 2170
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _signature_strip_non_python_syntax()

## Overview

Private helper function. Takes a signature in Argument Clinic's
extended signature format.

Returns a tuple of two things:
  * that signature re-rendered in standard Python syntax, and
  * the index of the "self" parameter (generally 0), or None if
    the function does not have a "self" parameter.

```python
def _signature_strip_non_python_syntax(signature)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 2170
