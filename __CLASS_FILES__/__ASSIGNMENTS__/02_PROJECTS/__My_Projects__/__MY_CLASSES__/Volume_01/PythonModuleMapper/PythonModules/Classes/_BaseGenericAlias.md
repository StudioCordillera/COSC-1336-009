---
type: class
name: _BaseGenericAlias
module: typing
lineno: 1297
tags:
  - python
  - class
---

# Class: _BaseGenericAlias

## Overview

The central part of the internal API.

This represents a generic version of type 'origin' with type arguments 'params'.
There are two kind of these aliases: user defined and special. The special ones
are wrappers around builtin collections and ABCs in collections.abc. These must
have 'name' always set. If 'inst' is False, then the alias can't be instantiated;
this is used by e.g. typing.List and typing.Dict.

**Module:** [[Modules/typing|typing]]
**Line:** 1297

## Inheritance

**Inherits from:**
- [[Classes/_Final|_Final]]

**Subclasses:**
- [[Classes/_GenericAlias|_GenericAlias]]
- [[Classes/_SpecialGenericAlias|_SpecialGenericAlias]]

## Methods

### Constructors
- [[Functions/__init___4698|__init__()]] (line 1307)

### Magic Methods
- [[Functions/__call___4699|__call__()]] (line 1313)
- [[Functions/__mro_entries___4700|__mro_entries__()]] (line 1326)
- [[Functions/__getattr___4701|__getattr__()]] (line 1358)
- [[Functions/__setattr___4702|__setattr__()]] (line 1368)
- [[Functions/__instancecheck___4703|__instancecheck__()]] (line 1374)
- [[Functions/__subclasscheck___4704|__subclasscheck__()]] (line 1377)
- [[Functions/__dir___4705|__dir__()]] (line 1381)
