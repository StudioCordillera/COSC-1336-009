---
type: function
name: _basename
module: shutil
lineno: 796
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _basename()

## Overview

A basename() variant which first strips the trailing slash, if present.
Thus we always get the last component of the path, even for directories.

path: Union[PathLike, str]

e.g.
>>> os.path.basename('/bar/foo')
'foo'
>>> os.path.basename('/bar/foo/')
''
>>> _basename('/bar/foo/')
'foo'

```python
def _basename(path)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 796
