---
type: function
name: __isub__
module: collections
lineno: 941
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __isub__()

## Overview

Inplace subtract counter, but keep only results with positive counts.

>>> c = Counter('abbbc')
>>> c -= Counter('bccd')
>>> c
Counter({'b': 2, 'a': 1})

```python
def __isub__(self, other)
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 941

## Categories

- [[Taxonomy/magic_method|magic_method]]
