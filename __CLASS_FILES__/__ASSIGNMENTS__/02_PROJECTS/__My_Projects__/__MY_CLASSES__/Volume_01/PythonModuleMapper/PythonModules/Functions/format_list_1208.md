---
type: function
name: format_list
module: traceback
lineno: 33
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: format_list()

## Overview

Format a list of tuples or FrameSummary objects for printing.

Given a list of tuples or FrameSummary objects as returned by
extract_tb() or extract_stack(), return a list of strings ready
for printing.

Each string in the resulting list corresponds to the item with the
same index in the argument list.  Each string ends in a newline;
the strings may contain internal newlines as well, for those items
whose source text line is not None.

```python
def format_list(extracted_list)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 33
