---
type: function
name: colormode
module: turtle
lineno: 1171
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: colormode()

## Overview

Return the colormode or set it to 1.0 or 255.

Optional argument:
cmode -- one of the values 1.0 or 255

r, g, b values of colortriples have to be in range 0..cmode.

Example (for a TurtleScreen instance named screen):
>>> screen.colormode()
1.0
>>> screen.colormode(255)
>>> pencolor(240,160,80)

```python
def colormode(self, cmode)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1171

## Categories

- [[Taxonomy/public_method|public_method]]
