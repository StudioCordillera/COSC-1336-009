---
type: function
name: do_exceptions
module: pdb
lineno: 1456
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_exceptions()

## Overview

exceptions [number]

List or change current exception in an exception chain.

Without arguments, list all the current exception in the exception
chain. Exceptions will be numbered, with the current exception indicated
with an arrow.

If given an integer as argument, switch to the exception at that index.

```python
def do_exceptions(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1456

## Categories

- [[Taxonomy/public_method|public_method]]
