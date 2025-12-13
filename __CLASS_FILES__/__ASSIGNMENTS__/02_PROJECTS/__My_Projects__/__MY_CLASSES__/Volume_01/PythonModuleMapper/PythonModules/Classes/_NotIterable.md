---
type: class
name: _NotIterable
module: typing
lineno: 516
tags:
  - python
  - class
---

# Class: _NotIterable

## Overview

Mixin to prevent iteration, without being compatible with Iterable.

That is, we could do::

    def __iter__(self): raise TypeError()

But this would make users of this mixin duck type-compatible with
collections.abc.Iterable - isinstance(foo, Iterable) would be True.

Luckily, we can instead prevent iteration by setting __iter__ to None, which
is treated specially.

**Module:** [[Modules/typing|typing]]
**Line:** 516

## Inheritance

**Subclasses:**
- [[Classes/_SpecialForm|_SpecialForm]]
- [[Classes/_SpecialGenericAlias|_SpecialGenericAlias]]
- [[Classes/_CallableGenericAlias|_CallableGenericAlias]]
- [[Classes/_UnionGenericAlias|_UnionGenericAlias]]
- [[Classes/_AnnotatedAlias|_AnnotatedAlias]]
