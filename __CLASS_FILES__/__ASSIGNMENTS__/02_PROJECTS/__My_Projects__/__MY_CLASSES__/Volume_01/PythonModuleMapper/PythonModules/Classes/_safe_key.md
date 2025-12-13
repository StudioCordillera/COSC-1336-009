---
type: class
name: _safe_key
module: pprint
lineno: 80
tags:
  - python
  - class
---

# Class: _safe_key

## Overview

Helper function for key functions when sorting unorderable objects.

The wrapped-object will fallback to a Py2.x style comparison for
unorderable types (sorting first comparing the type name and then by
the obj ids).  Does not work recursively, so dict.items() must have
_safe_key applied to both the key and the value.

**Module:** [[Modules/pprint|pprint]]
**Line:** 80

## Methods

### Constructors
- [[Functions/__init___559|__init__()]] (line 92)

### Magic Methods
- [[Functions/__lt___560|__lt__()]] (line 95)
