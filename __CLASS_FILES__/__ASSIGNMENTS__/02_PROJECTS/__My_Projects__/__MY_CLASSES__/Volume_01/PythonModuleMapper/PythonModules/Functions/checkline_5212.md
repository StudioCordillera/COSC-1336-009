---
type: function
name: checkline
module: pdb
lineno: 1245
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: checkline()

## Overview

Check whether specified line seems to be executable.

Return `lineno` if it is, 0 if not (e.g. a docstring, comment, blank
line or EOF). Warning: testing is not comprehensive.

```python
def checkline(self, filename, lineno)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 1245

## Categories

- [[Taxonomy/public_method|public_method]]
