---
type: function
name: find_first_executable_line
module: pdb
lineno: 105
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: find_first_executable_line()

## Overview

Try to find the first executable line of the code object.

Equivalently, find the line number of the instruction that's
after RESUME

Return code.co_firstlineno if no executable line is found.

```python
def find_first_executable_line(code)
```

**Module:** [[Modules/pdb|pdb]]
**Type:** Module-level function
**Line:** 105
