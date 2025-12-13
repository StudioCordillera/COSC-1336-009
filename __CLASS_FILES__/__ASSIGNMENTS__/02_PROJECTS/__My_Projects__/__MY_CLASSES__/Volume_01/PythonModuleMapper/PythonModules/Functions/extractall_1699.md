---
type: function
name: extractall
module: zipfile
lineno: 1772
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
directory. `path' specifies a different directory to extract to.
`members' is optional and must be a subset of the list returned
by namelist(). You can specify the password to decrypt all files
using 'pwd'.

```python
def extractall(self, path, members, pwd)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/ZipFile|ZipFile]]
**Type:** Method
**Line:** 1772

## Categories

- [[Taxonomy/public_method|public_method]]
