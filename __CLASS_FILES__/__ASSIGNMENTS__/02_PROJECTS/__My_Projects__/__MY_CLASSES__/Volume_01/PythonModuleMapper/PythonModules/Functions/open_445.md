---
type: function
name: open
module: lzma
lineno: 279
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: open()

## Overview

Open an LZMA-compressed file in binary or text mode.

filename can be either an actual file name (given as a str, bytes,
or PathLike object), in which case the named file is opened, or it
can be an existing file object to read from or write to.

The mode argument can be "r", "rb" (default), "w", "wb", "x", "xb",
"a", or "ab" for binary mode, or "rt", "wt", "xt", or "at" for text
mode.

The format, check, preset and filters arguments specify the
compression settings, as for LZMACompressor, LZMADecompressor and
LZMAFile.

For binary mode, this function is equivalent to the LZMAFile
constructor: LZMAFile(filename, mode, ...). In this case, the
encoding, errors and newline arguments must not be provided.

For text mode, an LZMAFile object is created, and wrapped in an
io.TextIOWrapper instance with the specified encoding, error
handling behavior, and line ending(s).

```python
def open(filename, mode)
```

**Module:** [[Modules/lzma|lzma]]
**Type:** Module-level function
**Line:** 279
