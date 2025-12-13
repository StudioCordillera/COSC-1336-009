---
type: function
name: _exec_in_closure
module: pdb
lineno: 649
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _exec_in_closure()

## Overview

Run source code in closure so code object created within source
can find variables in locals correctly

returns True if the source is executed, False otherwise

```python
def _exec_in_closure(self, source, globals, locals)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 649

## Categories

- [[Taxonomy/protected_method|protected_method]]
