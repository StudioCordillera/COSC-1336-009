---
type: class
name: _AnnotatedAlias
module: typing
lineno: 2215
tags:
  - python
  - class
---

# Class: _AnnotatedAlias

## Overview

Runtime representation of an annotated type.

At its core 'Annotated[t, dec1, dec2, ...]' is an alias for the type 't'
with extra annotations. The alias behaves like a normal typing alias.
Instantiating is the same as instantiating the underlying type; binding
it to types is also the same.

The metadata itself is stored in a '__metadata__' attribute as a tuple.

**Module:** [[Modules/typing|typing]]
**Line:** 2215

## Inheritance

**Inherits from:**
- [[Classes/_NotIterable|_NotIterable]]
- [[Classes/_GenericAlias|_GenericAlias]]

## Methods

### Constructors
- [[Functions/__init___4765|__init__()]] (line 2226)

### Magic Methods
- [[Functions/__repr___4767|__repr__()]] (line 2238)
- [[Functions/__reduce___4768|__reduce__()]] (line 2244)
- [[Functions/__eq___4769|__eq__()]] (line 2249)
- [[Functions/__hash___4770|__hash__()]] (line 2255)
- [[Functions/__getattr___4771|__getattr__()]] (line 2258)
- [[Functions/__mro_entries___4772|__mro_entries__()]] (line 2263)

### Methods
- [[Functions/copy_with_4766|copy_with()]] (line 2233)
