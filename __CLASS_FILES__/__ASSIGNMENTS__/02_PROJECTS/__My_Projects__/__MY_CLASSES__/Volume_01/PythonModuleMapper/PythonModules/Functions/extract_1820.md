---
type: function
name: extract
module: tarfile
lineno: 2395
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: extract()

## Overview

Extract a member from the archive to the current working directory,
using its full name. Its file information is extracted as accurately
as possible. `member' may be a filename or a TarInfo object. You can
specify a different directory using `path'. File attributes (owner,
mtime, mode) are set unless `set_attrs' is False. If `numeric_owner`
is True, only the numbers for user/group names are used and not
the names.

The `filter` function will be called before extraction.
It can return a changed TarInfo or None to skip the member.
String names of common filters are accepted.

```python
def extract(self, member, path, set_attrs)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2395

## Categories

- [[Taxonomy/public_method|public_method]]
