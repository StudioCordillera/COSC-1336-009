---
type: function
name: singledispatch
module: functools
lineno: 826
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: singledispatch()

## Overview

Single-dispatch generic function decorator.

Transforms a function into a generic function, which can have different
behaviours depending upon the type of its first argument. The decorated
function acts as the default implementation, and additional
implementations can be registered using the register() attribute of the
generic function.

```python
def singledispatch(func)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 826
