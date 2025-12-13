---
type: function
name: _richcmp
module: fractions
lineno: 983
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _richcmp()

## Overview

Helper for comparison operators, for internal use only.

Implement comparison between a Rational instance `self`, and
either another Rational instance or a float `other`.  If
`other` is not a Rational instance or a float, return
NotImplemented. `op` should be one of the six standard
comparison operators.

```python
def _richcmp(self, other, op)
```

**Module:** [[Modules/fractions|fractions]]
**Class:** [[Classes/Fraction|Fraction]]
**Type:** Method
**Line:** 983

## Categories

- [[Taxonomy/protected_method|protected_method]]
