---
type: function
name: extract
module: traceback
lineno: 432
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: extract()

## Overview

Create a StackSummary from a traceback or stack object.

:param frame_gen: A generator that yields (frame, lineno) tuples
    whose summaries are to be included in the stack.
:param limit: None to include all frames or the number of frames to
    include.
:param lookup_lines: If True, lookup lines for each frame immediately,
    otherwise lookup is deferred until the frame is rendered.
:param capture_locals: If True, the local variables from each frame will
    be captured as object representations into the FrameSummary.

```python
@classmethod
def extract(klass, frame_gen)
```

**Module:** [[Modules/traceback|traceback]]
**Class:** [[Classes/StackSummary|StackSummary]]
**Type:** Method
**Line:** 432

## Categories

- [[Taxonomy/public_method|public_method]]
