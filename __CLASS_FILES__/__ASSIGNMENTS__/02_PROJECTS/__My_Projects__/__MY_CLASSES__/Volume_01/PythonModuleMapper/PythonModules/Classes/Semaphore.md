---
type: class
name: Semaphore
module: threading
lineno: 449
tags:
  - python
  - class
---

# Class: Semaphore

## Overview

This class implements semaphore objects.

Semaphores manage a counter representing the number of release() calls minus
the number of acquire() calls, plus an initial value. The acquire() method
blocks if necessary until it can return without making the counter
negative. If not given, value defaults to 1.

**Module:** [[Modules/threading|threading]]
**Line:** 449

## Inheritance

**Subclasses:**
- [[Classes/BoundedSemaphore|BoundedSemaphore]]

## Methods

### Constructors
- [[Functions/__init___2537|__init__()]] (line 461)

### Magic Methods
- [[Functions/__repr___2538|__repr__()]] (line 467)
- [[Functions/__exit___2541|__exit__()]] (line 532)

### Methods
- [[Functions/acquire_2539|acquire()]] (line 472)
- [[Functions/release_2540|release()]] (line 519)
