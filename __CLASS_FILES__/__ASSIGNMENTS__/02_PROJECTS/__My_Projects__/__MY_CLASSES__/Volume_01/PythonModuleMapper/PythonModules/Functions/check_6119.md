---
type: function
name: check
module: tabnanny
lineno: 72
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: check()

## Overview

check(file_or_dir)

If file_or_dir is a directory and not a symbolic link, then recursively
descend the directory tree named by file_or_dir, checking all .py files
along the way. If file_or_dir is an ordinary Python source file, it is
checked for whitespace related problems. The diagnostic messages are
written to standard output using the print statement.

```python
def check(file)
```

**Module:** [[Modules/tabnanny|tabnanny]]
**Type:** Module-level function
**Line:** 72
