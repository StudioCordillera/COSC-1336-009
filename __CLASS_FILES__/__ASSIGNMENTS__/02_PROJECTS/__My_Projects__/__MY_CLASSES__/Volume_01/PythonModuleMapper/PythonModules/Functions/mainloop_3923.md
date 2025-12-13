---
type: function
name: mainloop
module: turtle
lineno: 789
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: mainloop()

## Overview

Starts event loop - calling Tkinter's mainloop function.

No argument.

Must be last statement in a turtle graphics program.
Must NOT be used if a script is run from within IDLE in -n mode
(No subprocess) - for interactive use of turtle graphics.

Example (for a TurtleScreen instance named screen):
>>> screen.mainloop()

```python
def mainloop(self)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreenBase|TurtleScreenBase]]
**Type:** Method
**Line:** 789

## Categories

- [[Taxonomy/public_method|public_method]]
