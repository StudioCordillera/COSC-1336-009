---
type: function
name: extractfile
module: tarfile
lineno: 2484
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: extractfile()

## Overview

Extract a member from the archive as a file object. `member' may be
a filename or a TarInfo object. If `member' is a regular file or
a link, an io.BufferedReader object is returned. For all other
existing members, None is returned. If `member' does not appear
in the archive, KeyError is raised.

```python
def extractfile(self, member)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2484

## Categories

- [[Taxonomy/public_method|public_method]]
