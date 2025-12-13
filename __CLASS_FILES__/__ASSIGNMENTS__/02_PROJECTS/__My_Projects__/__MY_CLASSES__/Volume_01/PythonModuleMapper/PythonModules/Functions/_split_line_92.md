---
type: function
name: _split_line
module: difflib
lineno: 1755
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _split_line()

## Overview

Builds list of text lines by splitting text lines at wrap point

This function will determine if the input text line needs to be
wrapped (split) into separate lines.  If so, the first wrap point
will be determined and the first line appended to the output
text line list.  This function is used recursively to handle
the second part of the split line to further split it.

```python
def _split_line(self, data_list, line_num, text)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/HtmlDiff|HtmlDiff]]
**Type:** Method
**Line:** 1755

## Categories

- [[Taxonomy/protected_method|protected_method]]
