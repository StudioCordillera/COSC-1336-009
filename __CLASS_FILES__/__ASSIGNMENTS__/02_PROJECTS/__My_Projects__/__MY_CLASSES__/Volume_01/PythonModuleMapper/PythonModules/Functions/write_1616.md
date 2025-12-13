---
type: function
name: write
module: lzma
lineno: 232
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

Write a bytes object to the file.

Returns the number of uncompressed bytes written, which is
always the length of data in bytes. Note that due to buffering,
the file on disk may not reflect the data written until close()
is called.

```python
def write(self, data)
```

**Module:** [[Modules/lzma|lzma]]
**Class:** [[Classes/LZMAFile|LZMAFile]]
**Type:** Method
**Line:** 232

## Categories

- [[Taxonomy/public_method|public_method]]
