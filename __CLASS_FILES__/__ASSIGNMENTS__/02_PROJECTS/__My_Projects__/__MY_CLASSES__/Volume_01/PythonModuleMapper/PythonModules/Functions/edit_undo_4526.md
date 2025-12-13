---
type: function
name: edit_undo
module: tkinter
lineno: 3922
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: edit_undo()

## Overview

Undoes the last edit action

If the undo option is true. An edit action is defined
as all the insert and delete commands that are recorded
on the undo stack in between two separators. Generates
an error when the undo stack is empty. Does nothing
when the undo option is false

```python
def edit_undo(self)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Text|Text]]
**Type:** Method
**Line:** 3922

## Categories

- [[Taxonomy/public_method|public_method]]
