---
type: function
name: architecture
module: platform
lineno: 759
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: architecture()

## Overview

Queries the given executable (defaults to the Python interpreter
binary) for various architecture information.

Returns a tuple (bits, linkage) which contains information about
the bit architecture and the linkage format used for the
executable. Both values are returned as strings.

Values that cannot be determined are returned as given by the
parameter presets. If bits is given as '', the sizeof(pointer)
(or sizeof(long) on Python version < 1.5.2) is used as
indicator for the supported pointer size.

The function relies on the system's "file" command to do the
actual work. This is available on most if not all Unix
platforms. On some non-Unix platforms where the "file" command
does not exist and the executable is set to the Python interpreter
binary defaults from _default_architecture are used.

```python
def architecture(executable, bits, linkage)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 759
