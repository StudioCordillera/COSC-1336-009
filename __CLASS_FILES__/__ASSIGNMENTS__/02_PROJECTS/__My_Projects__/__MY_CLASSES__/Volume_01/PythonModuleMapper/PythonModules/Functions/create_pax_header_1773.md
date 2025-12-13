---
type: function
name: create_pax_header
module: tarfile
lineno: 1067
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: create_pax_header()

## Overview

Return the object as a ustar header block. If it cannot be
represented this way, prepend a pax extended header sequence
with supplement information.

```python
def create_pax_header(self, info, encoding)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarInfo|TarInfo]]
**Type:** Method
**Line:** 1067

## Categories

- [[Taxonomy/public_method|public_method]]
