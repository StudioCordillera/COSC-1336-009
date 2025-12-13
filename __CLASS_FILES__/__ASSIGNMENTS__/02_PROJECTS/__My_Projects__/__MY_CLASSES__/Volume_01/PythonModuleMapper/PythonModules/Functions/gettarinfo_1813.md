---
type: function
name: gettarinfo
module: tarfile
lineno: 2077
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: gettarinfo()

## Overview

Create a TarInfo object from the result of os.stat or equivalent
on an existing file. The file is either named by `name', or
specified as a file object `fileobj' with a file descriptor. If
given, `arcname' specifies an alternative name for the file in the
archive, otherwise, the name is taken from the 'name' attribute of
'fileobj', or the 'name' argument. The name should be a text
string.

```python
def gettarinfo(self, name, arcname, fileobj)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2077

## Categories

- [[Taxonomy/public_method|public_method]]
