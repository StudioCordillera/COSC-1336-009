---
type: function
name: globaltrace_lt
module: trace
lineno: 534
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: globaltrace_lt()

## Overview

Handler for call events.

If the code block being entered is to be ignored, returns `None',
else returns self.localtrace.

```python
def globaltrace_lt(self, frame, why, arg)
```

**Module:** [[Modules/trace|trace]]
**Class:** [[Classes/Trace|Trace]]
**Type:** Method
**Line:** 534

## Categories

- [[Taxonomy/public_method|public_method]]
