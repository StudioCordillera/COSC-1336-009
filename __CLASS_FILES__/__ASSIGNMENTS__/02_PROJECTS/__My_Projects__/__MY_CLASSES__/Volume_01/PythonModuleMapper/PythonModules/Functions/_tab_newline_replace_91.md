---
type: function
name: _tab_newline_replace
module: difflib
lineno: 1732
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _tab_newline_replace()

## Overview

Returns from/to line lists with tabs expanded and newlines removed.

Instead of tab characters being replaced by the number of spaces
needed to fill in to the next tab stop, this function will fill
the space with tab characters.  This is done so that the difference
algorithms can identify changes in a file when tabs are replaced by
spaces and vice versa.  At the end of the HTML generation, the tab
characters will be replaced with a nonbreakable space.

```python
def _tab_newline_replace(self, fromlines, tolines)
```

**Module:** [[Modules/difflib|difflib]]
**Class:** [[Classes/HtmlDiff|HtmlDiff]]
**Type:** Method
**Line:** 1732

## Categories

- [[Taxonomy/protected_method|protected_method]]
