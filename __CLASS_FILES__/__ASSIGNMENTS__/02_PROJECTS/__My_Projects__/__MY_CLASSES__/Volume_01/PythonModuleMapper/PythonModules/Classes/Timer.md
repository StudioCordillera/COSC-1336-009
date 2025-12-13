---
type: class
name: Timer
module: timeit
lineno: 86
tags:
  - python
  - class
---

# Class: Timer

## Overview

Class for timing execution speed of small code snippets.

The constructor takes a statement to be timed, an additional
statement used for setup, and a timer function.  Both statements
default to 'pass'; the timer function is platform-dependent (see
module doc string).  If 'globals' is specified, the code will be
executed within that namespace (as opposed to inside timeit's
namespace).

To measure the execution time of the first statement, use the
timeit() method.  The repeat() method is a convenience to call
timeit() multiple times and return a list of results.

The statements may contain newlines, as long as they don't contain
multi-line string literals.

**Module:** [[Modules/timeit|timeit]]
**Line:** 86

## Methods

### Constructors
- [[Functions/__init___5278|__init__()]] (line 104)

### Methods
- [[Functions/print_exc_5279|print_exc()]] (line 139)
- [[Functions/timeit_5280|timeit()]] (line 166)
- [[Functions/repeat_5281|repeat()]] (line 186)
- [[Functions/autorange_5282|autorange()]] (line 212)
