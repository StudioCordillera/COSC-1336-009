---
type: function
name: getoutput
module: subprocess
lineno: 687
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getoutput()

## Overview

Return output (stdout or stderr) of executing cmd in a shell.

Like getstatusoutput(), except the exit status is ignored and the return
value is a string containing the command's output.  Example:

>>> import subprocess
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

```python
def getoutput(cmd)
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 687
