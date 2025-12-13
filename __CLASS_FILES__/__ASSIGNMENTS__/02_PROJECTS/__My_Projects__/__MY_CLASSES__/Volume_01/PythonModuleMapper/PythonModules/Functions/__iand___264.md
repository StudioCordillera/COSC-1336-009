---
type: function
name: __iand__
module: collections
lineno: 969
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __iand__()

## Overview

Inplace intersection is the minimum of corresponding counts.

>>> c = Counter('abbb')
>>> c &= Counter('bcc')
>>> c
Counter({'b': 1})

```python
def __iand__(self, other)
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 969

## Categories

- [[Taxonomy/magic_method|magic_method]]
