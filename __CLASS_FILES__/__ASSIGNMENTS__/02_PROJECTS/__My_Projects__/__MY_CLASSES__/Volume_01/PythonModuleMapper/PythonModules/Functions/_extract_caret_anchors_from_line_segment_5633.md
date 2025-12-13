---
type: function
name: _extract_caret_anchors_from_line_segment
module: traceback
lineno: 805
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _extract_caret_anchors_from_line_segment()

## Overview

Given source code `segment` corresponding to a FrameSummary, determine:
    - for binary ops, the location of the binary op
    - for indexing and function calls, the location of the brackets.
`segment` is expected to be a valid Python expression.

```python
def _extract_caret_anchors_from_line_segment(segment)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 805
