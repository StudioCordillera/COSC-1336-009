---
type: function
name: getabsfile
module: inspect
lineno: 988
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getabsfile()

## Overview

Return an absolute path to the source or compiled file for an object.

The idea is for each object to have a unique origin, so this routine
normalizes the result as much as possible.

```python
def getabsfile(object, _filename)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 988
