---
type: function
name: do_break
module: pdb
lineno: 1093
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_break()

## Overview

b(reak) [ ([filename:]lineno | function) [, condition] ]

Without argument, list all breaks.

With a line number argument, set a break at this line in the
current file.  With a function name, set a break at the first
executable line of that function.  If a second argument is
present, it is a string specifying an expression which must
evaluate to true before the breakpoint is honored.

The line number may be prefixed with a filename and a colon,
to specify a breakpoint in another file (probably one that
hasn't been loaded yet).  The file is searched for on
sys.path; the .py suffix may be omitted.

```python
def do_break(self, arg, temporary)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1093

## Categories

- [[Taxonomy/public_method|public_method]]
