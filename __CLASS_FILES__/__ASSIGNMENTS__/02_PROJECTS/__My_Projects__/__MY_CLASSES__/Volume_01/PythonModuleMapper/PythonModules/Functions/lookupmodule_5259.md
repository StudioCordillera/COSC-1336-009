---
type: function
name: lookupmodule
module: pdb
lineno: 2168
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: lookupmodule()

## Overview

Helper function for break/clear parsing -- may be overridden.

lookupmodule() translates (possibly incomplete) file or module name
into an absolute file name.

filename could be in format of:
    * an absolute path like '/path/to/file.py'
    * a relative path like 'file.py' or 'dir/file.py'
    * a module name like 'module' or 'package.module'

files and modules will be searched in sys.path.

```python
def lookupmodule(self, filename)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 2168

## Categories

- [[Taxonomy/public_method|public_method]]
