---
type: class
name: Condition
module: threading
lineno: 269
tags:
  - python
  - class
---

# Class: Condition

## Overview

Class that implements a condition variable.

A condition variable allows one or more threads to wait until they are
notified by another thread.

If the lock argument is given and not None, it must be a Lock or RLock
object, and it is used as the underlying lock. Otherwise, a new RLock object
is created and used as the underlying lock.

**Module:** [[Modules/threading|threading]]
**Line:** 269

## Methods

### Constructors
- [[Functions/__init___2524|__init__()]] (line 281)

### Magic Methods
- [[Functions/__enter___2526|__enter__()]] (line 303)
- [[Functions/__exit___2527|__exit__()]] (line 306)
- [[Functions/__repr___2528|__repr__()]] (line 309)

### Methods
- [[Functions/_at_fork_reinit_2525|_at_fork_reinit()]] (line 299)
- [[Functions/_release_save_2529|_release_save()]] (line 312)
- [[Functions/_acquire_restore_2530|_acquire_restore()]] (line 315)
- [[Functions/_is_owned_2531|_is_owned()]] (line 318)
- [[Functions/wait_2532|wait()]] (line 327)
- [[Functions/wait_for_2533|wait_for()]] (line 375)
- [[Functions/notify_2534|notify()]] (line 398)
- [[Functions/notify_all_2535|notify_all()]] (line 428)
- [[Functions/notifyAll_2536|notifyAll()]] (line 437)
