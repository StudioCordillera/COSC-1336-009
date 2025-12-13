---
type: function
name: write
module: bz2
lineno: 222
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write()

## Overview

Write a byte string to the file.

Returns the number of uncompressed bytes written, which is
always the length of data in bytes. Note that due to buffering,
the file on disk may not reflect the data written until close()
is called.

```python
def write(self, data)
```

**Module:** [[Modules/bz2|bz2]]
**Class:** [[Classes/BZ2File|BZ2File]]
**Type:** Method
**Line:** 222

## Categories

- [[Taxonomy/public_method|public_method]]
