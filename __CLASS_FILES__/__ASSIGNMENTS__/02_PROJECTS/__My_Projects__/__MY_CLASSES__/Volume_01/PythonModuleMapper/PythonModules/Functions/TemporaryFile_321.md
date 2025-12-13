---
type: function
name: TemporaryFile
module: tempfile
lineno: 610
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: TemporaryFile()

## Overview

Create and return a temporary file.
Arguments:
'prefix', 'suffix', 'dir' -- as for mkstemp.
'mode' -- the mode argument to io.open (default "w+b").
'buffering' -- the buffer size argument to io.open (default -1).
'encoding' -- the encoding argument to io.open (default None)
'newline' -- the newline argument to io.open (default None)
'errors' -- the errors argument to io.open (default None)
The file is created as mkstemp() would do it.

Returns an object with a file-like interface.  The file has no
name, and will cease to exist when it is closed.

```python
def TemporaryFile(mode, buffering, encoding, newline, suffix, prefix, dir)
```

**Module:** [[Modules/tempfile|tempfile]]
**Type:** Module-level function
**Line:** 610
