---
type: function
name: _set_stopinfo
module: bdb
lineno: 319
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - mutator
---

# Function: _set_stopinfo()

## Overview

Set the attributes for stopping.

If stoplineno is greater than or equal to 0, then stop at line
greater than or equal to the stopline.  If stoplineno is -1, then
don't stop at all.

```python
def _set_stopinfo(self, stopframe, returnframe, stoplineno, opcode)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 319

## Categories

- [[Taxonomy/mutator|mutator]]
