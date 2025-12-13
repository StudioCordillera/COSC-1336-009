---
type: function
name: clear_memo
module: pickle
lineno: 463
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: clear_memo()

## Overview

Clears the pickler's "memo".

The memo is the data structure that remembers which objects the
pickler has already seen, so that shared or recursive objects
are pickled by reference and not by value.  This method is
useful when re-using picklers.

```python
def clear_memo(self)
```

**Module:** [[Modules/pickle|pickle]]
**Class:** [[Classes/_Pickler|_Pickler]]
**Type:** Method
**Line:** 463

## Categories

- [[Taxonomy/public_method|public_method]]
