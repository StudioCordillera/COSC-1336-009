---
type: class
name: finalize
module: weakref
lineno: 540
tags:
  - python
  - class
---

# Class: finalize

## Overview

Class for finalization of weakrefable objects

finalize(obj, func, *args, **kwargs) returns a callable finalizer
object which will be called when obj is garbage collected. The
first time the finalizer is called it evaluates func(*arg, **kwargs)
and returns the result. After this the finalizer is dead, and
calling it just returns None.

When the program exits any remaining finalizers for which the
atexit attribute is true will be run in reverse order of creation.
By default atexit is true.

**Module:** [[Modules/weakref|weakref]]
**Line:** 540

## Methods

### Constructors
- [[Functions/__init___503|__init__()]] (line 568)

### Magic Methods
- [[Functions/__call___504|__call__()]] (line 585)
- [[Functions/__repr___509|__repr__()]] (line 625)

### Methods
- [[Functions/detach_505|detach()]] (line 592)
- [[Functions/peek_506|peek()]] (line 600)
- [[Functions/alive_507|alive()]] (line 609)
- [[Functions/atexit_508|atexit()]] (line 620)
- [[Functions/_select_for_exit_510|_select_for_exit()]] (line 635)
- [[Functions/_exitfunc_511|_exitfunc()]] (line 642)
