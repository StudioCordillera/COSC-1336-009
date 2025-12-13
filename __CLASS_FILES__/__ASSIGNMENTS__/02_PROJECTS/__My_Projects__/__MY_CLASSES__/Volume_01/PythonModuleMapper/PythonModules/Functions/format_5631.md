---
type: function
name: format
module: traceback
lineno: 738
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: format()

## Overview

Format the stack ready for printing.

Returns a list of strings ready for printing.  Each string in the
resulting list corresponds to a single frame from the stack.
Each string ends in a newline; the strings may contain internal
newlines as well, for those items with source text lines.

For long sequences of the same frame and line, the first few
repetitions are shown, followed by a summary line stating the exact
number of further repetitions.

```python
def format(self)
```

**Module:** [[Modules/traceback|traceback]]
**Class:** [[Classes/StackSummary|StackSummary]]
**Type:** Method
**Line:** 738

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
