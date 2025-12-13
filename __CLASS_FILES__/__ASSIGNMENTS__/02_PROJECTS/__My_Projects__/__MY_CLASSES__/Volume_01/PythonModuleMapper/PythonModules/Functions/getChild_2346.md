---
type: function
name: getChild
module: logging
lineno: 1791
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: getChild()

## Overview

Get a logger which is a descendant to this one.

This is a convenience method, such that

logging.getLogger('abc').getChild('def.ghi')

is the same as

logging.getLogger('abc.def.ghi')

It's useful, for example, when the parent logger is named using
__name__ rather than a literal string.

```python
def getChild(self, suffix)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/Logger|Logger]]
**Type:** Method
**Line:** 1791

## Categories

- [[Taxonomy/public_method|public_method]]
