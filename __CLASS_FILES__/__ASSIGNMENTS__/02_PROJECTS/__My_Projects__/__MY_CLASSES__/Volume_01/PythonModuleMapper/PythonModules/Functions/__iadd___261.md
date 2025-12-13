---
type: function
name: __iadd__
module: collections
lineno: 928
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
  - magic_method
---

# Function: __iadd__()

## Overview

Inplace add from another counter, keeping only positive counts.

>>> c = Counter('abbb')
>>> c += Counter('bcc')
>>> c
Counter({'b': 4, 'c': 2, 'a': 1})

```python
def __iadd__(self, other)
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 928

## Categories

- [[Taxonomy/magic_method|magic_method]]
- [[Taxonomy/magic_method|magic_method]]
