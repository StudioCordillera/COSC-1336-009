---
type: function
name: _sys_version
module: platform
lineno: 1128
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _sys_version()

## Overview

Returns a parsed version of Python's sys.version as tuple
(name, version, branch, revision, buildno, builddate, compiler)
referring to the Python implementation name, version, branch,
revision, build number, build date/time as string and the compiler
identification string.

Note that unlike the Python sys.version, the returned value
for the Python version will always include the patchlevel (it
defaults to '.0').

The function returns empty strings for tuple entries that
cannot be determined.

sys_version may be given to parse an alternative version
string, e.g. if the version was read from a different Python
interpreter.

```python
def _sys_version(sys_version)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 1128
