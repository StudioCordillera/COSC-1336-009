---
type: function
name: open
module: shelve
lineno: 237
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: open()

## Overview

Open a persistent dictionary for reading and writing.

The filename parameter is the base filename for the underlying
database.  As a side-effect, an extension may be added to the
filename and more than one file may be created.  The optional flag
parameter has the same interpretation as the flag parameter of
dbm.open(). The optional protocol parameter specifies the
version of the pickle protocol.

See the module's __doc__ string for an overview of the interface.

```python
def open(filename, flag, protocol, writeback)
```

**Module:** [[Modules/shelve|shelve]]
**Type:** Module-level function
**Line:** 237
