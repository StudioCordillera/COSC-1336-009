---
type: function
name: from_file
module: zipfile
lineno: 569
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: from_file()

## Overview

Construct an appropriate ZipInfo for a file on the filesystem.

filename should be the path to a file or directory on the filesystem.

arcname is the name which it will have within the archive (by default,
this will be the same as filename, but without a drive letter and with
leading path separators removed).

```python
@classmethod
def from_file(cls, filename, arcname)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/ZipInfo|ZipInfo]]
**Type:** Method
**Line:** 569

## Categories

- [[Taxonomy/public_method|public_method]]
