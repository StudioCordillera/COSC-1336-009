---
type: class
name: catch_warnings
module: warnings
lineno: 442
tags:
  - python
  - class
---

# Class: catch_warnings

## Overview

A context manager that copies and restores the warnings filter upon
exiting the context.

The 'record' argument specifies whether warnings should be captured by a
custom implementation of warnings.showwarning() and be appended to a list
returned by the context manager. Otherwise None is returned by the context
manager. The objects appended to the list are arguments whose attributes
mirror the arguments to showwarning().

The 'module' argument is to specify an alternative module to the module
named 'warnings' and imported under that name. This argument is only useful
when testing the warnings module itself.

If the 'action' argument is not None, the remaining arguments are passed
to warnings.simplefilter() as if it were called immediately on entering the
context.

**Module:** [[Modules/warnings|warnings]]
**Line:** 442

## Methods

### Constructors
- [[Functions/__init___5472|__init__()]] (line 462)

### Magic Methods
- [[Functions/__repr___5473|__repr__()]] (line 479)
- [[Functions/__enter___5474|__enter__()]] (line 488)
- [[Functions/__exit___5475|__exit__()]] (line 509)
