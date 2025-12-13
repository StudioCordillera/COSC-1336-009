---
type: function
name: glob
module: glob
lineno: 16
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: glob()

## Overview

Return a list of paths matching a pathname pattern.

The pattern may contain simple shell-style wildcards a la
fnmatch. Unlike fnmatch, filenames starting with a
dot are special cases that are not matched by '*' and '?'
patterns by default.

If `include_hidden` is true, the patterns '*', '?', '**'  will match hidden
directories.

If `recursive` is true, the pattern '**' will match any files and
zero or more directories and subdirectories.

```python
def glob(pathname)
```

**Module:** [[Modules/glob|glob]]
**Type:** Module-level function
**Line:** 16
