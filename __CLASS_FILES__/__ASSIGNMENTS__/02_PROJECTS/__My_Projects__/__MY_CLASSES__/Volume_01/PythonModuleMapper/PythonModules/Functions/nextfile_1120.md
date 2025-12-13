---
type: function
name: nextfile
module: fileinput
lineno: 101
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: nextfile()

## Overview

Close the current file so that the next iteration will read the first
line from the next file (if any); lines not read from the file will
not count towards the cumulative line count. The filename is not
changed until after the first line of the next file has been read.
Before the first line has been read, this function has no effect;
it cannot be used to skip the first file. After the last line of the
last file has been read, this function has no effect.

```python
def nextfile()
```

**Module:** [[Modules/fileinput|fileinput]]
**Type:** Module-level function
**Line:** 101
