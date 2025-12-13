---
type: function
name: get_stack
module: bdb
lineno: 594
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_stack()

## Overview

Return a list of (frame, lineno) in a stack trace and a size.

List starts with original calling frame, if there is one.
Size may be number of frames above or below f.

```python
def get_stack(self, f, t)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 594

## Categories

- [[Taxonomy/accessor|accessor]]
