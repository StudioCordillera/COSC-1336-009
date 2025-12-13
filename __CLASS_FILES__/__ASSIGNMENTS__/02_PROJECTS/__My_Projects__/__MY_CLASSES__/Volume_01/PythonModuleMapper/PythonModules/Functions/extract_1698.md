---
type: function
name: extract
module: zipfile
lineno: 1758
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
as possible. `member' may be a filename or a ZipInfo object. You can
specify a different directory using `path'. You can specify the
password to decrypt the file using 'pwd'.

```python
def extract(self, member, path, pwd)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/ZipFile|ZipFile]]
**Type:** Method
**Line:** 1758

## Categories

- [[Taxonomy/public_method|public_method]]
