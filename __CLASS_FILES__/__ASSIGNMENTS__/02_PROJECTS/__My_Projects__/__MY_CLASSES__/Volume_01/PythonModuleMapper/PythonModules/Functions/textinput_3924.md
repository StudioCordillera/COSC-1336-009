---
type: function
name: textinput
module: turtle
lineno: 804
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: textinput()

## Overview

Pop up a dialog window for input of a string.

Arguments: title is the title of the dialog window,
prompt is a text mostly describing what information to input.

Return the string input
If the dialog is canceled, return None.

Example (for a TurtleScreen instance named screen):
>>> screen.textinput("NIM", "Name of first player:")

```python
def textinput(self, title, prompt)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 804

## Categories

- [[Taxonomy/public_method|public_method]]
