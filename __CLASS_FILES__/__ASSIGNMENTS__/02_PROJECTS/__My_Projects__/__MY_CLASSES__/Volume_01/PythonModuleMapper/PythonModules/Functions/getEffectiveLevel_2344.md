---
type: function
name: getEffectiveLevel
module: logging
lineno: 1758
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: getEffectiveLevel()

## Overview

Get the effective level for this logger.

Loop through this logger and its parents in the logger hierarchy,
looking for a non-zero logging level. Return the first one found.

```python
def getEffectiveLevel(self)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Logger|Logger]]
**Type:** Method
**Line:** 1758

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
