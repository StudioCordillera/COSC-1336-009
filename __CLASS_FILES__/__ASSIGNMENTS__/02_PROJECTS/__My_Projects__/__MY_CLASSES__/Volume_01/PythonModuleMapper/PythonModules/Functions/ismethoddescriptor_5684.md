---
type: function
name: ismethoddescriptor
module: inspect
lineno: 310
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ismethoddescriptor()

## Overview

Return true if the object is a method descriptor.

But not if ismethod() or isclass() or isfunction() are true.

This is new in Python 2.2, and, for example, is true of int.__add__.
An object passing this test has a __get__ attribute, but not a
__set__ attribute or a __delete__ attribute. Beyond that, the set
of attributes varies; __name__ is usually sensible, and __doc__
often is.

Methods implemented via descriptors that also pass one of the other
tests return false from the ismethoddescriptor() test, simply because
the other tests promise more -- you can, e.g., count on having the
__func__ attribute (etc) when an object passes ismethod().

```python
def ismethoddescriptor(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 310
