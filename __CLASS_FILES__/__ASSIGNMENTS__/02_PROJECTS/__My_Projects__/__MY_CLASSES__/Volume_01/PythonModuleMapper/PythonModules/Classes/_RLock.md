---
type: class
name: _RLock
module: threading
lineno: 141
tags:
  - python
  - class
---

# Class: _RLock

## Overview

This class implements reentrant lock objects.

A reentrant lock must be released by the thread that acquired it. Once a
thread has acquired a reentrant lock, the same thread may acquire it
again without blocking; the thread must release it once for each time it
has acquired it.

**Module:** [[Modules/threading|threading]]
**Line:** 141

## Methods

### Constructors
- [[Functions/__init___2514|__init__()]] (line 151)

### Magic Methods
- [[Functions/__repr___2515|__repr__()]] (line 156)
- [[Functions/__exit___2519|__exit__()]] (line 237)

### Methods
- [[Functions/_at_fork_reinit_2516|_at_fork_reinit()]] (line 171)
- [[Functions/acquire_2517|acquire()]] (line 176)
- [[Functions/release_2518|release()]] (line 214)
- [[Functions/_acquire_restore_2520|_acquire_restore()]] (line 242)
- [[Functions/_release_save_2521|_release_save()]] (line 246)
- [[Functions/_is_owned_2522|_is_owned()]] (line 256)
- [[Functions/_recursion_count_2523|_recursion_count()]] (line 261)
