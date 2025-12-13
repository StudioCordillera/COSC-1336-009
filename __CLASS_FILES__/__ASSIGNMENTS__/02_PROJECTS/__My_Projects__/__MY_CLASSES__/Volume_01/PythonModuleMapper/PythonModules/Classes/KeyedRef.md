---
type: class
name: KeyedRef
module: weakref
lineno: 335
tags:
  - python
  - class
---

# Class: KeyedRef

## Overview

Specialized reference that includes a key corresponding to the value.

This is used in the WeakValueDictionary to avoid having to create
a function object for each key stored in the mapping.  A shared
callback object can use the 'key' attribute of a KeyedRef instead
of getting a reference to the key from an enclosing scope.

**Module:** [[Modules/weakref|weakref]]
**Line:** 335

## Methods

### Constructors
- [[Functions/__new___478|__new__()]] (line 347)
- [[Functions/__init___479|__init__()]] (line 352)
