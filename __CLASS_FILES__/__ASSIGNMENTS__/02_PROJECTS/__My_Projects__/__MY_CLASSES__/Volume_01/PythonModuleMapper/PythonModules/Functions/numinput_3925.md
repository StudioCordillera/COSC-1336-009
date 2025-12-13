---
type: function
name: numinput
module: turtle
lineno: 819
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: numinput()

## Overview

Pop up a dialog window for input of a number.

Arguments: title is the title of the dialog window,
prompt is a text mostly describing what numerical information to input.
default: default value
minval: minimum value for input
maxval: maximum value for input

The number input must be in the range minval .. maxval if these are
given. If not, a hint is issued and the dialog remains open for
correction. Return the number input.
If the dialog is canceled,  return None.

Example (for a TurtleScreen instance named screen):
>>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

```python
def numinput(self, title, prompt, default, minval, maxval)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 819

## Categories

- [[Taxonomy/public_method|public_method]]
