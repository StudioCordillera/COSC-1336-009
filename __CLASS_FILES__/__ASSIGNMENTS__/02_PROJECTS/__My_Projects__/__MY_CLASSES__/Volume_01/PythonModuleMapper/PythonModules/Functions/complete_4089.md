---
type: function
name: complete
module: cmd
lineno: 258
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: complete()

## Overview

Return the next possible completion for 'text'.

If a command has not been entered, then complete against command list.
Otherwise try to call complete_<command> to get list of completions.

```python
def complete(self, text, state)
```

**Module:** [[Modules/cmd|cmd]]
**Class:** [[Classes/Cmd|Cmd]]
**Type:** Method
**Line:** 258

## Categories

- [[Taxonomy/public_method|public_method]]
