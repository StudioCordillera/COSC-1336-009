---
type: function
name: writestr
module: zipfile
lineno: 1910
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: writestr()

## Overview

Write a file into the archive.  The contents is 'data', which
may be either a 'str' or a 'bytes' instance; if it is a 'str',
it is encoded as UTF-8 first.
'zinfo_or_arcname' is either a ZipInfo instance or
the name of the file in the archive.

```python
def writestr(self, zinfo_or_arcname, data, compress_type, compresslevel)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/ZipFile|ZipFile]]
**Type:** Method
**Line:** 1910

## Categories

- [[Taxonomy/public_method|public_method]]
