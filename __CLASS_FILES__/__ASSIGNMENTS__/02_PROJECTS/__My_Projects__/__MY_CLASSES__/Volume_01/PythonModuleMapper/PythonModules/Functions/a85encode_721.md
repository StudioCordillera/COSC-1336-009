---
type: function
name: a85encode
module: base64
lineno: 326
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: a85encode()

## Overview

Encode bytes-like object b using Ascii85 and return a bytes object.

foldspaces is an optional flag that uses the special short sequence 'y'
instead of 4 consecutive spaces (ASCII 0x20) as supported by 'btoa'. This
feature is not supported by the "standard" Adobe encoding.

wrapcol controls whether the output should have newline (b'\n') characters
added to it. If this is non-zero, each output line will be at most this
many characters long, excluding the trailing newline.

pad controls whether the input is padded to a multiple of 4 before
encoding. Note that the btoa implementation always pads.

adobe controls whether the encoded byte sequence is framed with <~ and ~>,
which is used by the Adobe implementation.

```python
def a85encode(b)
```

**Module:** [[Modules/base64|base64]]
**Type:** Module-level function
**Line:** 326
