---
type: function
name: elements
module: collections
lineno: 638
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: elements()

## Overview

Iterator over elements repeating each as many times as its count.

>>> c = Counter('ABCABC')
>>> sorted(c.elements())
['A', 'A', 'B', 'B', 'C', 'C']

Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1

>>> import math
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> math.prod(prime_factors.elements())
1836

Note, if an element's count has been set to zero or is a negative
number, elements() will ignore it.

```python
def elements(self)
```

**Module:** [[Modules/collections|collections]]
**Class:** [[Classes/Counter|Counter]]
**Type:** Method
**Line:** 638

## Categories

- [[Taxonomy/public_method|public_method]]
