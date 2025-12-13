---
type: function
name: getstatusoutput
module: subprocess
lineno: 655
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getstatusoutput()

## Overview

Return (exitcode, output) of executing cmd in a shell.

Execute the string 'cmd' in a shell with 'check_output' and
return a 2-tuple (status, output). The locale encoding is used
to decode the output and process newlines.

A trailing newline is stripped from the output.
The exit status for the command can be interpreted
according to the rules for the function 'wait'. Example:

>>> import subprocess
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
>>> subprocess.getstatusoutput('cat /bin/junk')
(1, 'cat: /bin/junk: No such file or directory')
>>> subprocess.getstatusoutput('/bin/junk')
(127, 'sh: /bin/junk: not found')
>>> subprocess.getstatusoutput('/bin/kill $$')
(-15, '')

```python
def getstatusoutput(cmd)
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 655
