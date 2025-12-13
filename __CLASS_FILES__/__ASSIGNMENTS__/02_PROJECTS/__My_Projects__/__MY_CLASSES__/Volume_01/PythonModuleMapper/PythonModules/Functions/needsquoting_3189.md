---
type: function
name: needsquoting
module: quopri
lineno: 21
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: needsquoting()

## Overview

Decide whether a particular byte ordinal needs to be quoted.

The 'quotetabs' flag indicates whether embedded tabs and spaces should be
quoted.  Note that line-ending tabs and spaces are always encoded, as per
RFC 1521.

```python
def needsquoting(c, quotetabs, header)
```

**Module:** [[Modules/quopri|quopri]]
**Type:** Module-level function
**Line:** 21
