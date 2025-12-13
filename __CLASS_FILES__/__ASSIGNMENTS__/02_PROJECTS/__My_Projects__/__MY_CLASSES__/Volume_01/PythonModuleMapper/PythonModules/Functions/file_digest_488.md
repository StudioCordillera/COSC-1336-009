---
type: function
name: file_digest
module: hashlib
lineno: 195
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: file_digest()

## Overview

Hash the contents of a file-like object. Returns a digest object.

*fileobj* must be a file-like object opened for reading in binary mode.
It accepts file objects from open(), io.BytesIO(), and SocketIO objects.
The function may bypass Python's I/O and use the file descriptor *fileno*
directly.

*digest* must either be a hash algorithm name as a *str*, a hash
constructor, or a callable that returns a hash object.

```python
def file_digest()
```

**Module:** [[Modules/hashlib|hashlib]]
**Type:** Module-level function
**Line:** 195
