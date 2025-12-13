---
type: class
name: BoundedSemaphore
module: threading
lineno: 536
tags:
  - python
  - class
---

# Class: BoundedSemaphore

## Overview

Implements a bounded semaphore.

A bounded semaphore checks to make sure its current value doesn't exceed its
initial value. If it does, ValueError is raised. In most situations
semaphores are used to guard resources with limited capacity.

If the semaphore is released too many times it's a sign of a bug. If not
given, value defaults to 1.

Like regular semaphores, bounded semaphores manage a counter representing
the number of release() calls minus the number of acquire() calls, plus an
initial value. The acquire() method blocks if necessary until it can return
without making the counter negative. If not given, value defaults to 1.

**Module:** [[Modules/threading|threading]]
**Line:** 536

## Inheritance

**Inherits from:**
- [[Classes/Semaphore|Semaphore]]

## Methods

### Constructors
- [[Functions/__init___2542|__init__()]] (line 553)

### Magic Methods
- [[Functions/__repr___2543|__repr__()]] (line 557)

### Methods
- [[Functions/release_2544|release()]] (line 562)
