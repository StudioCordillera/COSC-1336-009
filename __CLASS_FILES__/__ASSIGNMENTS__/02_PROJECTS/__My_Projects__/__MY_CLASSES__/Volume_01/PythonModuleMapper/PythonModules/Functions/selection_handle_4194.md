---
type: function
name: selection_handle
module: tkinter
lineno: 1126
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: selection_handle()

## Overview

Specify a function COMMAND to call if the X
selection owned by this widget is queried by another
application.

This function must return the contents of the
selection. The function will be called with the
arguments OFFSET and LENGTH which allows the chunking
of very long selections. The following keyword
parameters can be provided:
selection - name of the selection (default PRIMARY),
type - type of the selection (e.g. STRING, FILE_NAME).

```python
def selection_handle(self, command)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Misc|Misc]]
**Type:** Method
**Line:** 1126

## Categories

- [[Taxonomy/public_method|public_method]]
