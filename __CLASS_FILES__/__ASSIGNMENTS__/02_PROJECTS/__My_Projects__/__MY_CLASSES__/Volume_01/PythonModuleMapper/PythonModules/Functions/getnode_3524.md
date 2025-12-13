---
type: function
name: getnode
module: uuid
lineno: 637
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getnode()

## Overview

Get the hardware address as a 48-bit positive integer.

The first time this runs, it may launch a separate program, which could
be quite slow.  If all attempts to obtain the hardware address fail, we
choose a random 48-bit number with its eighth bit set to 1 as recommended
in RFC 4122.

```python
def getnode()
```

**Module:** [[Modules/uuid|uuid]]
**Type:** Module-level function
**Line:** 637
