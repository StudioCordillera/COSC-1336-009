---
type: class
name: itemgetter
module: operator
lineno: 271
tags:
  - python
  - class
---

# Class: itemgetter

## Overview

Return a callable object that fetches the given item(s) from its operand.
After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

**Module:** [[Modules/operator|operator]]
**Line:** 271

## Methods

### Constructors
- [[Functions/__init___1096|__init__()]] (line 279)

### Magic Methods
- [[Functions/__call___1097|__call__()]] (line 291)
- [[Functions/__repr___1098|__repr__()]] (line 294)
- [[Functions/__reduce___1099|__reduce__()]] (line 299)
