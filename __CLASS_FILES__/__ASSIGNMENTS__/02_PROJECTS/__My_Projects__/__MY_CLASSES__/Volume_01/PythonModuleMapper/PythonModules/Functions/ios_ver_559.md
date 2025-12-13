---
type: function
name: ios_ver
module: platform
lineno: 509
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: ios_ver()

## Overview

Get iOS version information, and return it as a namedtuple:
    (system, release, model, is_simulator).

If values can't be determined, they are set to values provided as
parameters.

```python
def ios_ver(system, release, model, is_simulator)
```

**Module:** [[Modules/platform|platform]]
**Type:** Module-level function
**Line:** 509
