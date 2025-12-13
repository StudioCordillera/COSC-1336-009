---
type: function
name: getLogger
module: logging
lineno: 1362
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: getLogger()

## Overview

Get a logger with the specified name (channel name), creating it
if it doesn't yet exist. This name is a dot-separated hierarchical
name, such as "a", "a.b", "a.b.c" or similar.

If a PlaceHolder existed for the specified name [i.e. the logger
didn't exist but a child of it did], replace it with the created
logger and fix up the parent/child references which pointed to the
placeholder to now point to the logger.

```python
def getLogger(self, name)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Manager|Manager]]
**Type:** Method
**Line:** 1362

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
