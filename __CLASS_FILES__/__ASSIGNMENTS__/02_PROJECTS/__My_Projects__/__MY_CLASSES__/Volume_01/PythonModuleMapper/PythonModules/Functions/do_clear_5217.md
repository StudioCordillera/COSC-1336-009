---
type: function
name: do_clear
module: pdb
lineno: 1381
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_clear()

## Overview

cl(ear) [filename:lineno | bpnumber ...]

With a space separated list of breakpoint numbers, clear
those breakpoints.  Without argument, clear all breaks (but
first ask confirmation).  With a filename:lineno argument,
clear all breaks at that line in that file.

```python
def do_clear(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1381

## Categories

- [[Taxonomy/public_method|public_method]]
