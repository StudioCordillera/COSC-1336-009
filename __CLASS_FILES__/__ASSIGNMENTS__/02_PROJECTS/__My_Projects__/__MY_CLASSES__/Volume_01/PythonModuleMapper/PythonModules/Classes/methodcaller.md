---
type: class
name: methodcaller
module: operator
lineno: 302
tags:
  - python
  - class
---

# Class: methodcaller

## Overview

Return a callable object that calls the given method on its operand.
After f = methodcaller('name'), the call f(r) returns r.name().
After g = methodcaller('name', 'date', foo=1), the call g(r) returns
r.name('date', foo=1).

**Module:** [[Modules/operator|operator]]
**Line:** 302

## Methods

### Constructors
- [[Functions/__init___1100|__init__()]] (line 311)

### Magic Methods
- [[Functions/__call___1101|__call__()]] (line 318)
- [[Functions/__repr___1102|__repr__()]] (line 321)
- [[Functions/__reduce___1103|__reduce__()]] (line 329)
