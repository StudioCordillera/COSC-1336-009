---
type: class
name: Barrier
module: threading
lineno: 674
tags:
  - python
  - class
---

# Class: Barrier

## Overview

Implements a Barrier.

Useful for synchronizing a fixed number of threads at known synchronization
points.  Threads block on 'wait()' and are simultaneously awoken once they
have all made that call.

**Module:** [[Modules/threading|threading]]
**Line:** 674

## Methods

### Constructors
- [[Functions/__init___2553|__init__()]] (line 683)

### Magic Methods
- [[Functions/__repr___2554|__repr__()]] (line 701)

### Methods
- [[Functions/wait_2555|wait()]] (line 708)
- [[Functions/_enter_2556|_enter()]] (line 738)
- [[Functions/_release_2557|_release()]] (line 749)
- [[Functions/_wait_2558|_wait()]] (line 763)
- [[Functions/_exit_2559|_exit()]] (line 774)
- [[Functions/reset_2560|reset()]] (line 781)
- [[Functions/abort_2561|abort()]] (line 801)
- [[Functions/_break_2562|_break()]] (line 811)
- [[Functions/parties_2563|parties()]] (line 818)
- [[Functions/n_waiting_2564|n_waiting()]] (line 823)
- [[Functions/broken_2565|broken()]] (line 832)
