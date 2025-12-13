---
type: function
name: fnmatch
module: fnmatch
lineno: 19
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: fnmatch()

## Overview

Test whether FILENAME matches PATTERN.

Patterns are Unix shell style:

*       matches everything
?       matches any single character
[seq]   matches any character in seq
[!seq]  matches any char not in seq

An initial period in FILENAME is not special.
Both FILENAME and PATTERN are first case-normalized
if the operating system requires it.
If you don't want this, use fnmatchcase(FILENAME, PATTERN).

```python
def fnmatch(name, pat)
```

**Module:** [[Modules/fnmatch|fnmatch]]
**Type:** Module-level function
**Line:** 19
