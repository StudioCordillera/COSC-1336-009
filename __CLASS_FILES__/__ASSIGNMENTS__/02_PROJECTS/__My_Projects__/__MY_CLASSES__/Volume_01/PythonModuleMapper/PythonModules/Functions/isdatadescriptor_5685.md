---
type: function
name: isdatadescriptor
module: inspect
lineno: 338
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: isdatadescriptor()

## Overview

Return true if the object is a data descriptor.

Data descriptors have a __set__ or a __delete__ attribute.  Examples are
properties (defined in Python) and getsets and members (defined in C).
Typically, data descriptors will also have __name__ and __doc__ attributes
(properties, getsets, and members have both of these attributes), but this
is not guaranteed.

```python
def isdatadescriptor(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 338
