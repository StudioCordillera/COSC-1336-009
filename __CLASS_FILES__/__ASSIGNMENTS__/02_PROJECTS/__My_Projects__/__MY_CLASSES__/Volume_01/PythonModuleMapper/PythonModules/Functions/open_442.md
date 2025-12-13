---
type: function
name: open
module: bz2
lineno: 279
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: open()

## Overview

Open a bzip2-compressed file in binary or text mode.

The filename argument can be an actual filename (a str, bytes, or
PathLike object), or an existing file object to read from or write
to.

The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or
"ab" for binary mode, or "rt", "wt", "xt" or "at" for text mode.
The default mode is "rb", and the default compresslevel is 9.

For binary mode, this function is equivalent to the BZ2File
constructor: BZ2File(filename, mode, compresslevel). In this case,
the encoding, errors and newline arguments must not be provided.

For text mode, a BZ2File object is created, and wrapped in an
io.TextIOWrapper instance with the specified encoding, error
handling behavior, and line ending(s).

```python
def open(filename, mode, compresslevel, encoding, errors, newline)
```

**Module:** [[Modules/bz2|bz2]]
**Type:** Module-level function
**Line:** 279
