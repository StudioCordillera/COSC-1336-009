---
type: function
name: __newobj_ex__
module: copyreg
lineno: 101
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __newobj_ex__()

## Overview

Used by pickle protocol 4, instead of __newobj__ to allow classes with
keyword-only arguments to be pickled correctly.

```python
def __newobj_ex__(cls, args, kwargs)
```

**Module:** [[Modules/copyreg|copyreg]]
**Type:** Module-level function
**Line:** 101

## Categories

- [[Taxonomy/magic_method|magic_method]]
