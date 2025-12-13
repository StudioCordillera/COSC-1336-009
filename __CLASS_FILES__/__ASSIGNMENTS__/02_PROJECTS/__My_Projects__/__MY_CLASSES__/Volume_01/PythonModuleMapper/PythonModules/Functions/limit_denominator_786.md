---
type: function
name: limit_denominator
module: fractions
lineno: 357
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: limit_denominator()

## Overview

Closest Fraction to self with denominator at most max_denominator.

>>> Fraction('3.141592653589793').limit_denominator(10)
Fraction(22, 7)
>>> Fraction('3.141592653589793').limit_denominator(100)
Fraction(311, 99)
>>> Fraction(4321, 8765).limit_denominator(10000)
Fraction(4321, 8765)

```python
def limit_denominator(self, max_denominator)
```

**Module:** [[Modules/fractions|fractions]]
**Class:** [[Classes/Fraction|Fraction]]
**Type:** Method
**Line:** 357

## Categories

- [[Taxonomy/public_method|public_method]]
