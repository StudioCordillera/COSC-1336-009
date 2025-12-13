---
type: function
name: extractall
module: tarfile
lineno: 2322
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: extractall()

## Overview

Extract all members from the archive to the current working
directory and set owner, modification time and permissions on
directories afterwards. `path' specifies a different directory
to extract to. `members' is optional and must be a subset of the
list returned by getmembers(). If `numeric_owner` is True, only
the numbers for user/group names are used and not the names.

The `filter` function will be called on each member just
before extraction.
It can return a changed TarInfo or None to skip the member.
String names of common filters are accepted.

```python
def extractall(self, path, members)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2322

## Categories

- [[Taxonomy/public_method|public_method]]
