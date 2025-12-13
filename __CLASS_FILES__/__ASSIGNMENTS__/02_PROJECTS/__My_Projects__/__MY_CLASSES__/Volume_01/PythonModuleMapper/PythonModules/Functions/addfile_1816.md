---
type: function
name: addfile
module: tarfile
lineno: 2270
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: addfile()

## Overview

Add the TarInfo object `tarinfo' to the archive. If `tarinfo' represents
a non zero-size regular file, the `fileobj' argument should be a binary file,
and tarinfo.size bytes are read from it and added to the archive.
You can create TarInfo objects directly, or by using gettarinfo().

```python
def addfile(self, tarinfo, fileobj)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2270

## Categories

- [[Taxonomy/public_method|public_method]]
