---
type: function
name: no_type_check
module: typing
lineno: 2630
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: no_type_check()

## Overview

Decorator to indicate that annotations are not type hints.

The argument must be a class or function; if it is a class, it
applies recursively to all methods and classes defined in that class
(but not to methods defined in its superclasses or subclasses).

This mutates the function(s) or class(es) in place.

```python
def no_type_check(arg)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2630
