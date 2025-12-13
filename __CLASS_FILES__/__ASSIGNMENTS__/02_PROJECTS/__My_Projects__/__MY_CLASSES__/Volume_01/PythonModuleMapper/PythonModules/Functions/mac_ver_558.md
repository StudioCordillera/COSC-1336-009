---
type: function
name: mac_ver
module: platform
lineno: 482
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: mac_ver()

## Overview

Get macOS version information and return it as tuple (release,
versioninfo, machine) with versioninfo being a tuple (version,
dev_stage, non_release_version).

Entries which cannot be determined are set to the parameter values
which default to ''. All tuple entries are strings.

```python
def mac_ver(release, versioninfo, machine)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 482
