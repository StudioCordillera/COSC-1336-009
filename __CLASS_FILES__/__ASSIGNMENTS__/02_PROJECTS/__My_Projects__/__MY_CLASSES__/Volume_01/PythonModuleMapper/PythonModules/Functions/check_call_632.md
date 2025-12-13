---
type: function
name: check_call
module: subprocess
lineno: 404
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: check_call()

## Overview

Run command with arguments.  Wait for command to complete.  If
the exit code was zero then return, otherwise raise
CalledProcessError.  The CalledProcessError object will have the
return code in the returncode attribute.

The arguments are the same as for the call function.  Example:

check_call(["ls", "-l"])

```python
def check_call()
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 404
