---
type: class
name: closing
module: contextlib
lineno: 342
tags:
  - python
  - class
---

# Class: closing

## Overview

Context to automatically close something at the end of a block.

Code like this:

    with closing(<module>.open(<arguments>)) as f:
        <block>

is equivalent to this:

    f = <module>.open(<arguments>)
    try:
        <block>
    finally:
        f.close()

**Module:** [[Modules/contextlib|contextlib]]
**Line:** 342

## Inheritance

**Inherits from:**
- [[Classes/AbstractContextManager|AbstractContextManager]]

## Methods

### Constructors
- [[Functions/__init___5548|__init__()]] (line 359)

### Magic Methods
- [[Functions/__enter___5549|__enter__()]] (line 361)
- [[Functions/__exit___5550|__exit__()]] (line 363)
