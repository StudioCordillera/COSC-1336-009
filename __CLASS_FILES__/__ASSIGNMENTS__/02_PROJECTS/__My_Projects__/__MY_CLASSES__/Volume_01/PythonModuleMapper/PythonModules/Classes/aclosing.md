---
type: class
name: aclosing
module: contextlib
lineno: 367
tags:
  - python
  - class
---

# Class: aclosing

## Overview

Async context manager for safely finalizing an asynchronously cleaned-up
resource such as an async generator, calling its ``aclose()`` method.

Code like this:

    async with aclosing(<module>.fetch(<arguments>)) as agen:
        <block>

is equivalent to this:

    agen = <module>.fetch(<arguments>)
    try:
        <block>
    finally:
        await agen.aclose()

**Module:** [[Modules/contextlib|contextlib]]
**Line:** 367

## Inheritance

**Inherits from:**
- [[Classes/AbstractAsyncContextManager|AbstractAsyncContextManager]]

## Methods

### Constructors
- [[Functions/__init___5551|__init__()]] (line 385)

### Magic Methods
- [[Functions/__aenter___5552|__aenter__()]] (line 387)
- [[Functions/__aexit___5553|__aexit__()]] (line 389)
