---
type: function
name: java_ver
module: platform
lineno: 536
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: java_ver()

## Overview

Version interface for Jython.

Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
tuple (os_name, os_version, os_arch).

Values which cannot be determined are set to the defaults
given as parameters (which all default to '').

```python
def java_ver(release, vendor, vminfo, osinfo)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 536
