---
type: function
name: make_file
module: difflib
lineno: 1705
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: make_file()

## Overview

Returns HTML file of side by side comparison with change highlights

Arguments:
fromlines -- list of "from" lines
tolines -- list of "to" lines
fromdesc -- "from" file column header string
todesc -- "to" file column header string
context -- set to True for contextual differences (defaults to False
    which shows full differences).
numlines -- number of context lines.  When context is set True,
    controls number of lines displayed before and after the change.
    When context is False, controls the number of lines to place
    the "next" link anchors before the next change (so click of
    "next" link jumps to just before the change).
charset -- charset of the HTML document

```python
def make_file(self, fromlines, tolines, fromdesc, todesc, context, numlines)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/HtmlDiff|HtmlDiff]]
**Type:** Method
**Line:** 1705

## Categories

- [[Taxonomy/public_method|public_method]]
