---
type: function
name: _syscmd_ver
module: platform
lineno: 266
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _syscmd_ver()

## Overview

Tries to figure out the OS version used and returns
a tuple (system, release, version).

It uses the "ver" shell command for this which is known
to exists on Windows, DOS. XXX Others too ?

In case this fails, the given parameters are used as
defaults.

```python
def _syscmd_ver(system, release, version, supported_platforms)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 266
