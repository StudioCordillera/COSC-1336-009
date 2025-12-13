---
type: function
name: cmpfiles
module: filecmp
lineno: 265
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: cmpfiles()

## Overview

Compare common files in two directories.

a, b -- directory names
common -- list of file names found in both directories
shallow -- if true, do comparison based solely on stat() information

Returns a tuple of three lists:
  files that compare equal
  files that are different
  filenames that aren't regular files.

```python
def cmpfiles(a, b, common, shallow)
```

**Module:** [[Modules/filecmp|filecmp]]
**Type:** Module-level function
**Line:** 265
