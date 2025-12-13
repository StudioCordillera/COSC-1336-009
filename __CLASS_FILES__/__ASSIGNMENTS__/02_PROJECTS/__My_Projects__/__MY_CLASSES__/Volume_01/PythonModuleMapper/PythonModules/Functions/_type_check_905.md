---
type: function
name: _type_check
module: typing
lineno: 173
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _type_check()

## Overview

Check that the argument is a type, and return it (internal helper).

As a special case, accept None and return type(None) instead. Also wrap strings
into ForwardRef instances. Consider several corner cases, for example plain
special forms like Union are not valid, while Union[int, str] is OK, etc.
The msg argument is a human-readable error message, e.g.::

    "Union[arg, ...]: arg should be a type."

We append the repr() of the actual value (truncated to 100 chars).

```python
def _type_check(arg, msg, is_argument, module)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 173
