---
type: function
name: __float__
module: numbers
lineno: 308
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: __float__()

## Overview

float(self) = self.numerator / self.denominator

It's important that this conversion use the integer's "true"
division rather than casting one side to float before dividing
so that ratios of huge integers convert without overflowing.

```python
def __float__(self)
```

**Module:** [[Modules/numbers|numbers]]
**Class:** [[Classes/Rational|Rational]]
**Type:** Method
**Line:** 308
