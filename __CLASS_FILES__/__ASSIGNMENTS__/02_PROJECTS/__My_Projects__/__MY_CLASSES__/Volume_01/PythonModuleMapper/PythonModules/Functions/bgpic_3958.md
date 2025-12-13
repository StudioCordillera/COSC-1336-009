---
type: function
name: bgpic
module: turtle
lineno: 1452
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: bgpic()

## Overview

Set background image or return name of current backgroundimage.

Optional argument:
picname -- a string, name of a gif-file or "nopic".

If picname is a filename, set the corresponding image as background.
If picname is "nopic", delete backgroundimage, if present.
If picname is None, return the filename of the current backgroundimage.

Example (for a TurtleScreen instance named screen):
>>> screen.bgpic()
'nopic'
>>> screen.bgpic("landscape.gif")
>>> screen.bgpic()
'landscape.gif'

```python
def bgpic(self, picname)
```

**Module:** [[Modules/turtle|turtle]]
**Class:** [[Classes/TurtleScreen|TurtleScreen]]
**Type:** Method
**Line:** 1452

## Categories

- [[Taxonomy/public_method|public_method]]
