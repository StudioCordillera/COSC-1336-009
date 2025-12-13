---
type: function
name: __trunc__
module: numbers
lineno: 191
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - magic_method
---

# Function: __trunc__()

## Overview

trunc(self): Truncates self to an Integral.

Returns an Integral i such that:
  * i > 0 iff self > 0;
  * abs(i) <= abs(self);
  * for any Integral j satisfying the first two conditions,
    abs(i) >= abs(j) [i.e. i has "maximal" abs among those].
i.e. "truncate towards 0".

```python
@abstractmethod
def __trunc__(self)
```

**Module:** [[Modules/numbers|numbers]]
**Class:** [[Classes/Real|Real]]
**Type:** Method
**Line:** 191

## Categories

- [[Taxonomy/magic_method|magic_method]]
