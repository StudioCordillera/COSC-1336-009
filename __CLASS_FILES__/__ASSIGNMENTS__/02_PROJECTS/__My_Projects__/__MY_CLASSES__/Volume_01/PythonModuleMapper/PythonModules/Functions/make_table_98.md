---
type: function
name: make_table
module: difflib
lineno: 1940
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: make_table()

## Overview

Returns HTML table of side by side comparison with change highlights

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

```python
def make_table(self, fromlines, tolines, fromdesc, todesc, context, numlines)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/HtmlDiff|HtmlDiff]]
**Type:** Method
**Line:** 1940

## Categories

- [[Taxonomy/public_method|public_method]]
