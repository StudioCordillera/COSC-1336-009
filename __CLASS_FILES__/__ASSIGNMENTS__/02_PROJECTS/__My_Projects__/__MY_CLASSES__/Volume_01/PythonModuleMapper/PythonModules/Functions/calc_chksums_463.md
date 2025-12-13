---
type: function
name: calc_chksums
module: tarfile
lineno: 224
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: calc_chksums()

## Overview

Calculate the checksum for a member's header by summing up all
characters except for the chksum field which is treated as if
it was filled with spaces. According to the GNU tar sources,
some tars (Sun and NeXT) calculate chksum with signed char,
which will be different if there are chars in the buffer with
the high bit set. So we calculate two checksums, unsigned and
signed.

```python
def calc_chksums(buf)
```

**Module:** [[Modules/tarfile|tarfile]]
**Type:** Module-level function
**Line:** 224
