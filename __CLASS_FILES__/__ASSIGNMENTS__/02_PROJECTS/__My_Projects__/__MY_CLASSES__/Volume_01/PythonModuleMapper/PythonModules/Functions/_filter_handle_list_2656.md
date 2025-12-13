---
type: function
name: _filter_handle_list
module: subprocess
lineno: 1439
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _filter_handle_list()

## Overview

Filter out console handles that can't be used
in lpAttributeList["handle_list"] and make sure the list
isn't empty. This also removes duplicate handles.

```python
def _filter_handle_list(self, handle_list)
```

**Module:** [[Modules/subprocess|subprocess]]
**Class:** [[Classes/Popen|Popen]]
**Type:** Method
**Line:** 1439

## Categories

- [[Taxonomy/protected_method|protected_method]]
