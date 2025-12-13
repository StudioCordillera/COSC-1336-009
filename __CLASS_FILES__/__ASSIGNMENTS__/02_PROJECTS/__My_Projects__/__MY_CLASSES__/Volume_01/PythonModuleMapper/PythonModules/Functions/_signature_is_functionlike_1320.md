---
type: function
name: _signature_is_functionlike
module: inspect
lineno: 2145
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _signature_is_functionlike()

## Overview

Private helper to test if `obj` is a duck type of FunctionType.
A good example of such objects are functions compiled with
Cython, which have all attributes that a pure Python function
would have, but have their code statically compiled.

```python
def _signature_is_functionlike(obj)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 2145
