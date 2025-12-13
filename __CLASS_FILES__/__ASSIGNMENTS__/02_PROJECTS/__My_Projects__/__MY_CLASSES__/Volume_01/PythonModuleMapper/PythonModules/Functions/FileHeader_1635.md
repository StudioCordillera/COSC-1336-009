---
type: function
name: FileHeader
module: zipfile
lineno: 469
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: FileHeader()

## Overview

Return the per-file header as a bytes object.

When the optional zip64 arg is None rather than a bool, we will
decide based upon the file_size and compress_size, if known,
False otherwise.

```python
def FileHeader(self, zip64)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/ZipInfo|ZipInfo]]
**Type:** Method
**Line:** 469

## Categories

- [[Taxonomy/public_method|public_method]]
