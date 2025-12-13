---
type: function
name: iglob
module: glob
lineno: 34
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: iglob()

## Overview

Return an iterator which yields the paths matching a pathname pattern.

The pattern may contain simple shell-style wildcards a la
fnmatch. However, unlike fnmatch, filenames starting with a
dot are special cases that are not matched by '*' and '?'
patterns.

If recursive is true, the pattern '**' will match any files and
zero or more directories and subdirectories.

```python
def iglob(pathname)
```

**Module:** [[Modules/glob|glob]]
**Type:** Module-level function
**Line:** 34
