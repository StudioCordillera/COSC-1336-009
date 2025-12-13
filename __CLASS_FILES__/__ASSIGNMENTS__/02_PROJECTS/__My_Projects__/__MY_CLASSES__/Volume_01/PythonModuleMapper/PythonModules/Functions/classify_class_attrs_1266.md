---
type: function
name: classify_class_attrs
module: inspect
lineno: 642
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: classify_class_attrs()

## Overview

Return list of attribute-descriptor tuples.

For each name in dir(cls), the return list contains a 4-tuple
with these elements:

    0. The name (a string).

    1. The kind of attribute this is, one of these strings:
           'class method'    created via classmethod()
           'static method'   created via staticmethod()
           'property'        created via property()
           'method'          any other flavor of method or descriptor
           'data'            not a method

    2. The class which defined this attribute (a class).

    3. The object as obtained by calling getattr; if this fails, or if the
       resulting object does not live anywhere in the class' mro (including
       metaclasses) then the object is looked up in the defining class's
       dict (found by walking the mro).

If one of the items in dir(cls) is stored in the metaclass it will now
be discovered and not have None be listed as the class in which it was
defined.  Any items whose home class cannot be discovered are skipped.

```python
def classify_class_attrs(cls)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 642
