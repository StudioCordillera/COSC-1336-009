---
type: function
name: getclasstree
module: inspect
lineno: 1272
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getclasstree()

## Overview

Arrange the given list of classes into a hierarchy of nested lists.

Where a nested list appears, it contains classes derived from the class
whose entry immediately precedes the list.  Each entry is a 2-tuple
containing a class and a tuple of its base classes.  If the 'unique'
argument is true, exactly one entry appears in the returned structure
for each class in the given list.  Otherwise, classes using multiple
inheritance and their descendants will appear multiple times.

```python
def getclasstree(classes, unique)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1272
