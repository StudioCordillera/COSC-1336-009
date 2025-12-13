---
type: function
name: _fileobj_lookup
module: selectors
lineno: 219
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _fileobj_lookup()

## Overview

Return a file descriptor from a file object.

This wraps _fileobj_to_fd() to do an exhaustive search in case
the object is invalid but we still have it in our map.  This
is used by unregister() so we can unregister an object that
was previously registered even if it is closed.  It is also
used by _SelectorMapping.

```python
def _fileobj_lookup(self, fileobj)
```

**Module:** [[Modules/selectors|selectors]]
**Class:** [[Classes/_BaseSelectorImpl|_BaseSelectorImpl]]
**Type:** Method
**Line:** 219

## Categories

- [[Taxonomy/protected_method|protected_method]]
