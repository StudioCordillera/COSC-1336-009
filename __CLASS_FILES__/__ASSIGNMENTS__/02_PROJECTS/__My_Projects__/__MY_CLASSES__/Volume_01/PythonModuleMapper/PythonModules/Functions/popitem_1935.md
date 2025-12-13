---
type: function
name: popitem
module: configparser
lineno: 892
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: popitem()

## Overview

Remove a section from the parser and return it as
a (section_name, section_proxy) tuple. If no section is present, raise
KeyError.

The section DEFAULT is never returned because it cannot be removed.

```python
def popitem(self)
```

**Module:** [[Modules/configparser|configparser]]
**Class:** [[Classes/RawConfigParser|RawConfigParser]]
**Type:** Method
**Line:** 892
