---
type: function
name: globaltrace_countfuncs
module: trace
lineno: 525
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: globaltrace_countfuncs()

## Overview

Handler for call events.

Adds (filename, modulename, funcname) to the self._calledfuncs dict.

```python
def globaltrace_countfuncs(self, frame, why, arg)
```

**Module:** [[Modules/trace|trace]]
**Class:** [[Classes/Trace|Trace]]
**Type:** Method
**Line:** 525

## Categories

- [[Taxonomy/public_method|public_method]]
