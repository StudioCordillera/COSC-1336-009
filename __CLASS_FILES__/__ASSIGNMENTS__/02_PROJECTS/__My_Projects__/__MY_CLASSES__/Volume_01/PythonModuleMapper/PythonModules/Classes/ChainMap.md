---
type: class
name: ChainMap
module: collections
lineno: 989
tags:
  - python
  - class
---

# Class: ChainMap

## Overview

A ChainMap groups multiple dicts (or other mappings) together
to create a single, updateable view.

The underlying mappings are stored in a list.  That list is public and can
be accessed or updated using the *maps* attribute.  There is no other
state.

Lookups search the underlying mappings successively until a key is found.
In contrast, writes, updates, and deletions only operate on the first
mapping.

**Module:** [[Modules/collections|collections]]
**Line:** 989

## Methods

### Constructors
- [[Functions/__init___265|__init__()]] (line 1003)

### Magic Methods
- [[Functions/__missing___266|__missing__()]] (line 1010)
- [[Functions/__getitem___267|__getitem__()]] (line 1013)
- [[Functions/__len___269|__len__()]] (line 1024)
- [[Functions/__iter___270|__iter__()]] (line 1027)
- [[Functions/__contains___271|__contains__()]] (line 1033)
- [[Functions/__bool___272|__bool__()]] (line 1036)
- [[Functions/__repr___273|__repr__()]] (line 1040)
- [[Functions/__setitem___278|__setitem__()]] (line 1070)
- [[Functions/__delitem___279|__delitem__()]] (line 1073)
- [[Functions/__ior___283|__ior__()]] (line 1097)
- [[Functions/__or___284|__or__()]] (line 1101)
- [[Functions/__ror___285|__ror__()]] (line 1108)

### Methods
- [[Functions/get_268|get()]] (line 1021)
- [[Functions/fromkeys_274|fromkeys()]] (line 1044)
- [[Functions/copy_275|copy()]] (line 1048)
- [[Functions/new_child_276|new_child()]] (line 1054)
- [[Functions/parents_277|parents()]] (line 1066)
- [[Functions/popitem_280|popitem()]] (line 1079)
- [[Functions/pop_281|pop()]] (line 1086)
- [[Functions/clear_282|clear()]] (line 1093)
