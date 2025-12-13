---
type: function
name: check_output
module: doctest
lineno: 1699
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: check_output()

## Overview

Return True iff the actual output from an example (`got`)
matches the expected output (`want`).  These strings are
always considered to match if they are identical; but
depending on what option flags the test runner is using,
several non-exact match types are also possible.  See the
documentation for `TestRunner` for more information about
option flags.

```python
def check_output(self, want, got, optionflags)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/OutputChecker|OutputChecker]]
**Type:** Method
**Line:** 1699

## Categories

- [[Taxonomy/public_method|public_method]]
