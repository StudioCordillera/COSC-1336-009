---
type: function
name: unregister
module: selectors
lineno: 123
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
  - public_method
  - public_method
  - public_method
---

# Function: unregister()

## Overview

Unregister a file object.

Parameters:
fileobj -- file object or file descriptor

Returns:
SelectorKey instance

Raises:
KeyError if fileobj is not registered

Note:
If fileobj is registered but has since been closed this does
*not* raise OSError (even if the wrapped syscall does)

```python
@abstractmethod
def unregister(self, fileobj)
```

**Module:** [[Modules/selectors|selectors]]
**Class:** [[Classes/BaseSelector|BaseSelector]]
**Type:** Method
**Line:** 123

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
