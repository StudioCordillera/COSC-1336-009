---
type: function
name: set_trace
module: pdb
lineno: 2336
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - mutator
---

# Function: set_trace()

## Overview

Enter the debugger at the calling stack frame.

This is useful to hard-code a breakpoint at a given point in a
program, even if the code is not otherwise being debugged (e.g. when
an assertion fails). If given, *header* is printed to the console
just before debugging begins.

```python
def set_trace()
```

**Module:** [[Modules/pdb|pdb]]
**Type:** Module-level function
**Line:** 2336

## Categories

- [[Taxonomy/mutator|mutator]]
