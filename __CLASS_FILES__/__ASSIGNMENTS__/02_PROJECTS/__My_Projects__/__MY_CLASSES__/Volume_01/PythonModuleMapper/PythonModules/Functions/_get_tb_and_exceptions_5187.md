---
type: function
name: _get_tb_and_exceptions
module: pdb
lineno: 547
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_tb_and_exceptions()

## Overview

Given a tracecack or an exception, return a tuple of chained exceptions
and current traceback to inspect.

This will deal with selecting the right ``__cause__`` or ``__context__``
as well as handling cycles, and return a flattened list of exceptions we
can jump to with do_exceptions.

```python
def _get_tb_and_exceptions(self, tb_or_exc)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 547

## Categories

- [[Taxonomy/accessor|accessor]]
