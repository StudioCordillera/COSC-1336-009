---
type: class
name: ExitStack
module: contextlib
lineno: 557
tags:
  - python
  - class
---

# Class: ExitStack

## Overview

Context manager for dynamic management of a stack of exit callbacks.

For example:
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in filenames]
        # All opened files will automatically be closed at the end of
        # the with statement, even if attempts to open files later
        # in the list raise an exception.

**Module:** [[Modules/contextlib|contextlib]]
**Line:** 557

## Inheritance

**Inherits from:**
- [[Classes/_BaseExitStack|_BaseExitStack]]
- [[Classes/AbstractContextManager|AbstractContextManager]]

## Methods

### Magic Methods
- [[Functions/__enter___5569|__enter__()]] (line 568)
- [[Functions/__exit___5570|__exit__()]] (line 571)

### Methods
- [[Functions/close_5571|close()]] (line 625)
