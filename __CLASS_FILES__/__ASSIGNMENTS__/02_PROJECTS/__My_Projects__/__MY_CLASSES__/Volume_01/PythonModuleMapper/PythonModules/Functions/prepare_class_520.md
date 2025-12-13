---
type: function
name: prepare_class
module: types
lineno: 98
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: prepare_class()

## Overview

Call the __prepare__ method of the appropriate metaclass.

Returns (metaclass, namespace, kwds) as a 3-tuple

*metaclass* is the appropriate metaclass
*namespace* is the prepared class namespace
*kwds* is an updated copy of the passed in kwds argument with any
'metaclass' entry removed. If no kwds argument is passed in, this will
be an empty dict.

```python
def prepare_class(name, bases, kwds)
```

**Module:** [[Modules/types|types]]
**Type:** Module-level function
**Line:** 98
