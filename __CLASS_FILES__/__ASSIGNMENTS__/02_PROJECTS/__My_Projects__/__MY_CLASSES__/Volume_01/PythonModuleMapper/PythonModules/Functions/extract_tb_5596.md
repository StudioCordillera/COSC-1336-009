---
type: function
name: extract_tb
module: traceback
lineno: 65
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: extract_tb()

## Overview

Return a StackSummary object representing a list of
pre-processed entries from traceback.

This is useful for alternate formatting of stack traces.  If
'limit' is omitted or None, all entries are extracted.  A
pre-processed stack trace entry is a FrameSummary object
containing attributes filename, lineno, name, and line
representing the information that is usually printed for a stack
trace.  The line is a string with leading and trailing
whitespace stripped; if the source is not available it is None.

```python
def extract_tb(tb, limit)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 65
