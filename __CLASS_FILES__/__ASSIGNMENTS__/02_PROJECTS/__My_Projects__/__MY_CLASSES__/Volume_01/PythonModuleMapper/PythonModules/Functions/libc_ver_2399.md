---
type: function
name: libc_ver
module: platform
lineno: 161
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: libc_ver()

## Overview

Tries to determine the libc version that the file executable
(which defaults to the Python interpreter) is linked against.

Returns a tuple of strings (lib,version) which default to the
given parameters in case the lookup fails.

Note that the function has intimate knowledge of how different
libc versions add symbols to the executable and thus is probably
only usable for executables compiled using gcc.

The file is read and scanned in chunks of chunksize bytes.

```python
def libc_ver(executable, lib, version, chunksize)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 161
