---
type: function
name: _replace_convenience_variables
module: pdb
lineno: 781
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _replace_convenience_variables()

## Overview

Replace the convenience variables in 'line' with their values.
e.g. $foo is replaced by __pdb_convenience_variables["foo"].
Note: such pattern in string literals will be skipped

```python
def _replace_convenience_variables(self, line)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 781

## Categories

- [[Taxonomy/protected_method|protected_method]]
